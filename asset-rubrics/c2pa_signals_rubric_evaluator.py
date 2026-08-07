import re
import yaml
import json
import sys
from c2pa_conformance_rubric_evaluator import create_json_formula_engine


def create_index_mapping(data):
    mapping = {}
    if "manifests" not in data:
        return mapping

    for idx, manifest in enumerate(data["manifests"]):
        label = manifest.get("label")
        if label:
            mapping[label] = str(idx)
    return mapping


def build_provenance_dag(data, index_mapping):
    dag = {}
    if "manifests" not in data:
        return dag

    # First, populate all normal manifests
    for manifest in data["manifests"]:
        label = manifest.get("label")
        if not label:
            continue

        node_id = index_mapping.get(label, "Unknown")

        dag[node_id] = {
            "urn": label,
            "manifest": manifest,
            "edges": [],
            "signals": [],
            "is_pseudo": False
        }

        claim = manifest.get("claim.v2") or manifest.get("claim") or {}
        mime_type = claim.get("dc:format")
        if mime_type:
            dag[node_id]["mime_type"] = mime_type

    # Now, scan for flat ingredients and create pseudo nodes
    next_node_index = len(data.get("manifests", []))

    for manifest in data["manifests"]:
        label = manifest.get("label")
        if not label:
            continue

        node_id = index_mapping.get(label, "Unknown")
        assertions = manifest.get("assertions", {})

        for key, value in assertions.items():
            if key.startswith("c2pa.ingredient"):
                active_manifest = value.get("activeManifest")
                url = active_manifest.get("url") if active_manifest else None
                relationship = value.get("relationship")

                if url:
                    # Normal ingredient with active manifest
                    parent_urn = url
                    if "urn:c2pa:" in url:
                        idx = url.find("urn:c2pa:")
                        parent_urn = url[idx:]
                        if "/" in parent_urn:
                            parent_urn = parent_urn.split("/")[0]

                    parent_id = index_mapping.get(parent_urn, parent_urn)

                    dag[node_id]["edges"].append({
                        "parent": parent_id,
                        "relationship": relationship
                    })

                    mime_type = value.get("dc:format")
                    if mime_type and parent_id in dag and "mime_type" not in dag[parent_id]:
                        dag[parent_id]["mime_type"] = mime_type
                else:
                    # Flat ingredient: no active manifest url, but check if it has a digitalSourceType!
                    dst = value.get("digitalSourceType")
                    if not dst:
                        # Check if any actions assertion contains a c2pa.opened action with digitalSourceType
                        for a_key, a_val in assertions.items():
                            if a_key.startswith("c2pa.actions"):
                                for act in a_val.get("actions", []):
                                    if act.get("action") == "c2pa.opened" and act.get("digitalSourceType"):
                                        dst = act.get("digitalSourceType")
                                        break
                                if dst:
                                    break
                    if dst:
                        pseudo_id = str(next_node_index)
                        next_node_index += 1

                        # Generate a pseudo label
                        title = value.get("dc:title", "flat-ingredient")
                        # Clean title to form a label URN
                        safe_title = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', title)
                        pseudo_label = f"urn:c2pa:pseudo:{label}:{safe_title}_{pseudo_id}"

                        # Synthesize a mock manifest
                        pseudo_manifest = {
                            "label": pseudo_label,
                            "assertions": {
                                "c2pa.actions.v2": {
                                    "allActionsIncluded": True,
                                    "actions": [
                                        {
                                            "action": "c2pa.created",
                                            "digitalSourceType": dst
                                        }
                                    ]
                                }
                            }
                        }

                        # Add pseudo node to DAG
                        dag[pseudo_id] = {
                            "urn": pseudo_label,
                            "manifest": pseudo_manifest,
                            "edges": [],
                            "signals": [],
                            "is_pseudo": True,
                            "parent_node_id": node_id,  # Link back to the parent manifest that asserted it
                            "mime_type": value.get("dc:format")
                        }

                        # Add edge from parent to pseudo node
                        dag[node_id]["edges"].append({
                            "parent": pseudo_id,
                            "relationship": relationship
                        })

            elif key.startswith("c2pa.thumbnail"):
                mime_type = value.get("format")
                if mime_type and "mime_type" not in dag[node_id]:
                    dag[node_id]["mime_type"] = mime_type

    return dag


def evaluate_asset(rubric_path, json_path=None, debug=False, data_dict=None):
    if data_dict is not None:
        data = data_dict
    elif json_path is not None:
        with open(json_path, 'r') as f:
            data = json.load(f)
    else:
        raise ValueError("Either json_path or data_dict must be provided")


    index_mapping = create_index_mapping(data)
    dag = build_provenance_dag(data, index_mapping)

    print(f"Built DAG with {len(dag)} nodes.", file=sys.stderr)
    print(f"Index mapping: {index_mapping}", file=sys.stderr)

    # Load rubric
    with open(rubric_path, 'r') as f:
        docs = list(yaml.safe_load_all(f))

    metadata = docs[0] if len(docs) > 0 and isinstance(docs[0], dict) else {}
    rubric_name = metadata.get("rubric_metadata", {}).get("name", "Unknown")
    rubric_version = metadata.get("rubric_metadata", {}).get("version", "Unknown")

    # Create json-formula engine with variables/expressions from metadata
    engine, variables = create_json_formula_engine(metadata, debug=debug)

    statements = []
    for doc in docs[1:]:
        if isinstance(doc, list):
            statements.extend(doc)
        elif isinstance(doc, dict):
            if "block" not in doc:
                statements.append(doc)

    # Node-local evaluation: each expression evaluates against the individual manifest
    for node_id, node in dag.items():
        manifest = node["manifest"]
        for stmt in statements:
            expr = stmt.get("expression")
            trait = stmt.get("id")

            if not expr or not trait:
                continue

            try:
                # Evaluate expression against the single manifest (not the full crJSON)
                val = engine.search(expr.strip(), manifest, globals=variables)

                bool_val = False
                is_multiple = False
                if isinstance(val, list):
                    bool_val = len(val) > 0
                    is_multiple = len(val) > 1
                elif isinstance(val, bool):
                    bool_val = val
                elif isinstance(val, (int, float)):
                    bool_val = val > 0
                elif val is not None:
                    bool_val = True

                if bool_val:
                    node["signals"].append({
                        "trait": trait,
                        "reportText": stmt.get("reportText", {}).get("true", {}).get("en", trait),
                        "multiple": is_multiple
                    })
            except Exception as e:
                if debug:
                    import traceback
                    traceback.print_exc()
                print(f"Error evaluating {trait} on node {node_id}: {e}", file=sys.stderr)

    output_manifests = []

    # Consolidate non-pseudo manifests first, then all pseudo manifests at the end of the array
    sorted_node_ids = sorted(
        dag.keys(),
        key=lambda x: (1 if dag[x].get("is_pseudo", False) else 0, int(x))
    )

    old_to_new_idx = {old_id: new_idx for new_idx, old_id in enumerate(sorted_node_ids)}

    for node_id in sorted_node_ids:
        dag_node = dag[node_id]
        is_pseudo = dag_node.get("is_pseudo", False)

        if not is_pseudo:
            orig_manifest = dag_node["manifest"]
            subject = orig_manifest.get("signature", {}).get("certificateInfo", {}).get("subject", {})
            cn = subject.get("CN", "Unknown CN")
            o = subject.get("O", "Unknown O")
            ou = subject.get("OU")

            subj_dict = {"CN": cn, "O": o}
            if ou:
                subj_dict["OU"] = ou
            asserted_by = {"subject": subj_dict}
        else:
            # Pseudo manifest inherits assertedBy from its parent manifest node
            parent_id = dag_node["parent_node_id"]
            parent_dag_node = dag[parent_id]
            parent_manifest = parent_dag_node["manifest"]
            subject = parent_manifest.get("signature", {}).get("certificateInfo", {}).get("subject", {})
            cn = subject.get("CN", "Unknown CN")
            o = subject.get("O", "Unknown O")
            ou = subject.get("OU")

            subj_dict = {"CN": cn, "O": o}
            if ou:
                subj_dict["OU"] = ou
            asserted_by = {"subject": subj_dict}

        local_inceptions = []
        local_transformations = []

        signals = dag_node.get("signals", [])
        for sig in signals:
            trait = sig.get("trait")
            if trait.startswith("inception:"):
                local_inceptions.append(sig)
            elif trait.startswith("transformation:"):
                local_transformations.append(sig)

        ingredients = []
        for edge in dag_node.get("edges", []):
            parent_id_str = str(edge.get("parent"))
            relationship = edge.get("relationship")

            if parent_id_str in old_to_new_idx:
                ingredients.append({
                    "index": old_to_new_idx[parent_id_str],
                    "relationship": relationship
                })
            else:
                try:
                    parent_idx = int(parent_id_str)
                    ingredients.append({
                        "index": parent_idx,
                        "relationship": relationship
                    })
                except (ValueError, TypeError):
                    print(f"Warning: Could not map parent URN {parent_id_str} to index", file=sys.stderr)

        manifest_entry = {
            "assertedBy": asserted_by,
            "dc:format": dag_node.get("mime_type"),
            "localInceptions": local_inceptions,
            "localTransformations": local_transformations,
            "ingredients": ingredients
        }
        if is_pseudo:
            manifest_entry["pseudo"] = True

        output_manifests.append(manifest_entry)


    final_output = {
        "rubricName": rubric_name,
        "rubricVersion": rubric_version,
        "manifests": output_manifests
    }

    print(json.dumps(final_output, indent=2, ensure_ascii=False))
    return final_output


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Evaluate a C2PA asset against a signals rubric')
    parser.add_argument('rubric', help='Path to the signals rubric YAML file')
    parser.add_argument('asset', help='Path to the asset JSON file')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    args = parser.parse_args()

    evaluate_asset(args.rubric, args.asset, debug=args.debug)

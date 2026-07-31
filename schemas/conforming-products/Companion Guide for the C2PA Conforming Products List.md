---
author: C2PA Technical Working Group Conformance Task Force
date: 2026-07-31
title: Companion Guide to the C2PA Conforming Products List
---

# Introduction

With the increasing velocity of digital content and availability of powerful creation and editing techniques, establishing the provenance of media is critical to ensure transparency, understanding, and ultimately, trust.

To address this issue at scale for publishers, creators and consumers, the Coalition for Content Provenance and Authenticity (C2PA) has developed a technical specification for providing content provenance and authenticity. It is designed to enable global, opt-in, adoption of digital provenance techniques through the creation of a rich ecosystem of digital provenance enabled applications for a wide range of individuals and organizations while meeting appropriate security requirements.

The work of the C2PA is fluid as the organization has worked diligently to issue its Specification v2.2 while committing to a long-term Governance Framework and Conformance Program. While the release of Spec 2.2 precedes the implementation of a fully-formed Conformance Program this release introduces the implementation of C2PA Conforming Products List comprised of Claim Generator companies and applications that plan to use CA-issued signing certificates to sign Spec 2.2 compliant Claim Manifests under a minimal set of requirements in addition to self-asserting their compliance to the V2.2 Specification.

The C2PA Conforming Products List is essentially a database of approved Generator Products and Validator Products and the attributes of their implementations. The database is intended to be machine-readable by Certification Authorities (CA) which must interrogate this list prior to issuing C2PA Claim Signing Certificates per the requirements of the C2PA Certificate Policy, to ensure that they only issue certificates to applications included in this list.

The purpose of this Companion Guide is provide transparency over all of the attributes and fields included in this Products List so that CAs, Applicants to the C2PA Conformance Program that create Generator Products or Validator Products, as well as relying parties have full disclosure of the applications that C2PA approves within its Governance Framework and Conformance Program.

# Structure of the C2PA Conforming Products List

Each record in the list is an object containing the following main fields:

- `recordId`: A unique identifier for this specific product record in the Conforming Products List (CPL).

- `applicant`: The legal name of the organization that applied for C2PA conformance for the product.

- `product`: Contains detailed information about the product itself. This is further broken down into:

  - `productType`: Specifies whether the product is a "generatorProduct" (creates C2PA claims) or a "validatorProduct" (validates C2PA claims).

  - `DN` (Distinguished Name): Information that uniquely identifies the product.

    - `CN` (Common Name): The user-facing marketing name and/or model of the device, application, or service (e.g., "Awesome Camera App for Android").

    - `O` (Organization): Legal name of the Applicant organization.

    - `OU` (Organizational Unit): The specific department or subdivision within the Applicant’s organization responsible for the product (e.g., "Android Division").

    - `C` (Country): A two-letter country code (e.g., "US" for United States, "GB" for Great Britain) indicating where the Applicant organization is based.

  - `infoURL`: Optional URL containing additional information about the product (e.g., `https://example.com/product-info`).

  - `minVersion`: The minimum software or firmware version of this product that is considered conformant (e.g., "2.3.0").

  - `assurance` (Only for `generatorProduct`): Describes the security confidence level of the product’s implementation.

    - `maxAssuranceLevel`: A numeric designation (1 or 2) assigned by the C2PA Conformance Program, reflecting the evaluated security of the product. Higher numbers generally indicate greater security assurance.

    - `attestationMethods`: A list of supported methods for verifying the product’s integrity or key security (e.g., `Android_KeyAttestation`, `Apple_AppAttest`). These methods help ensure the product is genuine and hasn’t been tampered with.

  - `disallowedSignals` (Only for `generatorProduct`): Signals from the Signals Rubric that this generator product is explicitly disallowed from emitting in active manifests whose claims it signs.

    - `inception`: A list of disallowed inception signals (e.g., `capturedMedia`, `capturedMediaStitched`, `nonGenAIDigitalCreation`).

- `specVersion`: A list of the C2PA Content Credentials specification versions supported by this product (e.g., "2.2", "2.4").

- `conformanceProgramVersion`: The version of the C2PA Conformance Program that was in effect when the product was submitted for evaluation (e.g., "0.1", "0.2").

- `containers`: Details the file types (MIME types) the product supports for C2PA claim generation and/or validation. This is divided into:

  - `generate`: File types for which the product can **generate** assets with C2PA claims. This can include categories like:

    - `image` (e.g., `image/jpeg`, `image/png`, `image/webp`, `image/heic`, `image/avif`)

    - `video` (e.g., `video/mp4`, `video/quicktime`)

      > [!NOTE]
      > `video` does not distinguish between pre-recorded and liveVideo, see `liveVideo` key below.

    - `audio` (e.g., `audio/mpeg`, `audio/flac`, `audio/wav`)

    - `textHtml` (e.g., `text/html`)

    - `textUnstructured` (e.g., `text/csv`, `text/tab-separated-values`, `text/plain`)

    - `textStructured` (e.g., `text/markdown`, `text/xml`, `application/xml`, `application/xhtml+xml`)

    - `documents` (e.g., `application/pdf`, `application/epub+zip`)

    - `fonts` (e.g., `font/otf`)

    - `mlModel` (e.g., `pytorch`, `tensorflow`, `onnx`, `jax`, `keras`)

  - `validate`: File types for which the product can **validate** assets with C2PA claims. It supports the same categories of file types as `generate`.

    > [!NOTE]
    > Every CPL product record must specify support for at least `containers` OR `liveVideo` (or both).

- `liveVideo`: Identifies which (if any) C2PA live streams mechanisms the product supports for generating and/or validating claims in live streaming or dynamic packaging media contexts. NOTE: `liveVideo` isn’t constrained to only live video streaming, it can also apply to live audio streaming, or other live media streaming contexts.

  - `supported`: A boolean value indicating whether the product supports live stream claim generation and/or validation.

  - `encapsulations`: If `supported` is true, an array specifying supported encapsulation format objects:

    - `type`: The encapsulation format (`fMP4` or `CMAF`).

    - `methods`: The live stream signing methods supported for this encapsulation (`per-segment` or `verifiable-segment-info`).

    - `generation`: A boolean indicating whether generation of live streams in this encapsulation format is supported.

    - `validation`: A boolean indicating whether validation of live streams in this encapsulation format is supported.

- `supportsCompressedManifests`: A boolean value indicating whether the product supports compressed manifests (generating assets with compressed manifests for generator products, or validating assets containing compressed manifests for validator products).

- `status`: The current standing of the product in the C2PA Conformance Program. Possible values include:

  - `conformant`: The product is currently C2PA conformant.

  - `revoked`: Conformance was revoked for a general reason not covered by other specific "revoked" statuses.

  - `revoked_eol`: Conformance was revoked due to the product reaching its end-of-life.

  - `revoked_vulnerability`: Conformance was revoked due to a security vulnerability.

- `dates`: Important dates associated with this product record.

  - `creation`: The date this product record was initially created in the CPL.

  - `conformance`: The date the product was officially deemed conformant.

  - `earliestPublicDisclosure`: The earliest date this product record was permitted to be made public.

  - `lastModification`: The date this product record was last updated.

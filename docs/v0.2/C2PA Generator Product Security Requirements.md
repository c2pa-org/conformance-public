---
author: C2PA Technical Working Group Conformance Task Force
date: 2026-07-31
title: C2PA Generator Product Security Requirements
version: v0.2
---

# Scope

This document outlines the security requirements for the Generator Product (GP). Security requirements for the Validator Product are out of scope of this document.

# Glossary

## Administering Authority

The party that the C2PA [Governing Authority](#_governing_authority) empowers to operate its Conformance Program on its behalf. It recognizes and accredits key conformance roles which agree to participate in the program. The C2PA Conformance Task Force of the Technical Working Group operates in this capacity.

## Applicant

An entity that has created a [Generator Product](#_generator_product) or a [Validator Product](#_validator_product) and wishes for it to be deemed a [Conforming Product](#_conforming_product) according to the governance framework of the [C2PA Conformance Program](#_c2pa_conformance_program), and added to the [C2PA Conforming Products List](#_c2pa_conforming_products_list).

## Applicant’s Representative

A natural person who is a duly-authorized employee or agent of the [Applicant](#applicant).

## Assertion

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## Asset

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## Assurance Level

An indication to a [Relying Party](#_relying_party) of the level of confidence that it may have that assertions and claims signed with a given [C2PA Claim Signing Certificate](#claimsigning-certs) reflect the intended behavior of the [Generator Product](#_generator_product) instance. A higher Assurance Level allows the [Relying Party](#_relying_party) to have a greater level of confidence.

The Assurance Level is conveyed through the `c2pa-al` (`1.3.6.1.4.1.62558.3`) X.509 v3 certificate extension in a [C2PA Claim Signing Certificate](#claimsigning-certs). The value of this extension is an encoded OID value that corresponds to a numeric value no higher than the [Max Assurance Level](#_max_assurance_level) for a given conforming [Generator Product](#_generator_product). The OID values corresponding to each Assurance Level are defined in the C2PA `oid.txt` MIB definition file.

The Assurance Level in the [C2PA Claim Signing Certificate](#claimsigning-certs) that is issued to an instance of a conforming [Generator Product](#_generator_product) may be lower than the [Max Assurance Level](#_max_assurance_level) that the [Generator Product](#_generator_product) is potentially eligible for, based on the [Dynamic Evidence](#_dynamic_evidence) that is presented by that instance of the [Generator Product](#_generator_product)

## Attestation

"The process of providing a digital signature for a set of measurements securely stored in hardware, and then having the requester validate the signature and the set of measurements." [NIST](https://csrc.nist.gov/glossary/term/attestation)

## C2PA Certificate Policy

A document that sets the requirements that SHALL be met by [Certification Authorities](#ca) (CAs) in the process of issuing digital certificates to [Subscriber](#_subscriber)s that implement C2PA Conforming Products that create [assets](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html#_asset) with [digital content](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html#_digital_content) and [C2PA manifests](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html#_c2pa_manifest), and the requirements that SHALL be met by the Subscribers in their use of the certificates.

## C2PA Claim

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## C2PA Claim Signing Certificate

An X.509 certificate issued by one of the [Certification Authorities](#ca) on the [C2PA Trust List](#_c2pa_trust_list) to an instance of the [Conforming Implementer](#_conforming_implementer)'s conforming [Generator Product](#_generator_product), and names the [Generator Product](#_generator_product) as the subject of the certificate.

## C2PA Conformance Program

A risk-based governance program intended to hold Applicants who want to demonstrate their conformance to its requirements and then differentiate themselves through C2PA recognition by satisfying program requirements being acknowledged as achieving that level of conformance. It consists of a set of processes, policies, and requirements governing the designation of [Applicant](#applicant) [Generator Product](#_generator_product)s or [Validator Product](#_validator_product)s as [Conforming Product](#_conforming_product)s, and the designation of [Certification Authorities](#ca) as adhering to the [C2PA Certificate Policy](#_c2pa_certificate_policy), as defined by the C2PA Technical Working Group Conformance Task Force.

Processes include:

- Evaluation of the C2PA-related functions of the [Applicant](#applicant) [Generator Product](#_generator_product) or [Validator Product](#_validator_product) as adhering to the normative requirements of the C2PA Content Credentials specification

- Evaluation of security attributes of the [???](#Target of Evaluation), which includes the [Applicant](#applicant) [Generator Product](#_generator_product) against the [Generator Product Security Requirements](#_generator_product_security_requirements), which results in assigning it a [Max Assurance Level](#_max_assurance_level)

- Evaluation of the processes, controls, and technical capabilities of [Certification Authorities](#ca) as required by the [C2PA Certificate Policy](#_c2pa_certificate_policy)

- Signing of the requisite legal agreements to become a member of the program.

## C2PA Conforming Products List

The canonical record of all [Conforming Product](#_conforming_product)s that have been deemed conformant according to the stipulations of the C2PA Conformance Program

## C2PA Content Credentials

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## C2PA Content Credentials Specification

A globally recognized standard for providing digital asset content provenance and authenticity. It is designed to enable global, opt-in, adoption of digital provenance techniques through the creation of a rich ecosystem of digital provenance enabled applications for a wide range of individuals and organizations while meeting appropriate security requirements.

## C2PA Governance Framework

A collection of governance documents which defines the C2PA trust ecosystem including roles, requirements and processes used by the C2PA [Governing Authority](#_governing_authority) to achieve greater assurance over the provenance and authenticity of digital asset content.

## C2PA Manifest

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## C2PA Trust List

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

In the context of the [C2PA Conformance Program](#_c2pa_conformance_program), a C2PA-managed list of X.509 certificate trust anchors (either root or subordinate [Certification Authorities](#ca)) that issue certificates to conforming [Generator Product](#_generator_product)s under the [C2PA Certificate Policy](#_c2pa_certificate_policy).

## C2PA TSA Trust List

A C2PA-managed list of X.509 certificate trust anchors (either root or subordinate [Certification Authorities](#ca)) that issue time-stamp signing certificates to Time-Stamping Authorities (TSA).

## Certification Authority

A trusted entity that issues, signs, and revokes digital certificates that bind public keys to subscriber identities. CAs are also known as PKI Certificate Authorities because they issue certificates based on public key infrastructure (PKI). These certificates contain credentials that confirm the possession of a private key by an entity, among other verified attributes. [Generator Product](#_generator_product)s sign C2PA Manifests using digital signing credentials issued by CAs.

An entity on the [C2PA Trust List](#_c2pa_trust_list) that is trusted by the [C2PA Conformance Program](#_c2pa_conformance_program) to issue X.509 [C2PA Claim Signing Certificate](#claimsigning-certs)s to instances of conforming [Generator Product](#_generator_product)s.

An organization that operates a Certification Authority may also operate a [Time-Stamping Authority](#_time_stamping_authority).

## Claim Generator

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## Conformance Criteria

A set of normative requirements that the C2PA expects a [Governed Party](#_governed_party) to demonstrate its conformance as part of the [C2PA Conformance Program](#_c2pa_conformance_program). This criteria consists of requirements derived from the [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) itself, and other ancillary requirements outside of the C2PA Specification including [Generator Product Security Requirements](#_generator_product_security_requirements) document and requirements in the [C2PA Certificate Policy](#_c2pa_certificate_policy).

## Conforming Implementer

An [Applicant](#applicant) who has become a member of the [C2PA Conformance Program](#_c2pa_conformance_program), and has at least one [Generator Product](#_generator_product) or [Validator Product](#_validator_product) in good standing on the [C2PA Conforming Products List](#_c2pa_conforming_products_list).

## Conforming Product

A [Generator Product](#_generator_product) or a [Validator Product](#_validator_product) that has been deemed conformant by the C2PA Conformance Program and added to the [C2PA Conforming Products List](#_c2pa_conforming_products_list) with a status of `conformant`. A [Generator Product](#_generator_product) that is deemed conformant is also assigned a [Max Assurance Level](#_max_assurance_level) that is recorded on the C2PA Conforming Products List.

Only instances of conforming [Generator Product](#_generator_product)s are eligible to receive [C2PA Claim Signing Certificate](#claimsigning-certs)s from a [Certification Authority](#ca) on the [C2PA Trust List](#_c2pa_trust_list).

## Digital Content

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## Dynamic Evidence

Attributes that a [Certification Authority](#ca) evaluates during automated enrollment for a [C2PA Claim Signing Certificate](#claimsigning-certs) by an instance of a [Generator Product](#_generator_product), usually relayed to the Certification Authority in the form of a verifiable hardware-backed artifact, such as a key or platform attestation report.

Dynamic Evidence may result in a particular instance of a Generator Product receiving a certificate of an [Assurance Level](#_assurance_level) that is lower than the [Max Assurance Level](#_max_assurance_level) that the [Generator Product](#_generator_product) is potentially eligible for.

## Generator Product

The set of software, hardware, and platform configurations created by an [Applicant](#applicant) that work together as a system to produce digital [Asset](#_asset)s with C2PA manifests. The asset’s active manifest contains assertions made by the Generator Product, and features a claim signed by a certificate where the Generator Product is the subject, about the provenance of the asset.

A Generator Product may integrate [Claim Generator](#_claim_generator) functions monolithically, or rely on a discrete [Claim Generator](#_claim_generator) service available either locally (e.g. on-device), or remotely (e.g. hosted in a cloud service). The monolithic or discrete [Claim Generator](#_claim_generator) service may be created by the [Applicant](#applicant) or by a different entity.

Because the Generator Product is always the [Signer](#_signer) in the [C2PA Conformance Program](#_c2pa_conformance_program), and is always the entity listed on the [C2PA Conforming Products List](#_c2pa_conforming_products_list), it is accountable for the conformance of the [Asset](#_asset)s with C2PA manifests that it generates with the normative requirements of the C2PA Content Credentials Specification, regardless of whether it integrates [Claim Generator](#_claim_generator) functions directly or relies on a discrete service.

## Generator Product Security Architecture Document

A filled-out version of the Generator Product Security Architecture Document Template, submitted by the [Applicant](#applicant) to the [C2PA Conformance Program](#_c2pa_conformance_program) as part of its application for inclusion on the [C2PA Conforming Products List](#_c2pa_conforming_products_list).

## Generator Product Security Requirements

Security-related implementation requirements for a [Generator Product](#_generator_product) to achieve a particular [Max Assurance Level](#_max_assurance_level), detailed in a document of the same name.

## Governed Party

An organization which desire to play a recognized role in the C2PA Conformance Program. It applies to the C2PA Conformance Program which requires them to sign a legal agreement and have their product reviewed prior to entering them on the C2PA Trust List or the Conforming Products List. Governed Parties of the C2PA ecosystem are [Certification Authorities](#ca) and [Applicants](#applicant) that elect to apply and and abide by the C2PA Conformance Program requirements.

## Governing Authority

The organization responsible for the trust of the ecosystem. It empowers an [Administering Authority](#_administering_authority) to manage the ecosystem and certifying entities to convey trust. The C2PA is the governing party of its conformance program driven by its Steering Committee.

## Hosting Environment

Server-side environment hosting a subset of [Generator Product](#_generator_product) or [Validator Product](#_validator_product) mechanisms and functionalities.

## Implementation Class - Backend

An implementation architecture for a [???](#Target of Evaluation) in which assets, assertions, claims, and claim signatures are generated in one or more [Hosting Environment](#_hosting_environment)s, including those hosted on premises or on commercial cloud service providers.

## Implementation Class - Distributed

An implementation architecture for a [???](#Target of Evaluation) which is composed of [Edge](#edge) and [Backend](#backend) subsystems, where the generation of assets, assertions, claims, and claim signatures is distributed between those subsystems.

## Implementation Class - Edge

An implementation architecture for a [???](#Target of Evaluation) in which assets, assertions, claims, and claim signatures are generated on an endpoint that operates at the edge of the network, such as:

- Smartphones and smartphone applications

- Laptop and desktop computers

- Fixed-function mirrorless cameras and surveillance cameras

- Portable audio recorders

## Manifest Consumer

The number and variety of consumers that rely upon the content provenance and authenticity of digital objects using content credentials are too numerous to capture in this document. In order for Manifest Consumers to consume Content Credentials supported by the C2PA, they MUST use C2PA-approved service providers. In addition, the C2PA Specification cites mandatory requirements for Manifest Consumers. While the C2PA mandates these requirements and discloses them in the Specification, it does not hold Manifest Consumers accountable to conform to these requirements within its governance framework.

## Max Assurance Level

A numeric designation, chosen at the discretion of the [C2PA Conformance Program](#_c2pa_conformance_program), based on evaluating the security functions, properties, and attributes of an [Applicant](#applicant) [Generator Product](#_generator_product) against the [Generator Product Security Requirements](#_generator_product_security_requirements) defined by the [C2PA Conformance Program](#_c2pa_conformance_program).

## Registration Authority

An entity authorized by the [Certification Authority](#ca) to collect, verify, and submit information provided by [Applicant](#applicant)s and/or [Subscriber](#_subscriber)s which is to be entered into public key certificates. The term RA refers to hardware, software, and individuals that collectively perform this function, including tasks such as validating platform attestations and presence of potential Subscriber implementations on the C2PA Conforming Products List. The RA operates under the CA’s authority and adheres to the guidelines set forth in the [C2PA Certificate Policy](#_c2pa_certificate_policy).

## Reliable Method of Communication

A method of communication, such as a postal/courier delivery address, telephone number, or email address, that was verified using a source other than the Applicant’s Representative.

## Relying Party

An entity that evaluates the trustworthiness of [Assertion](#_assertion)s made by a [Signer](#_signer) in a C2PA [Asset](#_asset), based on the [Signer](#_signer)'s identity and the [Assurance Level](#_assurance_level) encoded into the [C2PA Claim Signing Certificate](#claimsigning-certs).

## Rich Execution Environment

Refer to [NIST definition](https://csrc.nist.gov/glossary/term/rich_execution_environment). Abbreviated as REE.

## Root of Trust

Refer to [NIST definition](https://csrc.nist.gov/glossary/term/roots_of_trust). Abbreviated as RoT.

## Security Incident

"An occurrence that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information system or the information the system processes, stores, or transmits or that constitutes a violation or imminent threat of violation of security policies, security procedures, or acceptable use policies." [NIST](https://csrc.nist.gov/glossary/term/security_incident)

## Signer

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

In the C2PA Trust Model, the [Assertion](#_assertion)s enumerated in the `created_assertions` object of the [C2PA Claim](#_c2pa_claim) are attributed to the Signer.

In the context of the [C2PA Conformance Program](#_c2pa_conformance_program), an instance of the conforming [Generator Product](#_generator_product) listed on the [C2PA Conforming Products List](#_c2pa_conforming_products_list) is always the Signer.

## Static Evidence

Attributes of the [Generator Product](#_generator_product) [???](#Target of Evaluation) that are documented in the [Generator Product Security Requirements](#_generator_product_security_requirements) document which the [Administering Authority](#_administering_authority) evaluates during its assessment of the [Applicant](#applicant)'s [Generator Product](#_generator_product), in order to assign a [Max Assurance Level](#_max_assurance_level).

## Subscriber

An Applicant that has become a customer of one of the [Certification Authorities](#ca) on the [C2PA Trust List](#_c2pa_trust_list), and is eligible to receive [C2PA Claim Signing Certificate](#claimsigning-certs)s for use by instances of their conforming [Generator Product](#_generator_product).

## Generator Product Target of Evaluation (GP TOE)

The system which is evaluated by the [C2PA Conformance Program](#_c2pa_conformance_program) for its functional correctness and the security of its implementation. It consists of the sum total of the [Generator Product](#_generator_product) or [Validator Product](#_validator_product) created by an [Applicant](#applicant), **and** the subsystems that it relies on to produce or validate [Asset](#_asset)s with [C2PA Manifest](#_c2pa_manifest)s (this does not prohibit the GP TOE from opening [Asset](#_asset)s that were created outside its boundary). Those subsystems need not be created by the [Applicant](#applicant), but are necessary for the proper operation of the [Generator Product](#_generator_product) or the [Validator Product](#_validator_product).

The Target of Evaluation includes all components that are:

1.  involved in the generation of C2PA assertions referenced in the `created_assertions` claim field (including any data within them)

    1.  this naturally includes any components that were executed in order to make that assertion (e.g. a "c2pa.metadata" action assertion would require that the GP TOE include all components that produced that metadata)

2.  involved in the signing of the claim by the Generator Product claim signing key

3.  involved in the storage and usage of the claim signing key

The functional capabilities and security properties of those subsystems contribute to the overall security of the [Applicant](#applicant)'s product, and are thus are considered by the [C2PA Conformance Program](#_c2pa_conformance_program) when assigning an [Assurance Level](#_assurance_level) to a conforming [Generator Product](#_generator_product).

Targets of Evaluation can have [Edge](#edge), [Backend](#backend), or [Distributed](#distributed) implementation architectures.

## Time-Stamping Authority

A server that provides electronic certification and trust services by creating a hash of a document or digital information. The hash verifies the date and time of the document’s creation or last modification, and acts as an independent witness to prove that the document has not changed since it was signed. This is similar to how a notary acts for online documents. TSAs, that are part of Applicant Certification Authorities, that want to be recognized as issuing digital signing credentials approved by the C2PA, must satisfy the requirements of the program to be considered approved and designated as such within its governance records.

## Trusted Execution Environment

Refer to [NIST definition](https://csrc.nist.gov/glossary/term/trusted_execution_environment). Abbreviated as TEE.

## Validator

Refer to Section 2, "Glossary", of the C2PA Content Credentials specification.

## Validator Product

The set of software, hardware, and platform configurations created by an [Applicant](#applicant) that work together as a system to validate digital [Asset](#_asset)s with C2PA manifests.

A Validator Product may integrate [Validator](#_validator) functions monolithically, or rely on a discrete [Validator](#_validator) service available either locally (e.g. on-device), or remotely (e.g. hosted in a cloud service). The monolithic or discrete [Validator](#_validator) service may be created by the [Applicant](#applicant) or by a different entity.

Because the Validator Product is always the entity listed on the [C2PA Conforming Products List](#_c2pa_conforming_products_list), it is accountable for producing correct validation results in adherence with the normative requirements of the C2PA Content Credentials Specification, regardless of whether it integrates [Validator](#_validator) functions directly or relies on a discrete service.

# Overview

A structured approach to define security requirements for Generator Product consists of the following steps:

1.  Identification of threats relevant to C2PA technology that need to be addressed by the Generator Product Target of Evaluation (GP TOE).

2.  Translation of the threats into security objectives.

3.  Definition of security requirements that satisfy the security objectives up to different levels.

Meeting security requirements of a specific level grants a respective Max Assurance Value on the C2PA Conforming Product List.

<figure>
<img src="diagrams/GP_implementation_security_levels_flow_chart.png" alt="GP implementation security levels flow chart" />
<figcaption>Flow Chart for Determining Maximum Assurance Level of Generator Product on the Conforming Product List.</figcaption>
</figure>

# Threats

This section identifies threats that are relevant to C2PA technology that need to be addressed by the Generator Product Target of Evaluation (GP TOE).

## Threats identified within C2PA Security Considerations

As defined in the [C2PA Security Considerations](https://c2pa.org/specifications/specifications/2.4/security/Security_Considerations.html) document.

- 4.3.2.2. Threat: Spoofing signed C2PA Manifests via a stolen key.

- 4.3.2.3. Threat: Spoofing signed C2PA Manifests via misuse of a Claim Generator.

- 4.3.3.4. Threat: Exploitation of the hosting environment.

- 4.3.3.5. Threat: Interception and/or modification of traffic between two trusted sources.

- 4.3.2.12. Threat: Impersonating a conforming Generator Product instance during automated certificate enrollment.

- 4.3.2.13. Threat: Tampering with assets and/or assertions at generation.

# Security objectives

The following table translates the threats defined above into security objectives.

| Threat | Security Objective |
|----|----|
| T.1 - Impersonating a conforming Generator Product instance during automated certificate enrollment. | O.1 - Conforming GP instance provides proof of its eligibility during automated certificate enrollment. |
| T.2 - Spoofing signed C2PA Manifests via a stolen key. | O.2 - GP TOE protects the confidentiality of the signing key. |
| T.3 - Spoofing signed C2PA Manifests via misuse of Claim Generator. | O.3 - GP TOE protects the Claim Generator from exploits, misconfiguration and misuse. |
| T.4 - Tampering with asset and/or assertions at generation. | O.4 - GP TOE protects the asset and/or assertions from being tampered with at generation. |
| T.5 Interception and/or modification of traffic between two trusted sources. | O.5 GP TOE protects the traffic between subsystems and components of those subsystems from being intercepted and/or modified. |
| T.6 - Exploitation of the hosting environment. | O.6 - Hosting environment is protected from exploit, misconfiguration and misuse. |

# Definition of security requirements that satisfy the objectives up to different levels.

> [!NOTE]
> The requirements apply to all Implementation Classes (**Edge**, **Backend**, and **Distributed**) unless otherwise noted.  

> [!NOTE]
> Where applicable, evidence SHALL be provided in both forms static and dynamic, rather than choosing between the two evidence forms.

## O.1 - Conforming GP instance provides proof of its eligibility during automated certificate enrollment.

The following requirements are only applicable if conforming GP instances rely on automated certificate enrollment for initial certificate issuance or rotation.

### Level 1

#### Requirements

1.  GP TOE SHALL implement the secure authentication method required by the Certification Authority as part of an automated certificate enrollment process, which may rely on one of the following:

    - Shared secret/passphrase

    - Client certificate

    - Username/password

    - Challenge-response

    - Symmetric key MAC

2.  For **Edge** Implementation Class, the GP TOE binary/binaries SHALL NOT include authentication secrets

#### Static Evidence

1.  Applicant SHALL include details of the GP TOE’s automated certificate enrollment process, including its design for managing authentication secrets and the triggers for enrollment / renewal, in the GP Security Architecture Document. Applicant SHALL include details of their enrollment authentication method, either in their application, or, where those details are not available at the time of application, in a separate update to the Conformance Program within 90 days of the conformance being granted.

#### Dynamic Evidence

1.  The conforming GP instance SHALL authenticate with the CA using its secure credentials during automated certificate enrollment.

### Level 2

#### Requirements

In addition to the requirements defined for Level 1, Level 2 requires the following:

1.  GP TOE SHALL be capable of producing or deriving verifiable artifacts backed by a hardware [Root of Trust](#_root_of_trust), such as attestations or hardware-derived credentials, from its underlying platform, confirming the GP binary/binaries via package names, hashes, code signing certificates, other digital certificates, or a combination of the above.

A non-exhaustive list of examples of integrity attestation methods is available in [Integrity attestation methods](#integrity-attestation-methods)

#### Static Evidence

1.  Applicant SHALL include details of the GP TOE method for producing or deriving verifiable, hardware-backed artifacts confirming the identity of the GP binary/binaries in the GP Security Architecture Document.

#### Dynamic Evidence

1.  The conforming GP instances SHALL present the verifiable, hardware-backed artifacts for evaluation by the CA during automated certificate enrollment.

## O.2 - GP TOE protects the confidentiality of the signing key.

### Level 1

#### Requirements

1.  Where persistent storage is required, the GP TOE SHALL store the claim signing key in encrypted form, using industry best practices for encryption algorithms and key lengths<sup>1</sup>. The GP TOE SHALL SHALL keep the claim signing key encrypted when present in volatile memory, except when the key is being prepared for use in signing claims AND the handling of the decrypted key is done by either:

    1.  the Generator Product or Claim Generator itself, OR,

    2.  a discrete, dedicated key management component, function or service with an unrelated attack surface (e.g., Linux kernel keyring, macOS/iOS keychain, Android Keystore, systemd’s credential feature, HashiCorp Vault, AWS Secrets Manager or equivalents)

2.  GP TOE SHALL control access to the signing key in decrypted form, following the principle of [least privilege](https://csrc.nist.gov/glossary/term/least_privilege). Access SHALL be restricted to actors that have appropriate permissions, and those time-bound permissions are only granted to actors who have a justifiable requirement to access the key at that time.

3.  GP TOE SHALL be capable of rotating the claim signing key.

Additional requirements for **Distributed** and **Backend** Implementation Classes:

1.  The usage of the **Edge** subsystem authentication key (API Key) SHALL only be for the purposes of limiting access to the **Backend** subsystem.

2.  **Edge** and **Backend** subsystems SHALL be mutually authenticated; the role(s) of each subsystem across all communication channels SHALL be appropriate role(s), and SHALL be authenticated by the other.

3.  For **Distributed** Implementation Class, the remote claim signing **Backend** subsystem of the GP TOE SHALL securely authenticate the calling client, positively confirming that the calling client is a valid instance of the **Edge** subsystem of the GP TOE, before signing a claim with the claim signing key.

Authentication methods may include: shared secret/passphrase; client certificate; username/password; challenge-response; symmetric key MAC.

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document

    1.  Details of the claim signing key access controls (including encryption) in place that are designed to prevent unauthorized access

    2.  Details of the key rotation process

    3.  If ephemeral handling or storage of the plaintext claim signing key is implemented, a description of the controls and measures taken to minimize exposure and protect the key during such periods

        1.  Where such handling or storage is done by non-GP code, details of the vulnerability monitoring and upgrade process for such code shall be included

    4.  For **Distributed** and **Backend** Implementation Classes, documentation of the method for mutual authentication and role validation between the subsystems.

#### Dynamic Evidence

No stipulation.

### Level 2

#### Requirements

In addition to the requirements defined for Level 1, Level 2 requires the following:

1.  The GP TOE SHALL generate, store, and use the claim signing key within an environment with a higher privilege level than the privilege level of the Claim Generator execution environment, for example, a local platform keystore service or a hosted Key Management Service (KMS). The key management environment SHALL be one that has the following properties:

    1.  The key management environment restricts access to and usage of the key to authenticated callers

    2.  The key management environment sequesters the private key material such that the Claim Generator never has access to raw private key material in its memory space

    3.  The key management environment uses hardware-derived wrapping key(s) to store the claim signing key, and

    4.  One of the following:

        1.  The key management environment is capable of producing or deriving a verifiable artifact backed by a hardware Root of Trust (e.g. through attestation) confirming its possession of the claim signing private key, or

        2.  An accredited, independent 3rd party auditor certifies that the claim signing key is stored in such an environment

A non-exhaustive list of examples of key management environments is available in [Key management environments](#key-management-environments)

A non-exhaustive list of examples of accepted certification schemes are listed in [Accepted certification schemes](#accepted-certification-schemes)

Additional requirements for **Distributed** and **Backend** Implementation Classes:

1.  The subsystems (**Edge** and **Backend**) SHALL be capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust, such as attestations or hardware-derived credentials, from their underlying platforms

2.  The subsystems SHALL be capable of decoding and validating the hardware-backed artifacts produced by their counterpart subsystem

3.  The chosen method to produce or derive hardware-backed artifacts SHALL be one that allows the authentication of the counterpart subsystem via package names, hashes, code signing certificates, other digital certificates, or a combination of the above.

4.  Before a calling client requests the signing of a claim, the **Backend** subsystem SHALL request then validate the verifiable, artifact backed by a hardware Root of Trust, resulting in a validated verdict.

5.  If the the validated verdict does not positively confirm the calling client as a valid instance of the **Edge** subsystem, the **Backend** subsystem SHALL NOT sign the claim.

A non-exhaustive list of examples of integrity attestation methods is available in [Integrity attestation methods](#integrity-attestation-methods)

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document:

    1.  Details of the key management environment that the GP TOE uses, and its security properties. This may include commonly-accepted security certifications for the key management environment, and if applicable, certification by an accredited, independent 3rd party auditor certifying that the claim signing key is stored in such an environment.

    2.  Details of the key rotation process

    3.  If the Implementation Class is **Distributed**, or **Backend** details of the method for producing or deriving verifiable artifacts backed by a hardware Root of Trust by the subsystems.

#### Dynamic Evidence

1.  The conforming GP instance SHALL present a verifiable artifact backed by a hardware Root of Trust confirming its possession of the claim signing private key for evaluation by the CA during automated certificate enrollment.

## O.3 - GP TOE protects the Claim Generator from exploits, misconfiguration and misuse.

### Level 1

#### Requirements

1.  Applicant SHALL ensure a Software Composition Analysis (SCA) or Software Bill of Materials (SBOM) analysis is performed to detect vulnerabilities from the NIST National Vulnerability Database (NVD, <https://nvd.nist.gov/>) in the Claim Generator.

2.  Applicant SHALL ensure that applicable fixes or other mitigations are applied to any Claim Generator security vulnerabilities detected with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater within 90 days of detection.

Examples of such tools are listed in [SCA and SBOM dependency vulnerability scanning tools](#vulnerable-dependencies-tools) Examples of industry adopted vulnerability reporting formats are listed in [SCA and SBOM vulnerability reporting formats](#vulnerable-reporting-formats)

#### Static Evidence

1.  Applicant SHALL document the following in the GP Security Architecture Document:

    1.  The SCA/SBOM dependency vulnerability scanning tools used during the Claim Generator build or integration process.

    2.  The process by which the build and deployment pipeline prevents the release, more than a 90 days after detection, of the Claim Generator with known `CRITICAL` or `HIGH` severity vulnerabilities.

#### Dynamic Evidence

No stipulation.

### Level 2

#### Requirements

In addition to Level 1 requirements, Level 2 requires the following:

1.  The Applicant SHALL ensure that the Claim Generator and its execution environment enable [basic exploit countermeasures](#basic-exploit-countermeasures).

2.  The Applicant SHALL ensure [static analysis](#static-analysis-tools) of the Claim Generator and the platform/environment that the Claim Generator is built on.

3.  The Applicant SHALL ensure that the Claim Generator is built on a platform/environment where access control and image authentication for the Claim Generator binaries and the platform/environment are enforced by (if available) an environment with a privilege level higher than the privilege level of the platform/environment.

4.  The Applicant SHALL implement at least one of the following methods for ensuring the recency of security patches in the Claim Generator:

    1.  The Applicant SHALL ensure that the Claim Generator is capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust from its underlying platform, that provide evidence of how recently security patches were applied to this instance of the Claim Generator; or

    2.  The Applicant SHALL ensure that the Claim Generator is capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust from its underlying platform, which attest to the revision of the instance of the Claim Generator (e.g. version identifier, branch identifier, or commit identifier). If Applicant chooses this method, then Applicant SHALL design and execute a process by which Applicant SHALL:

        1.  Alert the CA of the minimum revision of the Claim Generator integrated with its GP that is eligible to enroll for certificates.

        2.  Alert the CA of which revisions of the Claim Generator integrated with its GP have applicable security vulnerabilities with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater and therefore make the integrating GP instance ineligible to enroll for certificates past 90 days after detection.

The following applies to Claim Generators that rely on external (from outside of the GP TOE) inputs:

1.  The Applicant SHALL ensure that, for the purposes of assertion generation, the Claim Generator enforces access control and validates external inputs before relying on their accuracy or integrity

2.  The Applicant SHALL ensure that the Claim Generator checks any external inputs for malicious data that could exploit vulnerabilities in the Claim Generator or its execution environment, and sanitises or rejects any such malicious data

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document:

    1.  Documentation of Claim Generator build scripts and build flags confirming enablement of countermeasures

    2.  Countermeasures functional test report.

    3.  Static analysis tools used

    4.  If applicable, access control methods

    5.  If applicable, binary image authentication methods

    6.  If applicable, external input validation methods

    7.  If applicable, access control lists for external input ingress points

    8.  Details of the method that the Applicant has chosen to provide information about the recency of security patches for the Claim Generator integrated with the instance of the GP through verifiable artifacts backed by a hardware Root of Trust.

    9.  Details of the validation methods for accuracy and integrity of any external inputs to the Claim Generator

    10. Details of any malicious data detection and sanitization methods for external inputs to the Claim Generator

#### Dynamic Evidence

1.  The conforming GP instance SHALL present verifiable artifacts backed by a hardware Root of Trust for evaluation by the CA during automated certificate enrollment confirming (depending on which method the Applicant has chosen):

    1.  The recency of application of applicable security patches of the Claim Generator integrated with the instance of the GP, is no less than the latest patch or version required to fix or otherwise mitigate any vulnerabilities with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater; or

    2.  The revision of the Claim Generator (e.g. a version identifier, a branch identifier, or a commit identifier) integrated with the instance of the GP, which the CA can compare against a list of allowed revisions

## O.4 - GP TOE protects the asset and assertions from being tampered with at generation.

### Level 1

Below requirements apply to all software in GP TOE that processes/modifies the [Digital Content](#_digital_content) and/or assertions:

#### Requirements

1.  Applicant SHALL ensure a Software Composition Analysis (SCA) or Software Bill of Materials (SBOM) analysis is performed to detect vulnerabilities from the NIST National Vulnerability Database (NVD, <https://nvd.nist.gov/>) in all such software.

2.  Applicant SHALL ensure that applicable fixes or mitigations are applied to any Claim Generator security vulnerabilities detected with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater within 90 days of detection.

Examples of such tools are listed in [SCA and SBOM dependency vulnerability scanning tools](#vulnerable-dependencies-tools) Examples of industry adopted vulnerability reporting formats are listed in [SCA and SBOM vulnerability reporting formats](#vulnerable-reporting-formats)

### Level 2

Below requirements apply to all software in GP TOE that processes/modifies the [Digital Content](#_digital_content) and/or assertions:

#### Requirements

1.  All such software SHALL enable [basic exploit countermeasures](#basic-exploit-countermeasures).

2.  The Applicant SHALL ensure [static analysis](#static-analysis-tools) on all such software.

3.  Authentication of binary images of all such software SHALL be enforced by (if available) an environment with a privilege level higher than the privilege level of such software <sup>8</sup>.

4.  The Applicant SHALL ensure that the GP TOE SHALL is capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust, such as attestations or hardware-derived credentials, confirming that all such software has been authenticated

5.  The Applicant SHALL implement at least one of the following methods for ensuring the recency of security patches in the GP TOE:

    1.  The Applicant SHALL ensure that the GP TOE is capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust from its underlying platform, that provide evidence of how recently security patches were applied to all such software in the GP TOE.

    2.  The Applicant SHALL ensure that the GP TOE is capable of producing or deriving verifiable artifacts backed by a hardware Root of Trust from its underlying platform, which attest to the revision(s) of the GP TOE software (e.g. version identifier, branch identifier, or commit identifier). If Applicant chooses this method, then Applicant SHALL design and execute a process by which Applicant SHALL:

        1.  Alert the CA of the minimum revision of the GP TOE software is eligible to enroll for certificates.

        2.  Alert the CA of which revisions of the GP TOE software have applicable security vulnerabilities with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater, and therefore make the integrating GP instance ineligible to enroll for certificates past 90 days after detection.

6.  GP TOE SHALL provide the following protection for the asset and all assertions, while these are processed by such software by ensuring usage of access control mechanisms enforced by (if available) an environment with privilege level higher than the privilege of such software:

    1.  isolation of the source processes and/or threads

    2.  protection of the inter-process communication channels

    3.  protection of memory.

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document:

    1.  If applicable, description of image authentication methods of source and its execution environment for all sources of assets and assertions implemented in software.

    2.  Details of the method that the Applicant has chosen to provide information about the recency of security patches for the GP TOE through verifiable artifacts backed by a hardware Root of Trust.

    3.  Documentation of build scripts and build flags confirming enablement of countermeasures

    4.  Countermeasures functional test report

    5.  Static analysis tools used

    6.  If applicable, binary image authentication methods

    7.  Confirmation of support of isolation of the source processes and/or threads and protection of the inter-process communication channels by the kernel or operating system in use. This can be achieved by demonstrating that:

        1.  the processes and/or threads run under a unique operating system UID or user account from other processes on the device,

        2.  forms of inter-process communication (Android broadcasters and receivers, IPC channels, etc.) are limited to only those necessary for the application to function and that ACLs limit the processes and/or threads that connect to them.

#### Dynamic Evidence

1.  The conforming GP instance SHALL present verifiable artifacts backed by a hardware Root of Trust for evaluation by the CA during automated certificate enrollment confirming the following properties of all software in the GP TOE that processes/modifies the [Digital Content](#_digital_content) and/or assertions:

    1.  That all such software has been authenticated

    2.  Depending on the method for confirming recency of security patches that the Applicant has chosen:

        1.  The recency of application of security patches of the GP TOE software, is no less than the latest patch or version required to fix or otherwise mitigate any applicable vulnerabilities with a CRITICAL or HIGH severity ratings in the NIST Common Vulnerability Scoring System (CVSS, <https://nvd.nist.gov/vuln-metrics/cvss>) version 3 or greater; or

        2.  The revision(s) of the GP TOE software (e.g. a version identifier, a branch identifier, or a commit identifier), which the CA can compare against a list of allowed revisions

## O.5 - GP TOE protects the traffic between subsystems and components of those subsystems from being intercepted and/or modified.

### Level 1

For **Distributed** and **Backend** Implementation Classes:

#### Requirements

1.  Network communication channels between the subsystems (**Edge** and/or **Backend**) SHALL be protected using TLS v1.3 (or higher) or an equivalent protocol.

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document:

    1.  Documentation of the TLS versions or equivalent protocols in use and the supported cryptographic protocols for network communication between the subsystems (**Edge** and/or **Backend**).

#### Dynamic Evidence

No stipulation

### Level 2

#### Requirements

GP TOE SHALL provide the following kernel/operating system level protection for asset and all assertions transmitted within subsystems (**Edge** and/or **Backend**):

1.  isolation of the source processes and/or threads related to asset and assertion generation

2.  protection of the inter-process communication channels used to transmit assets or assertions between processes and/or threads

#### Static Evidence

1.  Applicant SHALL include the following in the GP Security Architecture Document:

    1.  Confirmation of support of isolation of the source processes and/or threads and protection of the inter-process communication channels by the kernel or operating system in use. This can be achieved by demonstrating that:

        1.  the processes and/or threads run under a unique operating system UID or user account from other processes on the device,

        2.  forms of inter-process communication (Android broadcasters and receivers, IPC channels, etc.) are limited to only those necessary for the application to function and that ACLs limit the processes and/or threads that connect to them.

#### Dynamic Evidence

No stipulation.

## O.6 - Hosting environment is protected from exploit, misconfiguration and misuse.

This security objective apply only to the **Distributed** and **Backend** Implementation classes.

### Level 1

#### Requirements

1.  Resources used for asset and/or assertion generation SHALL protected with an Identity and Access Management (IAM) system that implements Role-Based Access Control (RBAC) or a similar access control model.

2.  The Applicant SHALL ensure vulnerability scanning and/or security review is performed for software dependencies and API surfaces, and ensure identified vulnerabilities SHALL be patched, fixed, or mitigated in a timely manner <sup>9</sup>. The process SHALL, at least cover vulnerabilities applicable to the implementation, if any, from: ..Open Worldwide Application Security Project (OWASP) (<https://owasp.org/www-project-top-ten/>) top 10 web application vulnerabilities.

3.  [Basic exploit countermeasures](#basic-exploit-countermeasures) SHALL be applied. Updates and security patches for the operating system and relevant software SHALL be applied in a timely manner <sup>9</sup>.

#### Static Evidence

Applicant SHALL include the following in the GP Security Architecture Document:

1.  Description of IAM system employed <sup>10</sup> and coverage of security boundaries (e.g., virtual machines, cloud storage repositories) related to asset and claim generation.

2.  Description of access policies for human and non-human principal (e.g., service accounts or production identities)

3.  Description of IAM policies showing access for main cloud resources (e.g., VM instances, cloud storage buckets).

4.  Description of the process used by the Applicant to ensure vulnerability scanning and/or security review is performed for software dependencies and API surfaces.

5.  Description of the process used by the Applicant to ensure vulnerabilities are fixed or mitigated in a timely manner <sup>9</sup>.

#### Dynamic Evidence

No stipulation.

### Level 2

#### Requirements

In addition to the requirements defined for Level 1, Level 2 requires the following:

1.  Audit logging SHALL be enabled and monitored for security-relevant events (e.g., human access).

2.  A Host-based Intrusion Detection System (HIDS) OR a distributed system that provides similar functionality SHALL be deployed for monitoring system integrity and detecting suspicious activities.

3.  Network segmentation SHALL be implemented to isolate the hosting environment.

#### Static Evidence

Applicant SHALL include the following in the GP Security Architecture Document:

1.  Description of audit logging system, event logging policies, and monitoring rules

2.  Description of HIDS software or similar systems used

3.  Description of the network architecture and configuration, including a description of network isolation boundaries

4.  Report showing audit logging is enabled

5.  Report showing active operation of a HIDS or similar systems

6.  Report showing active network isolation operation covering the application’s network infrastructure

#### Dynamic Evidence

No stipulation.

# Footnotes

<sup>1</sup> Catalogues of allowed cryptographic algorithms: NIST Cryptographic Standards and Guidelines (<https://csrc.nist.gov/Projects/Cryptographic-Standards-and-Guidelines>); ENISA ECCG Agreed Cryptographic Mechanisms (<https://certification.enisa.europa.eu/publications/eucc-guidelines-cryptography_en>).  
<sup>2</sup> Examples include key management within Trusted Execution Environment running at privilege level higher that Non-Secure World within ARM architecture.  
<sup>3</sup> Examples include AWS Key Management Service, AWS CloudHSM, GCP Cloud KMS, Azure Key Vault, HashiCorp Vault  
<sup>4</sup> See <https://www.iso.org/obp/ui/en/#iso:std:iso-iec:tr:20004:ed-2:v1:en> for more information on AVA_VAN levels  
<sup>5</sup> ASLR, stack canaries, guard pages, DEP, Safe Heap, NX.  
<sup>6</sup> Acceptable static analysis tools: …​ <sup>7</sup> CFI, PAC, MTE and sanitizers.  
<sup>8</sup> Examples include: a) authentication of a source application by Android Bootloader using Android Verified Boot Process; b) authentication of source trusted virtual machine by a hypervisor.  
<sup>9</sup> Timely manner means 30/90/180 days to fix high, moderate, and low severity vulnerabilities as determined by the Common Vulnerability Scoring System (CVSS) (<https://www.first.org/cvss/>)  
<sup>10</sup> Examples include: AWS - IAM (<https://aws.amazon.com/iam/>); Azure - Azure RBAC (<https://learn.microsoft.com/en-us/azure/role-based-access-control/overview>); GCP - Identity and Access Management (IAM) (<https://cloud.google.com/security/products/iam>)  

# Example Implementation Architectures

This appendix contains various examples of different implementation architectures for [Generator Product](#_generator_product)s and their Target of Evaluation. The Target of Evaluation is considered in its totality when assigning the Generator Product a [Max Assurance Level](#_max_assurance_level).

# Backend Class: Video Generation Service

<figure>
<img src="diagrams/toe-backend-video_gen_service.png" alt="toe backend video gen service" />
</figure>

# Backend Class: A "Minimal Generator Product" Service, Signing The Output Of An Open-source Application

<figure>
<img src="diagrams/toe-minimal-backend_claimsigning.png" alt="toe minimal backend claimsigning" />
</figure>

# Distributed Class: Edge REE App with Backend Claim Signing

<figure>
<img src="diagrams/toe-distributed-edge_app-backend_claimsigning.png" alt="toe distributed edge app backend claimsigning" />
</figure>

# Edge Class: Monolithic REE App

<figure>
<img src="diagrams/toe-edge-monolithic_ree_app.png" alt="toe edge monolithic ree app" />
</figure>

# Edge Class: REE App relying on 3p Discrete REE Claim Generator

<figure>
<img src="diagrams/toe-edge-ree_app-multi_tenant_ree-claimgen.png" alt="toe edge ree app multi tenant ree claimgen" />
</figure>

# Edge Class: REE App relying on 3p Discrete TEE Claim Generator

<figure>
<img src="diagrams/toe-edge-ree_app-multi_tenant_tee_claimgen.png" alt="toe edge ree app multi tenant tee claimgen" />
</figure>

# Edge Class: REE+TEE App relying on 3p Discrete TEE Claim Generator

<figure>
<img src="diagrams/toe-edge-ree_app-tee_app-multi_tenant_tee_claimgen.png" alt="toe edge ree app tee app multi tenant tee claimgen" />
</figure>

# Non-normative guidance

This non-normative guidance is designed to help Applicants understand the types of security technologies that may help them achieve the desired Assurance Level for their implementation. The examples provided here do not represent formal endorsements by the C2PA, its Steering Committee, its Technical Working Group, or the TWG’s Conformance Task Force of any specific commercial offering.

# AVA_VAN Levels

See <https://www.iso.org/obp/ui/en/#iso:std:iso-iec:tr:20004:ed-2:v1:en> for more information on AVA_VAN levels.

# Key management environments

Examples of key management environments include:

- For **Edge** Implementation Class:

  - [Apple Secure Enclave](https://developer.apple.com/documentation/security/protecting-keys-with-the-secure-enclave)

  - [Android Keystore](https://developer.android.com/privacy-and-security/keystore) (both StrongBox-based implementations, protected by a dedicated secure processor, and TEE-based implementations)

  - [Microsoft Platform Crypto Provider](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/how-windows-uses-the-tpm#platform-crypto-provider)

  - Other keystore services that operate within a Trusted Execution Environment running at privilege level higher that Non-Secure World within ARM architecture.

- For **Backend** and **Distributed** Implementation Classes:

  - [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

  - [Microsoft Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/)

  - [Google Cloud Key Management Service](https://cloud.google.com/kms/docs)

  - [HashiCorp Vault](https://www.vaultproject.io/)

# Integrity attestation methods

Examples of integrity attestation methods include:

- For **Edge** and **Distributed** Implementation Classes:

  - [Apple App Attest](https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity)

  - [Google Play Integrity API](https://developer.android.com/google/play/integrity)

  - [Android Key Attestation](https://source.android.com/docs/security/features/keystore/attestation)

- For **Backend** and **Distributed** Implementation Classes

  - [AWS Nitro Enclave Attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html)

  - [Microsoft Azure Attestation](https://learn.microsoft.com/en-us/azure/attestation/overview)

  - [Google Cloud Attestation](https://cloud.google.com/confidential-computing/docs/attestation)

# Accepted certification schemes

## SOC2 Type 2

To achieve SOC 2 compliance, organizations must demonstrate that they have robust controls in place for managing private keys, including: \* Secure Storage: Protecting private keys from unauthorized access and ensuring they are stored securely. \* Access Control: Limiting access to private keys based on the principle of least privilege. \* Key Rotation: Regularly rotating private keys to mitigate the risk of compromise. \* Encryption: Using strong encryption algorithms to protect data at rest and in transit.

# SCA and SBOM dependency vulnerability scanning tools

Examples of tools that enable identifying vulnerabilities in dependencies include:

- Open-source:

  - [OSV-Scanner](https://github.com/google/osv-scanner)

  - [Grype](https://github.com/anchore/grype)

  - [Dependency-Track](https://dependencytrack.org/)

- Commercial:

  - [GitHub security and analysis for repositories](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository)

  - [Tenable Web App Scanning](https://www.tenable.com/products/web-app-scanning)

  - [Acunetix](https://www.acunetix.com/)

  - [Invicti, formerly Netsparker](https://www.invicti.com/)

  - [Qualys SCA](https://www.qualys.com/apps/security-configuration-assessment/)

  - [Checkmarx One](https://checkmarx.com/product/application-security-platform/)

  - [NowSecure](https://www.nowsecure.com/)

  - [Google Cloud Artifact Analysis](https://cloud.google.com/artifact-analysis/docs/artifact-analysis)

# SCA and SBOM vulnerability reporting formats

Examples of industry standard formats for publishing vulnerabilities include: \* Industry-standard **[Common Vulnerability Reporting Framework](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html)** [Common Vulnerabilities and Exposures (CVE) JSON Format](https://www.cve.org/Resources/Support/Documentation) **[Security Advisory Markup Language (SAF/OSV)](https://ossf.github.io/osv-schema/)** [CycloneDX Vulnerability Format](https://cyclonedx.org/docs/1.5/json/#components_vulnerabilities) **[Vulnerability Exploitability eXchange (VEX)](https://www.cisa.gov/resources-tools/resources/vulnerability-exploitability-exchange-vex)** [SPDX Security Profile](https://spdx.dev/specifications/) \*\* [NVD JSON Feeds](https://nvd.nist.gov/vuln/data-feeds#JSON_FEED)

# Basic exploit countermeasures

Examples of basic exploit countermeasures include:

- ASLR

- Stack canaries

- Guard pages

- DEP

- Safe Heap

- NX

# Static analysis tools

Examples of static analysis tools include:

- Klocwork

- Coverity

- IntelliJ

- Fortify

- Snyk Code

- SonarQube

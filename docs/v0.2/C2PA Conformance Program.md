---
author: C2PA Technical Working Group Conformance Task Force
date: 2026-07-31
title: C2PA Conformance Program
version: v0.2
---

# Introduction

With the increasing velocity of digital content and the increasing availability of powerful creation and editing techniques, establishing the provenance of media is critical to ensure transparency, understanding, and ultimately, trust.

To address this issue at scale for publishers, creators and consumers, the Coalition for Content Provenance and Authenticity (C2PA) has developed a technical specification ([C2PA Content Credentials Specification](#_c2pa_content_credentials_specification)) for providing content provenance and authenticity. It is designed to enable global, opt-in, adoption of digital provenance techniques through the creation of a rich ecosystem of digital provenance enabled applications for a wide range of individuals and organizations while meeting appropriate security requirements.

The Specification has seen wide-scale acceptance but is limited without a robust governance framework and conformance program to provide required transparency for relying parties and accountability for governed parties which need to demonstrate recognized conformance of Specification requirements. This is the intent of the [C2PA Governance Framework](#_c2pa_governance_framework) and [C2PA Conformance Program](#_c2pa_conformance_program).

# Glossary

The C2PA has established the following glossary to define the following terms and constructs germane to the C2PA ecosystem. Other terms not specified in this glossary may be found in the Trust Over IP Glossary located at (<https://trustoverip.github.io/toip/glossary>).

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

# Purpose of the Program

The goal of the [C2PA Conformance Program](#_c2pa_conformance_program) is to address the challenge of trusting media in a context of rapidly evolving technology and widespread adoption of powerful creation and editing techniques. The [C2PA Conformance Program](#_c2pa_conformance_program) is designed to enable global, opt-in, adoption of digital provenance techniques through the creation of a rich ecosystem of digital provenance enabled applications for a wide range of individuals, organizations and devices, while meeting appropriate security and privacy requirements, as well as human rights considerations.

This goal cannot be achieved solely by the [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification); it needs a coordinated and regulated effort by all participants that play a role in conforming to the Specification to be accountable. Furthermore, it requires an unbiased and open governance process that enables Applicants to clearly understand the process of conformance and demonstrate that it meets the program’s requirements for the benefit of a digital society.

The [C2PA Conformance Program](#_c2pa_conformance_program) rewards Applicant [Generator Product](#_generator_product)s, [Validator Product](#_validator_product)s and Certification authorities which successfully demonstrate conformance to program requirements by placing machine-readable access information for that Applicant in controlled and accessible lists so [Manifest Consumer](#_manifest_consumer)s have confidence that they are working only with approved C2PA Conformance Program participants that have achieved that status. The administration of these trust lists is performed by the C2PA [Administering Authority](#_administering_authority) under the governance of its [Governing Authority](#_governing_authority).

# Program Scope

The scope of the C2PA Conformance Program includes all the tangible components: participants, processes and artifacts.

## Program Participants

- Generator Product Company: An [Applicant](#applicant) that has created a [Generator Product](#_generator_product).

- Validator Product Company: An [Applicant](#applicant) that has created a [Validator Product](#_validator_product).

- [Certification Authority](#ca)

- [Time-Stamping Authority](#_time_stamping_authority)

- [Manifest Consumer](#_manifest_consumer)

- [Relying Party](#_relying_party)

# Assurance Levels

The C2PA has established the notion of a [Max Assurance Level](#_max_assurance_level) based on the security attributes of the implementation architecture of a [Generator Product](#_generator_product), and the notion of an [Assurance Level](#_assurance_level) which a particular instance of the [Generator Product](#_generator_product) is eligible for based on the dynamic evidence it is able to present at the time of certificate enrollment with a [Certification Authority](#ca).

The implementation security requirements associated with each [Assurance Level](#_assurance_level) is detailed in the C2PA Generator Product Security Requirements document.

Two Assurance Levels are currently in operation, Assurance Level 1 and Assurance Level 2. The Assurance Level associated with an instance of a [Generator Product](#_generator_product) is encoded as the value of a custom X.509v3 certificate extension (as defined in the C2PA’s `OID.txt` MIB definition file) in the [C2PA Claim Signing Certificate](#claimsigning-certs) that the instance of the Generator Product uses to sign [C2PA Claim](#_c2pa_claim)s.

Relying Parties are advised to review and understand the implications of receiving [Asset](#_asset)s signed by [C2PA Claim Signing Certificate](#claimsigning-certs)s of a particular [Assurance Level](#_assurance_level).

# Conformance Criteria

## C2PA Content Credentials Specification Requirements

### C2PA Content Credentials Specification Process Requirements

The [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) provides prescriptive guidance on the generation and validation of manifests that are hard-bound to [Asset](#_asset)s. The minimum release level of the [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) for applicability of this version of the [C2PA Conformance Program](#_c2pa_conformance_program) is v2.2. The Specification includes normative requirements and non-normative recommendations. The C2PA Conformance Program has isolated the normative requirements (included in SHALL statements) and have attributed them to specific roles in the ecosystem where Applicants will eventually be held accountable against these role sets for C2PA recognition. The following role sets have been identified:

#### Generator Product Specific Requirements

The [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) includes over 300 normative requirements attributed to [Generator Product](#_generator_product)s which create C2PA manifests for consumers. The C2PA Conformance Program will eventually require Claim Generators to demonstrate complete conformance to these exacting requirements in order to receive its approval. Requirements for [Generator Product](#_generator_product)s include:

- Manifest Formatting

- Manifest Redaction

- Claim Signing

- Timestamp Insertion

- Cryptographic Hash Computation

- File-type Specific Handling Requirements

#### Validator Product Specification Requirements

The [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) includes over 150 normative requirements attributed to claims [Validator Product](#_validator_product)s which validate C2PA manifests for consumers. The C2PA Conformance Program will eventually require claims validators to demonstrate complete conformance to these exacting requirements in order to receive its approval. Requirements for [Validator Product](#_validator_product)s include:

- Conditions for a Fully Formed Manifest Sufficient for Validation

- Signature Validation

- Timestamp Validation

- Assertion Validation

- Cryptographic Hash Validation

- Validation Result Reporting

#### Certification Authority Specification Requirements

The [C2PA Conformance Program](#_c2pa_conformance_program) has enumerated the normative requirements from the [C2PA Content Credentials Specification](#_c2pa_content_credentials_specification) that are applicable to Certification Authorities in the [C2PA Certificate Policy](#_c2pa_certificate_policy).

## Generator Product Implementation Security Requirements

Not all implementations of the C2PA Specification are the same. While all [Generator Product](#_generator_product)s and [Validator Product](#_validator_product)s are required to abide by the normative requirements of the C2PA Specification, the C2PA [Governing Authority](#_governing_authority) has established additional requirements that mandate specific security attributes when an [Applicant](#applicant) is creating their implementation of a [Generator Product](#_generator_product).

An [Applicant](#applicant) must, at a minimum, meet the implementation security requirements associated with [Assurance Level](#_assurance_level) 1 in order for their Generator Product to be included on the [C2PA Conforming Products List](#_c2pa_conforming_products_list).

## Additional Conformance Requirements based on the C2PA Content Credentials Specification

One critical aspect of the C2PA Conformance Program is the contractual binding that Generator and Validator Product Applicants have to conform to the C2PA Content Credentials Specification (Spec) at the Spec version level they initially assert within the Program Intake Form, and is posted on our Conforming Products List (CPL). This document lists additional requirements of the C2PA Conformance Program, which are not requirements asserted in the Spec, that the program requires Applicants to be conformant with as part of the conformance acceptance process.

## Certificate Policy

The C2PA has created a Certificate Policy ("CP") which establishes the requirements governing the issuance of [C2PA Claim Signing Certificates](#claimsigning-certs) for use by implementers of the technical specifications developed by the [Coalition for Content Provenance and Authenticity](https://c2pa.org).

The policy sets the requirements that SHALL be met by a [Certification Authority](#ca) (CA) in the process of issuing [C2PA Claim Signing Certificates](#claimsigning-certs) to [Subscriber](#_subscriber)s that implement [Generator Product](#_generator_product)s, and the requirements that SHALL be met by the Subscribers in their use of the certificates. Instances of the Subscribers' [Generator Product](#_generator_product)s use the certificates to cryptographically sign a [C2PA Claim](#_c2pa_claim), to imbue an [Asset](#_asset) with [C2PA Content Credentials](#_c2pa_content_credentials).

[C2PA Claim Signing Certificates](#claimsigning-certs) under this policy SHALL only be issued to instances of [Generator Product](#_generator_product)s that have successfully passed the [C2PA Conformance Program](#_c2pa_conformance_program), as documented through the receipt of a signed Notice of Conformance from the C2PA Conformance Program Administrator at the time of conformance and their inclusion in the [C2PA Conforming Products List](#_c2pa_conforming_products_list) when Applicants direct the C2PA to post their records. Digital certificates issued under this CP indicate an [Assurance Level](#_assurance_level) that can be used by a [Relying Party](#_relying_party) as part of its evaluation of confidence in an [Asset](#_asset) that contains C2PA Content Credentials.

Certification Authorities that comply with this Certificate Policy and want to issue certificates under the C2PA Conformance Program MUST apply to the C2PA [Governing Authority](#_governing_authority) for inclusion on the [C2PA Trust List](#_c2pa_trust_list) . Furthermore, Only conformant [Certification Authority](#ca) may add Root and Intermediate [???](#Time-Stamping Authoritiy) certificates to the [C2PA TSA Trust List](#_c2pa_tsa_trust_list).

The legal agreement that CA applicants sign as part of the C2PA Conformance Program asserts that they meet CP requirements. Therefore, the Conformance Program, as part of its assessment of CA applicants, SHALL require CA applicants to:

- Show evidence that its Root and/or Intermediate cert(s) that it desires to be placed on the C2PA Trust List and TSA Trust List have been validated against certificate profiles located in the CP.

- Provide evidence of an independently witnessed key generation ceremony (with signed key generation script) for the certs that it desires to be placed on the C2PA Trust list and TSA Trust List. This can be waived if they can produce a WebTrust for CA report attesting that ceremonies and scripts are conformant to its requirements.

## Business Requirements

### Conformance Program Fee Schedule

There is no application fee for Certification Authorities, Generator Product companies, or Validator Product companies applying to the C2PA Conformance Program.

There is also no fee for adding applicant records to the CA Trust List or the Conforming Products List.

## Process Requirements for Applicants of the C2PA Conformance Program

This chart describes the process steps of the C2PA Conformance Program:

<figure>
<img src="diagrams/C2PA_Conformance_Program_Process_Steps.png" alt="C2PA Conformance Program Process Steps" />
</figure>

The following section describes the initial Applicant process for the C2PA Conformance Program from intake application to denoting recognition of an Applicant’s meeting program requirements through its application or service being added to its respective trust list.

### Expression of Interest Form

All Applicants (Certification Authorities, [Generator Product](#_generator_product)s and [Validator Product](#_validator_product)s) SHALL apply to the C2PA Conformance Program using this Expression of Interest Form (<https://docs.google.com/forms/d/e/1FAIpQLScERZH5rKfoeSu3y6gGbkllkyeAhmF0G-kXS0eXpb2vR238Rg/viewform?usp=header>) This form describes the governed role of the Applicant which drives the legal agreement it needs to sign as part of the program. Therefore, it is important to complete the legal entries of the form based on the Applicant Company’s legal business registration. It also identifies one of more roles that the Applicant is applying for (Generator Product (GP), Validator Product (VP) and Certification Authority (CA)). Each role will generate a separate legal agreement process.

The C2PA will not accept applicants that only apply for Time-Stamping Authority service. The Program only accepts Time-Stamping Authorities if they also provide a Certification Authority service.

### Legal Agreement Execution

Prior to accepting Applicants into the C2PA Conformance Program, each Applicant SHALL sign a legal agreement with the C2PA committing to the C2PA Conformance Program requirements. The C2PA has established separate templates for its legal agreements depending on the role that the Applicant requests within the program ([Generator Product](#_generator_product), [Validator Product](#_validator_product) and [Certification Authority](#ca)). For example, if an Applicant is applying to the program as a Generator Product and a Validator Product, separate legal agreements MUST be signed for each role.

After receipt of the Expression of Interest Form, the Applicant will be directed to the Linux Foundation’s document signing service to execute the Agreement. The Certification Authority Agreement is countersigned by the Executive Director of the C2PA. Applicants can forward the Agreement to their Company’s signatory using the signing platform. Once the Agreement is signed, it will prompt the Program Administrator to send an email to the Applicant directing them to complete the C2PA Conformance Program Intake Form.

### Program Intake Form

Once the legal agreement is signed, the [Applicant](#applicant) is sent a link to an Intake Form which is used to build the conformant record on one of our public lists. This will vary depending on the role the [Applicant](#applicant) is seeking within the program. The Conformance Program needs separate intake forms to be completed for every applicant record on the Conforming Products List (CPL) and any new set of Certification Authority and/or Time Stamp Authority (TSAs) Root or Intermediary CA certificates it requests to be added to the respective CA Trust List (CA TL) or TSA Trust List (TSA TL).

The primary purpose of the Program Intake Form is to collect information about an Applicant’s product or service that can be used to populate their record on either the CPL, CA TL or TSA TL. The form asks for legal business information for the purposes of the public record an applicant wants to state, and clicking on the role (CA, GP/VP) on the Intake Form will generate separate questions for that role.

CAs use the Program Intake Form to submit CA TL record details and separate PEM-encoded certificates for each of the CAs to which their certificate(s) ladder up, separated by a blank line. The Conformance Program WILL NOT accept entries indicating test CAs.

CAs that also operate a TSA use the Program Intake Form to submit TSA TL record details and separate PEM-encoded certificates for each of the TSAs to which their certificate(s) ladder up, separated by a blank line. If a TSA and CA ladder up to the same root, applicants should record the same root certificates in both the CA and TSA sections so their record can be properly recorded in both the CA TL and the TSA TL. The Conformance Program WILL NOT accept entries indicating test TSAs.

The C2PA Conformance Program strongly recommends that Applicants perform interoperability testing for their Generator Product or Validator Product prior to submitting their Program Intake form. This recommendation is designed to give Applicants and the C2PA Conformance Program confidence that Applicants have implemented their C2PA Generator Product and/or Validator Product functions correctly in accordance with the C2PA Content Credentials specification. The Conformance Program invites pre-released products into the program.

The Conformance Program is administered by an independent Administrator who is free from conflicts of interest. The Administrator workspace is securely isolated from C2PA members in accordance with legal agreements. In addition, the Program Intake form includes a “Date of Earliest Public Disclosure” that will be used to prevent the Applicant’s record from appearing on our public CPL until that date.

Other fields on the Program Intake Form queries for details on the Generator Product or Validator Product such as the media types it supports. For details of these fields, please reference the Companion Guide for the C2PA Conforming Products List.

### Processing Program Intake Forms

After an Applicant completes the Program Intake Form, a notice is sent to the Conformance Program Administrator and a CPL record snippet is automatically generated in the Administrator workspace. The Administrator reviews the content on the Program Intake Form and may notify the Applicant if content is not conformant to the schema at the publicly posted Companion Guide for the C2PA Conforming Products List.

Once the Program Intake Form is properly formatted and accurately documents the Applicants assertions for their product or service, additional evidence is required below based on the type of applicant. Depending on the role requested and the level of implementation security assurance requested on the intake form, the C2PA will request additional evidence to demonstrate that the application is meeting Conformance Program requirements.

Once the legal agreement is signed, the [Applicant](#applicant) is sent a link to an Intake Form which is used to build the conformant record on one of our public lists. This will vary depending on the role the [Applicant](#applicant) is seeking within the program. That Intake Form has media type selections which applicants can select the most specific media type available. If the specific media type is not available, please select the most appropriate media based type available (e.g., `image/x-tiff-based` for proprietary raw images) that applicants can demonstrate to the conformance program with samples.

#### Architecture Document Required of Generator Product Applicants

[Applicant](#applicant)s that are applying to the Conformance Program for the purpose of including their [Generator Product](#_generator_product) on the [C2PA Conforming Products List](#_c2pa_conforming_products_list) are required to submit a Generator Product Security Architecture (GPSA) Document. Applicants MUST use the C2PA Generator Product Security Architecture Document template, provided in Markdown format in the Conformance Program documents repository, to document the Generator Product’s security architecture. Submitted GPSA documents MUST be in Markdown format, accompanied by any architecture diagrams, in JPEG or PNG formats, that the applicant deems necessary to demonstrate conformance with the C2PA Generator Product Security Requirements.

The Generator Product and its supporting infrastructure (defined as the Target of Evaluation (TOE) by the Conformance Program) can operate solely on edge devices, on back-end systems or a combination of the two. In order to evaluate an Applicant’s Generator Product against the Generator Product Security Requirements, Applicants MUST indicate its implementation type of its Generator Product (See Conformance Program Glossary for definition of terms). The key for Applicants to remember is the Target of Evaluation (TOE) boundaries start from the initial capture or upload of assets through to a signing operation and delivery or persistence of a signed asset of a signed asset.

The C2PA Conformance Program has created two sets of implementation security requirements that generator products can assert conformance. These levels of implementation security assurance are defined in the Generator Product Security Requirements. The Program Intake form queries an Applicant on the Max Assurance level they are seeking for their Generator Product. This level will be included on the Applicant’s CPL record and will prompt additional evidence in the Assessment phase of the process at a later step. Once Applicant’s Generator Product record is assessed and deemed conformant at Max Assurance level 2 on the CPL, the Applicant may request CA certificates from a conformant CA at both Assurance levels 1 and 2.

#### Generator Product Sample Evidence

Generator Product applicants must provide sample output media files of every asserted generate and validate media type in their Generator Product Program Intake Form, along with their associated .crjson or .json files for analysis. Some applicants may not have validate media types listed as would be normal for a "capture only" application (eg. camera app) and does not ingest files that may have manifests.

If applicants assert that their product validates incoming manifests as ingredients, they must show samples of ingesting manifests into their application for every asserted media type. The Conformance Program maintains a library of sample C2PA-Conformant assets that applicants can use in their testing and evidence:

#### Validator Product Sample Evidence

Validator Product applicants must provide sample validation results of every asserted validate media type in their Generator Product Program Intake Form, along with their associated .json or .crjson files for analysis. The Conformance Program maintains a library of sample C2PA-Conformant assets that applicants can use in their testing and evidence

We recommend that Validator Product applicants provide the Conformance Program access to validation evidence so we can ingest our own samples into the Applicant’s product and determine conformance of the activity.

#### Certification Authority Evidence Request

[Applicant](#applicant)s that are applying to the Conformance Program for the purpose of including their [Certification Authority](#ca) Root and Intermediate CA on the [C2PA Trust List](#_c2pa_trust_list) are required to provide evidence that these certificates meet the certificate profiles on the Certificate Policy and the generation of keys included in those certificates were independently witnessed within a process that was scripted and available for C2PA review.

### Evidence Assessment and Approval

The Administrator of the C2PA Conformance Program will review conformance evidence supplied by the Applicant to determine whether the Applicant has met conformance program requirements. This may involve this may involve email communication. Once the Administrator has been satisfied with the evidence, the [Applicant](#applicant) record will be submitted for approval. Controls with the C2PA Conformance Program require that at least two separate individuals are involved in the update of public repository records.

All pull requests from the staging libraries to the public repository require an approval from someone besides an Administrator. To provide for a fair and consistent application of Conformance Program requirements, the program has created internal checklists, conformance tools, and assessment spreadsheets that document the required administrative steps that support a conformant record. In conjunction with the creation of the pull request, the Administrator completes the approval documentation to support their conformant recommendation.

### Application Approval

The Applicant’s pull request record and its supporting information is reviewed by an Approver. If the Approver identifies nonconformities or has questions of the Applicant, all issues and questions are noted in the case record and separately communicated back to the Applicant for answers or remediation. When updated responses and evidence satisfy both the Administrator and the Approver, a final record will be created, ready for publication.

### Notice of Conformance

If approved, the Administrator will proceed to establishing an Applicant record on either the C2PA Trust List or the Conforming Products List. After a pull request for an update for an Applicant’s record to the public repository has been approved, the Administrator will create a digitally signed Notice of Conformant Status letter. Even if an Applicant’s Generator Product has not reached the Date of Earliest Public Disclosure, GP Applicants can provide this letter to their conformant CA of choice so they can start to receive conformant production certificates.

### Public Record Posting

Approved [Applicant](#applicant)s will either appear on the Certification Authority Trust List or the C2PA Conforming Products List. The C2PA Administrator will add attributes of the Applicant’s trust list record based on information supplied on its Intake Form. Once a record has been established to the respective Trust List, the C2PA Administrator will preview the record and confirm the contents of the record prior to publishing. [Applicant](#applicant)s have the option of submitting an "Earliest Date of Release" to its Intake Form which delays the issuance of the conformant record until a specific date. This might be useful for pre-released products that have a pre-defined release date. Once confirmed with the Applicant, the C2PA will publish the record on the date specified.

The C2PA Conformance Program has created a human-readable form of our public trust lists, the Conformance Explorer (<https://spec.c2pa.org/conformance-explorer/>).

### Definition of Material Change Requiring New Conformance Program Application

Once a record of the Applicant’s Generator Product is published on the C2PA Conforming Products List, the product SHALL re-submit their Generator Product or Validator Product to the Conformance Program IF the product undergoes a "material change", one that constitutes a clear modification to the product’s Conforming Product List record or its conformance to the Generator Product Security Requirements Document. The modified product SHALL be attributed to a new record id on the C2PA Conforming Products List.

## Machine-Readable List Operation

### Use of C2PA Machine-Readable Lists

- Approved [Certification Authority](#ca) Applicants of the C2PA Conformance Program appear on the [C2PA Trust List](#_c2pa_trust_list).

- Approved [Generator Product](#_generator_product)s and [Validator Product](#_validator_product)s appear on the [C2PA Conforming Products List](#_c2pa_conforming_products_list).

- [Applicant](#applicant)s whose conforming [Generator Product](#_generator_product)s appear on the C2PA Conforming Products List MUST access the C2PA Trust List to determine whether a Certification Authority has been approved by the Conformance Program.

- Instances of conforming [Generator Product](#_generator_product)s MUST be issued a [C2PA Claim Signing Certificate](#claimsigning-certs) from a CA that appears on the C2PA Trust List.

- CAs that appear on the C2PA Trust List MUST only issue [C2PA Claim Signing Certificates](#claimsigning-certs) to instances of [Generator Product](#_generator_product)s that have a record with a `status` of `conformant` on the C2PA Conforming Products List.

- Conforming [Validator Product](#_validator_product)s SHALL regularly refresh the C2PA Trust List to determine whether a [C2PA Claim](#_c2pa_claim) is signed with a [C2PA Claim Signing Certificate](#claimsigning-certs) that cryptographically ladders up to a [Certification Authority](#ca) on the C2PA Trust List.

- Validator products SHOULD access the C2PA Conforming Products List to determine whether [Generator Product](#_generator_product)s are approved and recognized by the C2PA Conformance Program. Manifest consumers SHOULD review the C2PA Trust List and C2PA Conforming Products List to determine whether CAs, Generator Products, or [Validator Product](#_validator_product)s have been approved by the C2PA and have an active status in the program.

### Security Controls Over C2PA Machine-Readable Lists

The C2PA Conformance Program mandates tight access controls over the C2PA Trust List, the C2PA TSA Trust List, and the C2PA Conforming Products List while maintaining high availability to relying parties.

Access controls to the machine-readable lists are limited to designated members of the C2PA Conformance Program Task Force which independently administers the program. All changes to any of the machine-readable lists require multi-party approval quorum.

### Removal of Conforming Products List / C2PA Trust List Record

The C2PA reserves the right to and remove Applicants from the C2PA Trust List and C2PA TSA Trust List, or revoke the `conformant` status of a [Generator Product](#_generator_product) or [Validator Product](#_validator_product) on the C2PA Conforming Products List.

Factors indicating the need for removal MAY originate from the global marketplace or within the C2PA itself. If an action has been taken for machine-readable list removal, the [Governed Party](#_governed_party) will be formally notified and required to appear before the C2PA Conformance Program Task Force where evidence will be considered concerning the party’s violation of the terms of its acceptance as an approved service provider of its conformance program. Based on this evaluation, the Conformance Task Force will make a recommendation for removal to the C2PA Steering Committee for its final decision.

### Dispute Mediation and Arbitration

The C2PA Conformance Program has mediation measures in place to support appeals of C2PA actions. It has established an independent committee which acts in the interests of all parties to mediate disputes between parties. Any dispute between the [C2PA Conformance Program](#_c2pa_conformance_program) and a [Governed Party](#_governed_party) not resolved by mediation shall be settled by the arbitration process defined in the legal agreement between the parties.

### Program Versioning and Grace Period

This version of the Conformance Program is stated at v0.2. This version accepts Applicant assertions as meeting the C2PA Content Credential Specification v2.2 and v2.4. If and when the C2PA Conformance Task Force decides to deprecate C2PA Conformance Requirements or C2PA Content Credential versions its supports, it MUST announce and allow a grace period of no less than 90 days to provide Applicants the time to adjust to new sets of requirements.

| Version | Sunrise | Sunset | Comments |
|----|----|----|----|
| 0.1 | 2025-06-02 | 2026-10-09 | First version of conformance program, supporting Spec v2.2. |
| 0.2 | 2026-07-31 | Not set | Updated conformance program, supporting Spec v2.2 and v2.4. |

Conformance Program Versions and Grace Periods

Sunrise means the date on which the Conformance Program version is announced and open for Applicant intake. Sunset means the date on which the Conformance Program version is deprecated and no longer accepting new Applicants. The grace period is the time between the announcement of a new version and the sunset of the previous version, during which Applicants can adjust to new requirements.

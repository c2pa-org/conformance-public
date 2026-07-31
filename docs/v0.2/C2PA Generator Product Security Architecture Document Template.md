# C2PA Generator Product Security Architecture Document Template

_Please note that sections marked "Required" for a particular section must be present and filled in order for the Generator Product to be evaluated at its target Assurance Level. Even if a particular section is not marked "Required" for the target Assurance Level, it is strongly recommended that the Applicant provide as much detail as possible that may be relevant in that section._

---

## 1. Generator Product Information

_(Refers to C2PA Generator Product Security Requirements §1 Scope and §3 Overview)_

### 1.1 Applicant organization details

_Please provide the full legal name of the Applicant organization, its address, and contact information._

### 1.2 C2PA Conformance Program Version

_Please specify the C2PA Conformance Program Version under which this application is being submitted (e.g., "0.1", "0.2")._

### 1.3 C2PA Content Credentials Specification Version

_Please specify the C2PA Content Credentials Specification Version under which this Generator Product is being evaluated (e.g., "2.2", "2.4")._

### 1.4 Distinguished name

_Please document the values of the following fields for the Generator Product's Distinguished Name:_

1. **Common Name (CN)**: _the user-facing marketing name and/or model of the device, application, or service_
2. **Organization (O)**: _the legal name of the Applicant organization_
3. **Organizational Unit (OU)**: _(optional) the department or subdivision within the Applicant's organization that created this product_
4. **Country (C)**: _Two-letter country code in ISO 3166-1 alpha-2 format where the organization named in the 'O' field has its base of operations._

### 1.5 Generator Product Description

_Please provide a high-level description of the Generator Product, including its intended use cases, target audience, and key features._

### 1.6 Generator Product Target of Evaluation (GP TOE) Description

_Please provide a high-level description of the complete Target of Evaluation of this submission, which encompasses the Generator Product as well as the underlying platform(s) on which the Generator Product will perform its functions._

_**Architectural diagrams are strongly encouraged.**_

### 1.7 Implementation Class

_Please specify the Implementation Class of this Generator Product: **Edge**, **Backend**, or **Distributed**._

### 1.8 Target Max Assurance Level

_Please specify your intended maximum Assurance Level for which this Generator Product should be evaluated._

### 1.9 Target Generator Product capabilities

_Please provide the list of claim generation and claim validation functions that this Generator Product will support for various media types._

_The list of supported media types must be a subset of the following:_

1. Claim generation:
   * Still image media types:
     * `image/jpeg`
     * `image/jxl`
     * `image/png`
     * `image/svg+xml`
     * `image/gif`
     * `image/x-adobe-dng`
     * `image/tiff`
     * `image/webp`
     * `image/heic`
     * `image/heic-sequence`
     * `image/heif`
     * `image/heif-sequence`
     * `image/avif`
     * `image/x-tiff-based`
     * `image/x-riff-based`
   * Video media types:
     * `video/x-msvideo`
     * `video/mp4`
     * `video/quicktime`
     * `video/x-bmff-based`
     * `video/x-riff-based`
   * Audio media types:
     * `audio/flac`
     * `audio/MPA`
     * `audio/mpeg`
     * `audio/wav`
     * `audio/aac`
     * `audio/mp4`
     * `audio/x-riff-based`
   * Text media types:
     * HTML:
       * `text/html`
     * Unstructured text:
       * `text/csv`
       * `text/tab-separated-values`
       * `text/plain`
     * Structured text:
       * `text/markdown`
       * `text/xml`
       * `application/xml`
       * `application/xhtml+xml`
   * Document media types:
     * `application/pdf`
     * `application/epub+zip`
     * `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
     * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
     * `application/vnd.openxmlformats-officedocument.presentationml.presentation`
     * `application/vnd.openxmlformats-officedocument.presentationml.slideshow`
     * `application/vnd.oasis.opendocument.text`
     * `application/vnd.oasis.opendocument.spreadsheet`
     * `application/vnd.oasis.opendocument.presentation`
     * `application/vnd.oasis.opendocument.graphics`
     * `application/oxps`
     * `application/x-zip-based`
   * Fonts:
     * `font/otf`
   * ML Models:
     * `jax`
     * `keras`
     * `ml_net`
     * `mxnet`
     * `onnx`
     * `openvivo.parameter`
     * `openvivo.topology`
     * `pytorch`
     * `tensorflow`
     * `numpy`
     * `protobuf`
     * `pickle`
     * `savedmodel`
2. Claim validation:
   * Still image media types:
     * `image/jpeg`
     * `image/jxl`
     * `image/png`
     * `image/svg+xml`
     * `image/gif`
     * `image/x-adobe-dng`
     * `image/tiff`
     * `image/webp`
     * `image/heic`
     * `image/heic-sequence`
     * `image/heif`
     * `image/heif-sequence`
     * `image/avif`
     * `image/x-tiff-based`
     * `image/x-riff-based`
   * Video media types:
     * `video/x-msvideo`
     * `video/mp4`
     * `video/quicktime`
     * `video/x-bmff-based`
     * `video/x-riff-based`
   * Audio media types:
     * `audio/flac`
     * `audio/MPA`
     * `audio/mpeg`
     * `audio/wav`
     * `audio/aac`
     * `audio/mp4`
     * `audio/x-riff-based`
   * Text media types:
     * HTML:
       * `text/html`
     * Unstructured text:
       * `text/csv`
       * `text/tab-separated-values`
       * `text/plain`
     * Structured text:
       * `text/markdown`
       * `text/xml`
       * `application/xml`
       * `application/xhtml+xml`
   * Document media types:
     * `application/pdf`
     * `application/epub+zip`
     * `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
     * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
     * `application/vnd.openxmlformats-officedocument.presentationml.presentation`
     * `application/vnd.openxmlformats-officedocument.presentationml.slideshow`
     * `application/vnd.oasis.opendocument.text`
     * `application/vnd.oasis.opendocument.spreadsheet`
     * `application/vnd.oasis.opendocument.presentation`
     * `application/vnd.oasis.opendocument.graphics`
     * `application/oxps`
     * `application/x-zip-based`
   * Fonts:
     * `font/otf`
   * ML Models:
     * `jax`
     * `keras`
     * `ml_net`
     * `mxnet`
     * `onnx`
     * `openvivo.parameter`
     * `openvivo.topology`
     * `pytorch`
     * `tensorflow`
     * `numpy`
     * `protobuf`
     * `pickle`
     * `savedmodel`

---

## 2. Security Architecture Details by Objective

### 2.1 [O.1] Automated Certificate Enrollment Proof of Eligibility (§6.1)

_(Refers to C2PA Generator Product Security Requirements §6.1 / Objective O.1)_

#### 2.1.1 Assurance Level 1 & 2 Base Evidence (Enrollment Process & Secret Management)

_**Applicability:** Required for Assurance Level 1 and Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.1 Level 1 & Level 2 Static Evidence)_

_Please describe and document the following:_

1. **Certificate Enrollment Process**: _Describe the certificate enrollment process for instances of the Generator Product, including the triggers, steps involved, the entities involved, and the security measures in place. If certificate enrollment is automated with an API, please describe how authentication and secret management are handled._
2. **Authentication Method & API Details**: _Please provide detail of the specific enrollment authentication method used, and if it's automated, API details / documentation. This should be included either as part of this application, or as an update provided to the conformance program within 90 days of conformance being granted._
3. **Management of Authentication Secrets**: _Describe the method for managing authentication secrets used during certificate enrollment, including how they are generated, stored, and protected from unauthorized access._

#### 2.1.2 Assurance Level 2 Additional Evidence (Hardware Root of Trust Binary Identity)

_**Applicability:** Required for Assurance Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.1 Level 2 Static Evidence)_

_Please describe and document the following:_

1. **Confirming GP Binary Identity**: _Describe how the GP and/or GP TOE produce verifiable artifacts backed by a hardware Root of Trust, which the GP must provide to a CA during automated certificate enrollment, that confirm GP binary/binaries via package names, hashes, code signing certificates, other certificates, or a combination of the above._

---

### 2.2 [O.2] Confidentiality of the Claim Signing Key (§6.2)

_(Refers to C2PA Generator Product Security Requirements §6.2 / Objective O.2)_

#### 2.2.1 Assurance Level 1 & 2 Base Evidence (Key Generation, Least Privilege & Rotation)

_**Applicability:** Required for Assurance Level 1 and Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.2 Level 1 & Level 2 Static Evidence)_

_Please describe and document the following:_

1. **Key Generation & Storage**: _Describe how claim signing keys are generated and stored, including the cryptographic algorithms, key lengths, and storage mechanisms used (referencing NIST/ENISA approved algorithms)._
2. **Access Controls & Encryption**: _Detail the access control policies (enforcing least privilege) and encryption mechanisms in place to protect the claim signing key from unauthorized access both at rest and in volatile memory._
3. **Ephemeral Plaintext Key Handling** _(If applicable)_: _If plaintext claim signing keys are handled or stored ephemerally in volatile memory, describe the technical controls taken to minimize exposure and protect the key. Where handling is performed by non-GP code, include details of the vulnerability monitoring and upgrade process for that code._
4. **Key Rotation Process**: _Describe the triggers, procedures, and frequency for rotating the claim signing key._
5. **Subsystem Mutual Authentication & Role Validation** _(For **Distributed** and **Backend** classes)_: _Document the authentication methods (e.g., mTLS, shared secret, MAC, challenge-response) and role validation protocols between the Edge and Backend subsystems._

#### 2.2.2 Assurance Level 2 Additional Evidence (Key Management Environment & Hardware Attestation)

_**Applicability:** Required for Assurance Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.2 Level 2 Static Evidence)_

_Please describe and document the following:_

1. **Key Management Environment Properties**: _Describe the key management environment (e.g., Apple Secure Enclave, Android StrongBox/TEE Keystore, Windows TPM, AWS KMS, Azure Key Vault, Google Cloud KMS, HashiCorp Vault) used by the GP TOE, confirming that private key material is sequestered from Claim Generator memory and wrapped with hardware-derived keys._
2. **Hardware Root of Trust Attestation / 3rd-Party Auditor Certification**: _Detail either (a) how the key management environment produces verifiable artifacts backed by a hardware Root of Trust confirming private key possession, or (b) attach certification from an accredited, independent third-party auditor verifying the secure storage environment._

#### 2.2.3 Assurance Level 2 Additional Evidence for Distributed & Backend Classes (Calling Client Attestation)

_**Applicability:** Required for Assurance Level 2 for Distributed and Backend Implementation Classes only_  
_(Refers to C2PA Generator Product Security Requirements §6.2 Level 2 Static Evidence for Distributed & Backend Classes)_

_Please describe and document the following:_

1. **Hardware-Backed Client Attestation**: _Describe how the Backend claim-signing subsystem requests, decodes, and validates verifiable artifacts backed by a hardware Root of Trust (e.g., Apple App Attest, Google Play Integrity, Android Key Attestation, AWS Nitro Enclave Attestation) from the calling client before signing a claim._

---

### 2.3 [O.3] Protection of the Claim Generator (§6.3)

_(Refers to C2PA Generator Product Security Requirements §6.3 / Objective O.3)_

#### 2.3.1 Assurance Level 1 & 2 Base Evidence (SCA/SBOM Scan Tools & 90-Day Remediation Policy)

_**Applicability:** Required for Assurance Level 1 and Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.3 Level 1 & Level 2 Static Evidence)_

_Please describe and document the following:_

1. **SCA / SBOM Scanning Tools**: _Specify the Software Composition Analysis (SCA) or Software Bill of Materials (SBOM) scanning tools used during the Claim Generator build or integration process to detect vulnerabilities from the NIST National Vulnerability Database (NVD)._
2. **90-Day Remediation Policy**: _Describe the build and deployment pipeline controls that prevent the release—more than 90 days after detection—of any Claim Generator build containing vulnerabilities with `CRITICAL` or `HIGH` severity ratings (CVSS v3+)._

#### 2.3.2 Assurance Level 2 Additional Evidence (Exploit Countermeasures, Static Analysis & Patch Recency)

_**Applicability:** Required for Assurance Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.3 Level 2 Static Evidence)_

_Please describe and attach evidence for the following:_

1. **Exploit Countermeasures Enablement & Testing**: _Document the build scripts and compiler build flags confirming enablement of basic exploit countermeasures (ASLR, Stack Canaries, Guard Pages, DEP, Safe Heap, NX). Attach the **Countermeasures Functional Test Report**._
2. **Static Analysis**: _Identify the static analysis tools (e.g., Coverity, Fortify, Snyk Code, SonarQube, Klocwork) executed against the Claim Generator and its underlying platform._
3. **Privilege Isolation & Image Authentication**: _Describe how access control and binary image authentication for the Claim Generator and its platform are enforced by an environment with a higher privilege level._
4. **External Input Validation & Ingress ACLs** _(If relying on external inputs)_: _Detail the validation methods for accuracy and integrity of external inputs, malicious data detection/sanitization methods, and access control lists (ACLs) for external ingress points._
5. **Hardware Root of Trust Patch Recency / Revision Attestation**: _Detail the verifiable artifact method backed by a hardware Root of Trust that the GP TOE uses to prove either patch recency or specific revision eligibility to the CA during automated certificate enrollment._

---

### 2.4 [O.4] Protection of Assets & Assertions at Generation (§6.4)

_(Refers to C2PA Generator Product Security Requirements §6.4 / Objective O.4)_

#### 2.4.1 Assurance Level 1 & 2 Base Evidence (SCA/SBOM Scan Tools & Remediation for Content Software)

_**Applicability:** Required for Assurance Level 1 and Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.4 Level 1 & Level 2 Static Evidence)_

_Please describe and document the following:_

1. **SCA / SBOM Scanning Tools**: _Specify the SCA or SBOM vulnerability scanning tools used during the build or integration process for all software within the GP TOE that processes or modifies Digital Content or assertions._
2. **90-Day Remediation Policy**: _Describe the pipeline controls that prevent the release—more than 90 days after detection—of content-processing software with known `CRITICAL` or `HIGH` severity vulnerabilities (CVSS v3+)._

#### 2.4.2 Assurance Level 2 Additional Evidence (Countermeasures, Static Analysis, Kernel Isolation & Patch Recency)

_**Applicability:** Required for Assurance Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.4 Level 2 Static Evidence)_

_Please describe and attach evidence for the following:_

1. **Exploit Countermeasures Enablement & Testing**: _Document the build scripts and compiler flags confirming enablement of basic exploit countermeasures for content-processing software. Attach the **Countermeasures Functional Test Report**._
2. **Static Analysis**: _Identify the static analysis tools executed against all content-processing and assertion-generating software._
3. **Binary Image Authentication**: _Describe the image authentication methods enforced by a higher-privilege environment for all content-processing and assertion-generating binaries._
4. **Kernel / OS-Level Process & Thread Isolation**: _Confirm and demonstrate that content-processing source processes (and/or threads in RTOS environments) run under a unique operating system UID/user account, and that inter-process communication (IPC) channels and memory are protected by access control lists (ACLs)._
5. **Hardware Root of Trust Patch Recency / Revision Attestation**: _Detail the verifiable artifact method backed by a hardware Root of Trust used to attest to binary integrity and patch recency/revision eligibility for content-processing software._

---

### 2.5 [O.5] Protection of Traffic Between Subsystems (§6.5)

_(Refers to C2PA Generator Product Security Requirements §6.5 / Objective O.5)_

#### 2.5.1 Assurance Level 1 & 2 Base Evidence for Distributed & Backend Classes (TLS 1.3 & Cryptographic Protocols)

_**Applicability:** Required for Assurance Level 1 and Level 2 for Distributed and Backend Implementation Classes only_  
_(Refers to C2PA Generator Product Security Requirements §6.5 Level 1 & Level 2 Static Evidence for Distributed & Backend Classes)_

_Please describe and document the following:_

1. **TLS 1.3 & Cryptographic Protocols**: _Document the TLS versions (TLS 1.3 or higher) or equivalent protocols in use, along with supported cryptographic algorithms and cipher suites for network communication between the Edge and Backend subsystems._

#### 2.5.2 Assurance Level 2 Additional Evidence (Kernel-Level IPC Isolation & Thread/Process Separation)

_**Applicability:** Required for Assurance Level 2_  
_(Refers to C2PA Generator Product Security Requirements §6.5 Level 2 Static Evidence)_

_Please describe and document the following:_

1. **Kernel / OS-Level IPC & Process Isolation**: _Demonstrate how the kernel or operating system isolates asset- and assertion-transmitting processes/threads (e.g., unique OS UIDs) and protects inter-process communication channels (e.g., Android broadcasters/receivers, IPC channels) with strict access control lists._

---

### 2.6 [O.6] Protection of the Hosting Environment (§6.6)

_(Refers to C2PA Generator Product Security Requirements §6.6 / Objective O.6)_

#### 2.6.1 Assurance Level 1 & 2 Base Evidence for Distributed & Backend Classes (IAM, RBAC, Cloud Resource Policies & OWASP Top 10)

_**Applicability:** Required for Assurance Level 1 and Level 2 for Distributed and Backend Implementation Classes only_  
_(Refers to C2PA Generator Product Security Requirements §6.6 Level 1 & Level 2 Static Evidence for Distributed & Backend Classes)_

_Please describe and document the following:_

1. **IAM & Role-Based Access Control (RBAC)**: _Describe the IAM system employed and how RBAC policies protect security boundaries (e.g., virtual machines, cloud storage repositories) related to asset and claim generation._
2. **Principal Access Policies**: _Detail the access policies for both human and non-human principals (e.g., service accounts, production identities)._
3. **Cloud Resource IAM Policies**: _Describe the IAM policies governing access to primary cloud resources (e.g., VM instances, cloud storage buckets, KMS repositories)._
4. **Vulnerability Scanning & OWASP Top 10 Coverage**: _Describe the process for vulnerability scanning and security review of software dependencies and API surfaces, explicitly confirming coverage of the OWASP Top 10 web application vulnerabilities._
5. **Timely Remediation Policy**: _Describe the operational process ensuring that identified vulnerabilities are remediated within required timelines (30 days for High, 90 days for Moderate, 180 days for Low CVSS severity)._

#### 2.6.2 Assurance Level 2 Additional Evidence for Distributed & Backend Classes (Audit Logging, HIDS, Network Segmentation & Attached Reports)

_**Applicability:** Required for Assurance Level 2 for Distributed and Backend Implementation Classes only_  
_(Refers to C2PA Generator Product Security Requirements §6.6 Level 2 Static Evidence for Distributed & Backend Classes)_

_Please describe and document the following:_

1. **Audit Logging & Event Monitoring**: _Describe the audit logging system, event logging policies, and monitoring rules deployed to track security-relevant events (e.g., administrative and human access)._
2. **Host-Based Intrusion Detection System (HIDS)**: _Describe the HIDS or distributed integrity monitoring system deployed to detect suspicious activities and monitor system integrity._
3. **Network Architecture & Segmentation**: _Describe the network architecture, configuration, and segmentation boundaries isolating the hosting environment._
4. **Required Attached Reports**: _Please attach the following verification reports to this document:_
   * **Attachment A**: _Report showing audit logging is enabled and actively monitored._
   * **Attachment B**: _Report showing active operation of the HIDS or integrity monitoring system._
   * **Attachment C**: _Report showing active network segmentation and isolation covering the application's network infrastructure._

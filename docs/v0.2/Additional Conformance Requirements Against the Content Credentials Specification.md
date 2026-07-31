---
author: C2PA Technical Working Group Conformance Task Force
date: 2026-07-31
title: Additional Conformance Requirements Against the Content Credentials Specification
version: v0.2
---

# Introduction

One critical aspect of the C2PA Conformance Program is the contractual binding that Generator and Validator Product Applicants have to conform to the C2PA Content Credentials Specification (Spec) at the Spec version level they initially assert within the Program Intake Form, and is posted on our Conforming Products List (CPL). This document lists additional requirements of the C2PA Conformance Program, which are not requirements asserted in the Spec, that the program requires Applicants to be conformant with as part of the conformance acceptance process.

# Requirements

## Required Use of the specVersion Key within claim_generator_info for All Generated Manifests.

Applies to Spec Version 2.4 and higher.

### Context

In the Spec (version 2.4) it is stated,

> To facilitate testing and diagnosing interoperability issues between claim generators and validators, a claim generator should declare which version of the specification it is using to generate the C2PA Manifest by providing a `specVersion` key in the `claim_generator_info` field of the claim. When a claim generator sets this field, it is declaring that the active manifest of the asset is produced in accordance with that version of the specification and thus, for example, does not contain any constructs that are deprecated in that version of the specification …​

As the Conformance Program requires Generator Product Applicants to assert and be conformant to a stated version(s) of the Spec, it also requires Generator Products to indicate that stated version as part of the generated manifest. Generator Products accomplish this by setting the value of the `specVersion` field of the `claim_generator_info` object to the version of the Spec that appears in the C2PA Conforming Products List Record for the Generator Product, and that the Generator Product is currently conformant to.

### Stated Requirement

A Generator Product SHALL declare which version of the C2PA Content Credential Specification it is using to generate the C2PA Manifest by providing a `specVersion` key in the `claim_generator_info` object of the manifest’s Claim. That version number SHALL be equivalent to the Spec version asserted in its Program Intake Form and equivalent to the version(s) that appear on its CPL record.

### Enforcement Mechanism

All Generator Product Applicants indicate the Spec Version they assert conformance on their Program Intake Form. If an Applicant selects v2.4 or later, the stated requirement shall be enforced as follows:

All Generator Product Applicants are required to submit samples of generated manifests demonstrating conformance to the Spec version asserted within their Program Intake Form. All submitted samples SHALL include a `specVersion` key in the `claim_generator_info` object of the manifest’s Claim. The value of that key SHALL be the same as the asserted Spec Version on their submitted Program Intake Form.

## Mandatory Presence of allActionsIncluded Field.

Applies to Spec Version 2.2 and 2.4.

### Context

Version 2.2 of the Spec introduces an optional `allActionsIncluded` field in `actions-map-v2`. Setting this field to `true` indicates that only the actions listed in the actions assertions were performed on the asset. Setting it to `false` indicates that additional actions not listed in the actions assertions may have been performed.

Version 0.2 of the Conformance Program introduces Asset Rubrics, a framework that enables a consistent interpretation of provenance for standardized classification of assets. For this classification to be unambiguous, it is necessary to declare whether all actions performed on the asset are included in its provenance.

### Stated Requirement

Generator Product Applicants for spec versions 2.2 and 2.4 SHALL ensure that the Generator Product populates the `actions-map-v2` `allActionsIncluded` field with one of the defined values (*true* or *false*).

### Enforcement Mechanism

All Generator Product Applicants are required to submit samples of generated manifests demonstrating conformance to the Spec version asserted within their Program Intake Form. All submitted samples SHALL include the actions-map-v2 allActionsIncluded field with one of the defined values (true or false).

## Support of crJSON format for evaluation of product with validation functionality.

Applies to all Spec Versions.

### Context

To enable consistent and automated assessment by the Conformance Administrator, Applicants SHALL have a test harness for their product that supports testing the product’s validation functionality. The test harness SHALL accept the following inputs:

1.  an asset to validate

2.  a (test) C2PA Trust List

3.  a (test) C2PA TSA Trust List

4.  a validation time (RFC 3339)

Given these inputs, the test harness SHALL produce the validation results in [crJSON](https://spec.c2pa.org/specifications/specifications/2.4/crJSON/crjson-format.html) format. Applicants will be provided with a set of such test inputs and SHALL provide the outputs to the Conformance Administrator as part of the evaluation process.

### Stated Requirement

For a Validator Product or Generator Product with validation functionality, Applicant SHALL provide validation results in crJSON format for a set of test inputs provided by the Conformance Program.

### Enforcement Mechanism

All Applicants are required to participate in conformance testing using assets provided by the Conformance Program.

## Mandatory Presence of digitalSourceType Field in Selected pre-defined C2PA Actions.

Applies to Spec Version 2.2 and 2.4.

### Context

The Spec requires a `digitalSourceType` field, with an appropriate value, in the `c2pa.created` action, to indicate the nature of the asset at its inception. The Spec does not require `digitalSourceType` in any other actions.

Version 0.2 of the Conformance Program introduces Asset Rubrics, a framework that enables a consistent interpretation of provenance for standardized classification of assets. For this classification to be unambiguous, `digitalSourceType` field, with an appropriate value, needs to be recorded in selected actions carried within created assertions. This is particularly important to unambiguously capture involvement, if any, of generative AI.

### Stated Requirement

`digitalSourceType` field, with an appropriate value, SHALL be recorded in all C2PA pre-defined actions carried within created assertions except for: `c2pa.converted`, `c2pa.edited.metadata`, `c2pa.enhanced`, `c2pa.opened`, `c2pa.placed`, `c2pa.published`, `c2pa.redacted`, `c2pa.repackaged`, `c2pa.resized.proportional`, `c2pa.transcoded`, `c2pa.watermarked`, `c2pa.watermarked.bound` and `c2pa.watermarked.unbound`.

> [!NOTE]
> This requirement does not prohibit recording the `digitalSourceType` field, with an appropriate value, in these excepted actions, however a separate requirement prohibits it for the `c2pa.opened` action for Spec Version 2.4.

### Enforcement Mechanism

All Generator Product Applicants are required to submit samples of generated manifests demonstrating conformance to the Spec version asserted within their Program Intake Form. For all submitted samples, the `digitalSourceType` field, with an appropriate value, SHALL be recorded for selected C2PA pre-defined actions.

## Prohibition of digitalSourceType Field in c2pa.opened Actions

Applies to Spec Version 2.4.

### Context

The Spec requires a `digitalSourceType` field, with an appropriate value, to be recorded with the `c2pa.created` inception action. The Spec explicitly states that no `digitalSourceType` field is required in conjunction with a `c2pa.opened` inception action.

In the Spec, a `c2pa.opened` action indicates that an existing asset was opened to serve as a `parentOf` ingredient. This action merely opens an ingredient’s byte stream. As such, attaching a digital source type is semantically ambiguous.

### Stated Requirement

A `c2pa.opened` action SHALL NOT contain a `digitalSourceType` field.

### Enforcement Mechanism

For all Generator Products that support ingesting ingredients, Applicants are required to submit samples showing no digital source type values for `c2pa.opened` actions.

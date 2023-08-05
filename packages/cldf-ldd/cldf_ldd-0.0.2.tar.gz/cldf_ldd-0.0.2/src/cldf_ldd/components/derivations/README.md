# Derivations
A derivation relates a [stem](../stems) or a [root](../morphs) to a derived stem.
Optionally, it can reference a morphological part of the derived stem.


## DerivationTable: `derivations.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
`Process_ID` | `string` | singlevalued | The derivational process involved. References DerivationalprocessTable (processs.csv)
`Target_ID` | `string` | singlevalued | The derived stem. References StemTable (stems.csv)
`Source_ID` | `string` | singlevalued | The stem to which the derivational process applies. References StemTable (stems.csv)
`Root_ID` | `string` | singlevalued | The root to which the derivational process applies. References MorphTable (morphs.csv)
`Stempart_IDs` | list of `string` (separated by `,`) | multivalued | Specifies one or multiple morphs in the stem marking the derivation. References Stemparts (stemparts.csv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | unspecified | <div> <p> A human-readable comment on a resource, providing additional context. </p> </div> 
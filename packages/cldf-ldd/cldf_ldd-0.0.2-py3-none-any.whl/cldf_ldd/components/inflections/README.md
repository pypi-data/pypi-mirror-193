Inflection consists of morphological processes with which wordforms express [grammatical categories](../inflectionalcategories) like person, tense, or gender.
Inflections are conceptualized as linking a [wordform](../wordforms) with the following entities: a [stem](../stems) (of which it is an inflected form), an [inflectional value](inflectionalvalues) (for which it is inflected), and optionally a [part of a wordform](../wordformparts) (which is the exponent of the inflectional value).
This mechanism allows for inflectional values to not be bound to a specific morph (e.g., values that are zero-marked or expressed with nonsegmental means), or to have multiple inflectional values expressed in a single morph.

## InflectionTable: `InflectionTable`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
`Wordform_ID` | `string` | singlevalued | The wordform this inflection describes. References WordformTable (wordforms.csv)
`Stem_ID` | `string` | singlevalued | The stem this wordform is an inflected form of. References StemTable (stems.csv)
`Value_ID` | `string` | singlevalued | The inflectional value being expressed. References InflValTable (inflectionalvalues.csv)
`Wordformpart_ID` | `string` | singlevalued | The part of the wordform expressing this value. References Wordformparts (wordformparts.csv)
# Wordformparts


## WordformParts: `wordformparts.csv`

Name/Property | Datatype | Cardinality | Description
 --- | --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | singlevalued | <div> <p>A unique identifier for a row in a table.</p> <p> To allow usage of identifiers as path components of URLs IDs must only contain alphanumeric characters, underscore and hyphen. </p> </div> 
`Wordform_ID` | `string` | singlevalued | The involved wordform. References WordformTable (wordforms.csv)
`Morph_ID` | `string` | singlevalued | The involved morph. References MorphTable (morphs.csv)
`Index` | `string` | singlevalued | Specifies the position of a morph in a wordform.
`Gloss_ID` | `string` | singlevalued | The gloss the morph has in the wordform. References GlossTable (glosses.csv)
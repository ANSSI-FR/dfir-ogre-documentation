---
 title: 'Merge File'
---


{{< callout type="important" >}}Data Type: **merge_file** \
	Python Parser: **Merge**{{< /callout >}}

### Description 

Each row is the complete text of one multiline input artifact after its lines are concatenated for downstream parsing or language-model analysis. It preserves content but adds no independent event semantics, timestamps, or provenance beyond the source file. Interpret any claims using the originating artifact and collection context.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Description |
|---|---|---|

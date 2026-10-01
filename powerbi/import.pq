// Change FilePath to the local clean CSV path. Name the query Campaigns.
let
 FilePath = "C:\\marketing-roi\\data\\clean_campaigns.csv",
 Source = Csv.Document(File.Contents(FilePath),[Delimiter=",",Columns=11,Encoding=65001,QuoteStyle=QuoteStyle.Csv]),
 Headers = Table.PromoteHeaders(Source,[PromoteAllScalars=true]),
 Types = Table.TransformColumnTypes(Headers,{{"date",type date},{"campaign_id",type text},{"channel",type text},{"audience",type text},{"spend",type number},{"impressions",Int64.Type},{"clicks",Int64.Type},{"acquisitions",Int64.Type},{"revenue",type number},{"contribution_profit",type number},{"month",type text}},"en-US")
in Types

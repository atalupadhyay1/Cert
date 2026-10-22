# Microsoft PL-300 — Full-Length Mock Exam 6

Power BI Data Analyst · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A group archive of forty million ledger rows is analysed daily, and the source must not serve analyst queries. Which connection fits?

Domain: Prepare the data

- A. Live connection to a published semantic model
- B. DirectLake over a lakehouse
- C. Import mode
- D. DirectQuery

### 2. A group needs live operational status on one dashboard and governed definitions on another. Which two choices fit? Select two.

Domain: Prepare the data

- A. DirectQuery
- B. Live connection to a published semantic model
- C. DirectLake over a lakehouse
- D. Connect to a shared semantic model instead of importing the source again
- E. Dual mode table

### 3. Delta tables in a group lakehouse must be queried at Import-like speed without a copy. Which mode fits?

Domain: Prepare the data

- A. Dual mode table
- B. DirectLake over a lakehouse
- C. DirectQuery
- D. Import mode

### 4. A composite model imports dimensions from the group and queries each business fact directly, and dimension lookups cost round trips. Which setting helps?

Domain: Prepare the data

- A. DirectQuery
- B. DirectLake over a lakehouse
- C. Dual mode table
- D. Import mode

### 5. A subsidiary's compliance rule forbids copying its data into a shared model. Which mode fits?

Domain: Prepare the data

- A. Import mode
- B. DirectLake over a lakehouse
- C. Dual mode table
- D. DirectQuery

### 6. A group consolidation of sixty million rows is reported monthly and the source is a busy ERP. Which mode fits?

Domain: Prepare the data

- A. Import mode
- B. Dual mode table
- C. DirectQuery
- D. DirectLake over a lakehouse

### 7. The same group query must read a subsidiary test database and then production. What should be created?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Update the data source credentials in the semantic model settings
- C. Create a parameter for the server, path, or filter
- D. Change the data source settings rather than rebuilding the query

### 8. A query combines subsidiary finance data with group HR data, and the engine is folding across them. What should be configured?

Domain: Prepare the data

- A. Change the data source settings rather than rebuilding the query
- B. Create a parameter for the server, path, or filter
- C. Set privacy levels to isolate the sources
- D. Update the data source credentials in the semantic model settings

### 9. Group refresh fails with an authorization error after a managed identity secret was rotated. What should be updated?

Domain: Prepare the data

- A. Update the data source credentials in the semantic model settings
- B. Change the data source settings rather than rebuilding the query
- C. Set privacy levels to isolate the sources
- D. Create a parameter for the server, path, or filter

### 10. A group currency column arrives as text with symbols, so consolidation totals misbehave. What should be corrected?

Domain: Prepare the data

- A. Review column statistics and value distribution
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Profile the column with column quality, distribution, and profile views
- D. Correct the column data type before building the model

### 11. A group treasurer asks whether a few subsidiaries dominate intercompany balances. Which evidence answers that?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Profile the column with column quality, distribution, and profile views
- C. Review column statistics and value distribution
- D. Replace nulls with a defined placeholder or a filled-down value

### 12. A group is onboarding four subsidiary feeds at once. Which sequence keeps rework out of the build?

Domain: Prepare the data

- A. Shape the table → delete the profiling steps → load every column
- B. Profile the source → fix types and nulls → shape the table → load only the needed columns
- C. Load the table → discover the type errors in the report → re-import the source
- D. Load every column → profile in the report → patch the visual

### 13. Group revenue doubles whenever a subsidiary batch is reprocessed. What is the most likely cause?

Domain: Prepare the data

- A. Remove duplicate rows using the natural business key
- B. Filter out the error rows and report them separately
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Trim, clean, and standardize the text values

### 14. Subsidiary names differ only by trailing spaces and casing, and a few rows fail on a country code. Which two fixes are required? Select two.

Domain: Prepare the data

- A. Remove duplicate rows using the natural business key
- B. Trim, clean, and standardize the text values
- C. Filter out the error rows and report them separately
- D. Replace nulls with a defined placeholder or a filled-down value
- E. Use a locale-aware conversion for dates and decimals

### 15. A group margin column is blank where a business does not report margin, and averages swing wildly. What should be done?

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Remove duplicate rows using the natural business key
- C. Filter out the error rows and report them separately
- D. Replace nulls with a defined placeholder or a filled-down value

### 16. A consolidation extract has stray characters, duplicated members, and mixed formats. Which sequence is defensible?

Domain: Prepare the data

- A. Identify the bad values → standardize text → convert types → document what was replaced
- B. Replace all values with a default → convert types → load
- C. Convert types first → then look for duplicates → then trim
- D. Filter out the failing rows → load → ask the business later

### 17. The group report needs a single label combining business unit and entity code. What should be added?

Domain: Prepare the data

- A. Extract the needed part of the text with a delimiter or position
- B. Group by the key and aggregate the measures
- C. Add a conditional column for rule-based bucketing
- D. Add a custom column with an M expression

### 18. The consolidated amount must be numeric, and the monthly roll-up must sum rather than count. Which two steps are required? Select two.

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Extract the needed part of the text with a delimiter or position
- C. Add an aggregate step with the correct summarization
- D. Add a custom column with an M expression
- E. Add a conditional column for rule-based bucketing

### 19. Entities must be classified as core, growth, or divest using the group portfolio policy. What should be added?

Domain: Prepare the data

- A. Group by the key and aggregate the measures
- B. Split the combined column into separate fields
- C. Add a custom column with an M expression
- D. Add a conditional column for rule-based bucketing

### 20. A group extract has one column per subsidiary, and the model needs one entity column and one value column. What should be done?

Domain: Prepare the data

- A. Unpivot the month columns into rows
- B. Pivot the attribute values into columns
- C. Transpose the table so the header becomes a column
- D. Expand the JSON record into typed columns

### 21. An intercompany feed returns an XML document with repeated entries. What should be done?

Domain: Prepare the data

- A. Transpose the table so the header becomes a column
- B. Convert the list value to a table and expand it
- C. Convert the XML or JSON list into a table of rows
- D. Expand the JSON record into typed columns

### 22. A group API returns a JSON object per entity with nested contact fields. What should be done?

Domain: Prepare the data

- A. Transpose the table so the header becomes a column
- B. Convert the list value to a table and expand it
- C. Convert the XML or JSON list into a table of rows
- D. Expand the JSON record into typed columns

### 23. Four subsidiary sales files share the same columns and must become one table. What should be used?

Domain: Prepare the data

- A. Append the queries into one table
- B. Use a left outer join to keep every fact row
- C. Merge the two queries on a matching key
- D. Use a fuzzy merge with a similarity threshold

### 24. A consolidated fact must gain group account mapping, and no row may be lost when a subsidiary code is unmapped. Which two choices are required? Select two.

Domain: Prepare the data

- A. Use a left outer join to keep every fact row
- B. Append the queries into one table
- C. Merge the two queries on a matching key
- D. Create an integer surrogate key for the relationship
- E. Use a fuzzy merge with a similarity threshold

### 25. The same group transformation is repeated in six models, and each refresh must stay fast. Which two choices address that? Select two.

Domain: Prepare the data

- A. Keep the steps foldable so the source does the work
- B. Use a native query to select only the needed rows
- C. Duplicate the query so the two are independent
- D. Reuse a dataflow for the shared transformation
- E. Stage the raw query and build a separate clean query on it

### 26. A consolidated table repeats entity name, region, and currency on every row, and filters drag. What should be built?

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Set the table and column properties, including hidden keys and format strings
- C. Flatten the lookup attributes into a single dimension
- D. Build a star schema with a fact table and conformed dimensions

### 27. Authors keep dragging entity identifiers onto visuals, and amounts show inconsistent currencies. Which two actions fix that? Select two.

Domain: Model the data

- A. Hide technical columns from the report view
- B. Normalize the dimension into a snowflake
- C. Build a star schema with a fact table and conformed dimensions
- D. Flatten the lookup attributes into a single dimension
- E. Set the table and column properties, including hidden keys and format strings

### 28. A group model must be rebuilt from one consolidated export. Which sequence produces a model that lasts?

Domain: Model the data

- A. Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact
- B. Keep one wide table → relate it to itself → build measures
- C. Create a dimension per column → relate each one to the fact
- D. Build the relationships first → decide the grain afterwards → load

### 29. A region table sits between entity and fact, and every group filter crosses two hops. What should be done?

Domain: Model the data

- A. Set the table and column properties, including hidden keys and format strings
- B. Flatten the lookup attributes into a single dimension
- C. Build a star schema with a fact table and conformed dimensions
- D. Normalize the dimension into a snowflake

### 30. Posting date and reporting date both relate to the date table, but only one filters the group page. Why?

Domain: Model the data

- A. One-to-one relationship between two tables with the same grain
- B. Inactive relationship activated with USERELATIONSHIP
- C. One-to-many relationship from the dimension to the fact
- D. Single-direction filter from dimension to fact

### 31. Group cost centres serve many entities and entities use many cost centres, with an allocation table between them. Which relationship shape is required?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Many-to-many relationship with a bridging table
- C. Single-direction filter from dimension to fact
- D. One-to-one relationship between two tables with the same grain

### 32. The consolidated fact must filter from its dimensions and must never let one dimension filter another. Which two choices fit? Select two.

Domain: Model the data

- A. Many-to-many relationship with a bridging table
- B. Set the cross-filter direction on the relationship
- C. One-to-many relationship from the dimension to the fact
- D. Single-direction filter from dimension to fact
- E. Bi-directional cross-filtering on the relationship

### 33. An entity visual ignores a selection made in a consolidated visual, and the model is suspected. Which setting decides that?

Domain: Model the data

- A. Bi-directional cross-filtering on the relationship
- B. Set the cross-filter direction on the relationship
- C. Single-direction filter from dimension to fact
- D. Inactive relationship activated with USERELATIONSHIP

### 34. Rolling group totals skip days with no postings across any entity, and the running figure looks wrong. What is missing?

Domain: Model the data

- A. Build the fiscal periods as columns in the date table
- B. Create one date table and role-play it through several relationships
- C. Mark the table as a date table
- D. Create a dedicated date table marked as the date table

### 35. Posted, reported, and settled dates all need the same year-quarter-month logic. What should be used?

Domain: Model the data

- A. Mark the table as a date table
- B. Create a dedicated date table marked as the date table
- C. Create one date table and role-play it through several relationships
- D. Build the fiscal periods as columns in the date table

### 36. Two subsidiaries report on different year-ends, and the group reports on a June year. What must be added?

Domain: Model the data

- A. Create one date table and role-play it through several relationships
- B. Mark the table as a date table
- C. Create a dedicated date table marked as the date table
- D. Build the fiscal periods as columns in the date table

### 37. The group pack needs dependable year-to-date and prior-year figures. Which sequence delivers that?

Domain: Model the data

- A. Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it
- B. Create one date table per date column → relate all of them to the fact
- C. Create a date table → leave it unrelated → filter with it
- D. Use the fact date column directly → write TOTALYTD → add a date slicer

### 38. Group margin must respond to entity and period slicers without adding a stored column. What should be created?

Domain: Model the data

- A. Create a calculated column
- B. Create a calculated table
- C. Create a measure for the aggregation
- D. The filter context supplied by the visual, slicers, and page filters

### 39. A calculated column needs a value from a related mapping table, and the expression fails. What explains the failure?

Domain: Model the data

- A. Create a calculated table
- B. The row context inside an iterator
- C. The filter context supplied by the visual, slicers, and page filters
- D. Create a measure for the aggregation

### 40. A group needs a margin ratio that survives a zero denominator and revenue converted before summing. Which two functions fit? Select two.

Domain: Model the data

- A. Use an iterator such as SUMX over the row-level expression
- B. Use DIVIDE instead of the division operator
- C. Use DISTINCT COUNT for unique entities
- D. Use an iterator function for row-level arithmetic
- E. Create a measure for the aggregation

### 41. A measure must show each entity's share of group revenue while the visual lists entities. Which function changes the filter context?

Domain: Model the data

- A. Store intermediate results in VAR and RETURN
- B. Wrap the aggregation in CALCULATE to change the filter context
- C. Use ALL on the table to clear its filters
- D. Add KEEPFILTERS to intersect rather than replace the filter

### 42. A group share must stay inside the period the reader chose, whatever entity rows the visual displays. Which modifier fits?

Domain: Model the data

- A. Add KEEPFILTERS to intersect rather than replace the filter
- B. Use ALLSELECTED to respect the slicer but ignore the visual
- C. Remove the filter with REMOVEFILTERS or ALL
- D. Use ALL on the table to clear its filters

### 43. A group measure repeats the same filtered base three times and is hard to review. What should be used?

Domain: Model the data

- A. Store intermediate results in VAR and RETURN
- B. Wrap the aggregation in CALCULATE to change the filter context
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Use ALL on the table to clear its filters

### 44. A group share measure must compare each business with the whole group regardless of the business filter. Which function clears the table filter?

Domain: Model the data

- A. Use ALLSELECTED to respect the slicer but ignore the visual
- B. Use ALL on the table to clear its filters
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Remove the filter with REMOVEFILTERS or ALL

### 45. The group needs cumulative revenue from the start of its June year to the selected month. Which pattern fits?

Domain: Model the data

- A. Use AVERAGEX over a rolling date window
- B. Use TOTALYTD or DATESYTD for year-to-date
- C. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance

### 46. A group pack needs cumulative revenue and the same figure for the equivalent month last year. Which two patterns are required? Select two.

Domain: Model the data

- A. Use AVERAGEX over a rolling date window
- B. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- C. Use DATESINPERIOD for a windowed calculation
- D. Use TOTALYTD or DATESYTD for year-to-date
- E. Use LASTNONBLANK or LASTDATE for a semi-additive balance

### 47. The group standard requires month-to-date, quarter-to-date, and year-to-date for every measure. What should be used?

Domain: Model the data

- A. Create a calculation group for the time-intelligence variants
- B. Use a quick measure for the standard pattern
- C. Create a field parameter so the author can switch the measure or axis
- D. Create a numeric range parameter for scenario analysis

### 48. One group page must switch between revenue and margin and test a transfer-price assumption. Which two features fit? Select two.

Domain: Model the data

- A. Use a quick measure for the standard pattern
- B. Create a field parameter so the author can switch the measure or axis
- C. Create a numeric range parameter for scenario analysis
- D. Create a calculation group for the time-intelligence variants
- E. Use PERCENTILE.INC for a distribution boundary

### 49. A group page takes a minute, and the author must identify the slow visual. What should be used?

Domain: Model the data

- A. Run Performance Analyzer to find the slow visual
- B. Inspect the query plan in DAX query view
- C. Reduce the granularity loaded into the model
- D. Reduce column cardinality and width to shrink the VertiPaq store

### 50. A group model is dominated by a document identifier column nobody filters on. What should be done?

Domain: Model the data

- A. Add an aggregation table for the large fact
- B. Remove the high-cardinality columns the report does not use
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Remove unnecessary rows and columns before optimizing measures

### 51. A consolidated fact must stay at detail level but monthly summaries are slow. What should be added?

Domain: Model the data

- A. Remove unnecessary rows and columns before optimizing measures
- B. Add an aggregation table for the large fact
- C. Reduce the granularity loaded into the model
- D. Run Performance Analyzer to find the slow visual

### 52. A group page needs a monthly trend and progress against the annual target. Which two visuals fit? Select two.

Domain: Visualize and analyze the data

- A. A line chart with a date axis
- B. A KPI visual with a target
- C. A matrix visual with row and column groups
- D. A pie or donut chart
- E. A gauge visual

### 53. Forty product categories must be shown by contribution to group revenue. Which visual fits?

Domain: Visualize and analyze the data

- A. A treemap
- B. A pie or donut chart
- C. A waterfall chart
- D. A scatter chart

### 54. A group analyst must see whether marketing spend relates to revenue growth across businesses. Which visual fits?

Domain: Visualize and analyze the data

- A. A scatter chart
- B. A matrix visual with row and column groups
- C. A funnel chart
- D. A line chart with a date axis

### 55. Group readers need a visible control for choosing a business on the page. What should be added?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. A slicer on the report page
- C. Sync the slicer across the pages that share the same filter
- D. Set the filter pane scope by page, report, or visual

### 56. A chosen business must stay applied across eight group pages. What should be configured?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Set the filter pane scope by page, report, or visual
- C. Sync the slicer across the pages that share the same filter
- D. A slicer on the report page

### 57. A single filter must apply across all pages of the group report rather than the page in view. Where should it be placed?

Domain: Visualize and analyze the data

- A. A slicer on the report page
- B. Edit the interactions so the visual does not filter the others
- C. Set the filter pane scope by page, report, or visual
- D. Sync the slicer across the pages that share the same filter

### 58. Selecting a business on the page is filtering a fixed group commentary card. What should be changed?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Set the filter pane scope by page, report, or visual
- C. A slicer on the report page
- D. Sync the slicer across the pages that share the same filter

### 59. A group view and a business view share one page, and readers must switch between saved states. What should be captured?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Add buttons with actions that navigate or apply a bookmark
- C. Use the Selection pane to group and layer visuals
- D. Capture the view in a bookmark

### 60. Four visuals occupy two slots, and only two may be visible at a time. What should be used?

Domain: Visualize and analyze the data

- A. Capture the view in a bookmark
- B. Add a page navigator for the report
- C. Use the Selection pane to group and layer visuals
- D. Add buttons with actions that navigate or apply a bookmark

### 61. A group page needs three saved views, each reachable from a button. Which sequence works?

Domain: Visualize and analyze the data

- A. Create a page per view → duplicate the visuals → maintain each page
- B. Capture a bookmark before setting the filters → expect it to restore them
- C. Create the views → capture each in a bookmark → add buttons → hide the visuals not in use
- D. Use buttons without actions → tell readers to click twice

### 62. The group report will reach twenty pages and needs navigation that stays current. What should be used?

Domain: Visualize and analyze the data

- A. Capture the view in a bookmark
- B. Add a page navigator for the report
- C. Add buttons with actions that navigate or apply a bookmark
- D. Use the Selection pane to group and layer visuals

### 63. A reader must click a business and open a detail page about that business. What should be configured?

Domain: Visualize and analyze the data

- A. Enable drill-down through the hierarchy
- B. Edit the interactions so the visual does not filter the others
- C. Configure a drillthrough page with the entity filter
- D. Set the filter pane scope by page, report, or visual

### 64. A hover must show revenue, margin, and headcount together without adding visuals. Which two actions deliver that? Select two.

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Set the tooltip to a report page and size it to the hover area
- C. Configure a drillthrough page with the entity filter
- D. Build a custom tooltip page
- E. Enable drill-down through the hierarchy

### 65. A group team is building its first drillthrough page. Which sequence works?

Domain: Visualize and analyze the data

- A. Choose the entity field → create the drillthrough page → place the entity filter → add a back button
- B. Create the detail page → add a visual → tell readers to filter it manually
- C. Set the drillthrough filter → publish → skip the back button
- D. Put every field on the summary visual → expect drillthrough to work

### 66. A chart must let a reader descend from group to business to cost centre without leaving the visual. What should be enabled?

Domain: Visualize and analyze the data

- A. Build a custom tooltip page
- B. Edit the interactions so the visual does not filter the others
- C. Configure a drillthrough page with the entity filter
- D. Enable drill-down through the hierarchy

### 67. The group report must be usable by screen-reader users, and its visuals carry no descriptions. What must be added?

Domain: Visualize and analyze the data

- A. Provide alt text for each meaningful visual
- B. Build the mobile layout in the mobile view
- C. Enable personalization for the visuals the reader may change
- D. Set a logical tab order for the interactive elements

### 68. Group executives will open the report on a phone and need two measures first. What should be built?

Domain: Visualize and analyze the data

- A. Configure the export and download settings for the report
- B. Enable personalization for the visuals the reader may change
- C. Provide alt text for each meaningful visual
- D. Build the mobile layout in the mobile view

### 69. Every group page must share one palette and font without individual styling. What should be applied?

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Use the Selection pane to group and layer visuals
- C. Apply conditional formatting driven by a measure
- D. Turn on and format data labels

### 70. A table must colour businesses whose margin falls below the group floor. What should be applied?

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Set the axis range and units explicitly
- C. Use the Selection pane to group and layer visuals
- D. Apply conditional formatting driven by a measure

### 71. A bar axis must not exaggerate small differences, and a six-bar chart must show exact values. Which two settings are required? Select two.

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Apply a report theme JSON
- C. Turn on and format data labels
- D. Set the axis range and units explicitly
- E. Apply conditional formatting driven by a measure

### 72. A stable group revenue series must be projected two quarters ahead with a confidence band. What should be used?

Domain: Visualize and analyze the data

- A. Create bins for a continuous measure
- B. Use the built-in forecast on a line chart
- C. Add a reference line for the target or average
- D. Use clustering to find segments in the data

### 73. A group series contains a few points far from the pattern, and the analyst wants them surfaced. What should be used?

Domain: Visualize and analyze the data

- A. Add error bars to show the uncertainty range
- B. Use the outlier detection feature on the visual
- C. Add a reference line for the target or average
- D. Use the Analyze feature to explain a change

### 74. A group root-cause page must explore any dimension in any order. Which visual fits?

Domain: Visualize and analyze the data

- A. Use Q&A to answer a natural-language question
- B. Use Copilot to suggest a report page
- C. Use the Key Influencers visual
- D. Use the Decomposition Tree visual

### 75. The group wants the factors associated with churn and a written summary for the board. Which two features fit? Select two.

Domain: Visualize and analyze the data

- A. Use the Decomposition Tree visual
- B. Use Q&A to answer a natural-language question
- C. Use Copilot to create a narrative visual
- D. Use Copilot to suggest a report page
- E. Use the Key Influencers visual

### 76. A group author wants a first-draft page from a written prompt before building it manually. Which feature fits?

Domain: Visualize and analyze the data

- A. Use Copilot to suggest a report page
- B. Use the Key Influencers visual
- C. Use Copilot to create a narrative visual
- D. Use Q&A to answer a natural-language question

### 77. Each business needs one place where its analysts collaborate on shared content. What should be created?

Domain: Manage and secure Power BI

- A. Publish an app from the workspace
- B. Workspace Admin role
- C. Create a workspace for the team that owns the content
- D. Workspace Viewer role

### 78. Group executives must read the reports but must not change them. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Admin role
- B. Workspace Contributor role
- C. Workspace Viewer role
- D. Workspace Member role

### 79. The group platform lead must manage membership, and a business analyst must publish and add viewers. Which two roles cover that? Select two.

Domain: Manage and secure Power BI

- A. Workspace Viewer role
- B. Publish an app from the workspace
- C. Workspace Contributor role
- D. Workspace Admin role
- E. Workspace Member role

### 80. One group app must show business pages to each business and consolidated pages to the board. What should be configured?

Domain: Manage and secure Power BI

- A. Publish an app from the workspace
- B. Choose the distribution method that matches the audience
- C. Define an app audience for each group of consumers
- D. Update the app after changing the workspace content

### 81. The group is publishing its first app to four audiences. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Publish the app before the report is finished → update it never
- B. Create one app per person → assign each audience manually
- C. Give every consumer the workspace Viewer role → skip the app
- D. Build in the workspace → curate the app pages → assign audiences → publish and update the app

### 82. A fix was published to the workspace, yet business users still see the earlier version. What was missed?

Domain: Manage and secure Power BI

- A. Update the app after changing the workspace content
- B. Publish an app from the workspace
- C. Define an app audience for each group of consumers
- D. Choose the distribution method that matches the audience

### 83. The group board wants one page of pinned metrics from four business reports. What should be created?

Domain: Manage and secure Power BI

- A. Create a data alert on a dashboard tile
- B. Create a subscription for the report or dashboard
- C. Pin the visual to a dashboard tile
- D. Create a dashboard in the service

### 84. A group treasurer must be notified when consolidated cash falls below a floor. What should be created?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Set the alert threshold on the pinned card tile
- C. Create a data alert on a dashboard tile
- D. Pin the visual to a dashboard tile

### 85. A five-year consolidated fact must refresh inside a short window, and only the recent period changes. Which two steps are required? Select two.

Domain: Manage and secure Power BI

- A. Install an on-premises data gateway
- B. Configure scheduled refresh on the semantic model
- C. Configure incremental refresh with the range parameters
- D. Set the RangeStart and RangeEnd parameters the refresh policy expects
- E. Update the credentials used by the refresh schedule

### 86. The group is moving its largest fact to incremental refresh. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Load all history every refresh → add a policy later → hope it rebuilds
- B. Filter the query by date → set the policy → skip the parameters
- C. Configure the policy in Desktop → publish → assume partitions were created
- D. Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh

### 87. A role is written, and the team must confirm what a business user actually sees before release. What should be used?

Domain: Manage and secure Power BI

- A. Test the role with View as role in the service
- B. Use a dynamic RLS rule based on USERPRINCIPALNAME
- C. Define a row-level security role with a DAX filter
- D. Add the security group to the role membership

### 88. Group financial data must stay protected after a report is exported. What should be applied?

Domain: Manage and secure Power BI

- A. Grant item-level access to the specific report
- B. Apply a sensitivity label to the semantic model and report
- C. Promote the content as endorsed
- D. Certify the semantic model

---

## Case study — Atlas Holdings

Atlas Holdings is a group of four businesses with different ERPs and one group data office. The group analyst must report across all four using the model the data office certifies, because a second definition of group revenue is not acceptable. A newly acquired business has just supplied its first extract, and nobody has inspected it. Subsidiary transactions arrive at line level, but the consolidation needs one row per entity per month before it is loaded.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. The group analyst must report across four businesses using the model the data office certifies. What should the analyst do?

Domain: Prepare the data

- A. DirectQuery
- B. Import mode
- C. Connect to a shared semantic model instead of importing the source again
- D. DirectLake over a lakehouse

### 90. A newly acquired business supplies an extract nobody has inspected, and its quality is unknown. What should be done first?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Review column statistics and value distribution
- D. Profile the column with column quality, distribution, and profile views

### 91. Subsidiary transaction rows must become one row per entity per month before loading. What should be used?

Domain: Prepare the data

- A. Add a conditional column for rule-based bucketing
- B. Add an aggregate step with the correct summarization
- C. Group by the key and aggregate the measures
- D. Add a custom column with an M expression

---

## Case study — Beacon Mutual

Beacon Mutual is a mutual insurer reporting group reserves, claims, and policy data. Group reserve balances are captured at a point in time, and the current pack sums them across months into a meaningless peak. The claims desk must publish the settlement time below which 90 percent of claims close, not an average that hides the tail. Policy data is restricted: readers outside the actuarial function must not be able to download it from the report.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Group reserve balances are being summed across months and producing a meaningless peak. What should the measure do?

Domain: Model the data

- A. Use TOTALYTD or DATESYTD for year-to-date
- B. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- C. Use AVERAGEX over a rolling date window
- D. Use LASTNONBLANK when the balance is only recorded on some dates

### 93. The claims desk must state the settlement time below which 90 percent of claims close. What should be used?

Domain: Model the data

- A. Use a statistical function such as STDEV.P or MEDIAN to describe the spread
- B. Use PERCENTILE.INC for a distribution boundary
- C. Create a calculation group for the time-intelligence variants
- D. Use a quick measure for the standard pattern

### 94. Policy data must not be downloaded by readers outside the actuarial function. What should be configured?

Domain: Visualize and analyze the data

- A. Provide alt text for each meaningful visual
- B. Enable personalization for the visuals the reader may change
- C. Configure the export and download settings for the report
- D. Build the mobile layout in the mobile view

---

## Case study — Cedarline Foods

Cedarline Foods reports volume and revenue for four regional businesses and a group board. The board must compare revenue across the regions, and the current chart mixes two measures on one axis. Each region is measured against a volume plan, and the monthly chart has to show whether the plan was beaten without a second visual. The commercial director wants the volume pack as an email snapshot on the first working day of the month.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. The board must compare revenue across its four regional businesses. Which visual fits?

Domain: Visualize and analyze the data

- A. A line chart with a date axis
- B. A pie or donut chart
- C. A treemap
- D. A clustered bar or column chart

### 96. A monthly chart must show whether each region beat its volume plan. What should be added?

Domain: Visualize and analyze the data

- A. Add a reference line for the target or average
- B. Use the built-in forecast on a line chart
- C. Create groups for the categories that matter
- D. Add error bars to show the uncertainty range

### 97. The commercial director wants the volume pack as an email snapshot on the first working day. What should be configured?

Domain: Manage and secure Power BI

- A. Set the alert threshold on the pinned card tile
- B. Create a data alert on a dashboard tile
- C. Pin the visual to a dashboard tile
- D. Create a subscription for the report or dashboard

---

## Case study — Pinnacle Services

Pinnacle Services is a professional services group with two business units that both keep their practice management system on premises. The service cannot reach either system directly, and refresh has to run overnight for both. Eight hundred consultants must see only their own engagements, and the mapping between person and engagement changes with every new project. The group wants one engagement model certified so that every business unit reports margin the same way.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Two business units keep their practice system on-premises and the service cannot reach either. What is required?

Domain: Manage and secure Power BI

- A. Configure scheduled refresh on the semantic model
- B. Personal mode gateway
- C. Install an on-premises data gateway
- D. Virtual network data gateway

### 99. Eight hundred consultants must be filtered by a mapping table rather than a role per person. What should be used?

Domain: Manage and secure Power BI

- A. Map the signed-in user with USERPRINCIPALNAME in the filter
- B. Use a dynamic RLS rule based on USERPRINCIPALNAME
- C. Define a row-level security role with a DAX filter
- D. A static RLS role per region with fixed members

### 100. The group wants one engagement model to become the standard every business can trust. What should be done?

Domain: Manage and secure Power BI

- A. Grant item-level access to the specific report
- B. Grant Build permission on the semantic model
- C. Promote the content as endorsed
- D. Certify the semantic model

---

## Answer key and explanations

### Question 1 — C

Answer: Import mode. Import serves the volume from memory and protects the source. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Import serves the volume from memory and protects the source.
- **B:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import serves the volume from memory and protects the source.
- **C:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import serves the volume from memory and protects the source.
- **D:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import serves the volume from memory and protects the source.

### Question 2 — A, D

Answers: DirectQuery; Connect to a shared semantic model instead of importing the source again. Live status needs DirectQuery, and governed definitions come from the certified shared model. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: Live status needs DirectQuery, and governed definitions come from the certified shared model.
- **B:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Live status needs DirectQuery, and governed definitions come from the certified shared model.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Live status needs DirectQuery, and governed definitions come from the certified shared model.
- **D:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Live status needs DirectQuery, and governed definitions come from the certified shared model.
- **E:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Live status needs DirectQuery, and governed definitions come from the certified shared model.

### Question 3 — B

Answer: DirectLake over a lakehouse. DirectLake reads Delta tables directly when capacity and format allow it. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.
- **B:** Correct. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. In this case: DirectLake reads Delta tables directly when capacity and format allow it.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.

### Question 4 — C

Answer: Dual mode table. A Dual table can answer some queries from memory instead of the source. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.
- **B:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.
- **C:** Correct. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. In this case: A Dual table can answer some queries from memory instead of the source.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.

### Question 5 — D

Answer: DirectQuery. DirectQuery leaves the data in the source and reads it at query time. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.
- **B:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.
- **C:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.
- **D:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery leaves the data in the source and reads it at query time.

### Question 6 — A

Answer: Import mode. Import moves the analytical load off the busy source. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import moves the analytical load off the busy source.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Import moves the analytical load off the busy source.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import moves the analytical load off the busy source.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import moves the analytical load off the busy source.

### Question 7 — C

Answer: Create a parameter for the server, path, or filter. A parameter swaps the environment without editing the M code. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **B:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **C:** Correct. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. In this case: A parameter swaps the environment without editing the M code.
- **D:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: A parameter swaps the environment without editing the M code.

### Question 8 — C

Answer: Set privacy levels to isolate the sources. Privacy levels stop values being combined across sources that must stay separate. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **B:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **C:** Correct. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. In this case: Privacy levels stop values being combined across sources that must stay separate.
- **D:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.

### Question 9 — A

Answer: Update the data source credentials in the semantic model settings. The stored credential in the data source settings is what refresh uses. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. In this case: The stored credential in the data source settings is what refresh uses.
- **B:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **C:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **D:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.

### Question 10 — D

Answer: Correct the column data type before building the model. A numeric value stored as text cannot be aggregated, so the type must be fixed. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **C:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **D:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: A numeric value stored as text cannot be aggregated, so the type must be fixed.

### Question 11 — C

Answer: Review column statistics and value distribution. Value distribution shows whether the measure is concentrated in a few members. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **B:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **C:** Correct. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. In this case: Value distribution shows whether the measure is concentrated in a few members.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.

### Question 12 — B

Answer: Profile the source → fix types and nulls → shape the table → load only the needed columns. Profiling comes first, shaping follows, and loading only needed columns keeps the model small. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Deleting profiling removes the evidence of quality problems and loading every column inflates the model. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **B:** Correct. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. In this case: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **C:** Incorrect for this question. Discovering type errors after load means the model was built on wrong data and the work restarts. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **D:** Incorrect for this question. Patching visuals hides the data problem instead of fixing it at the source. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.

### Question 13 — A

Answer: Remove duplicate rows using the natural business key. The same business key is being loaded twice, so de-duplicating on that key reverses the inflation. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **C:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **D:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.

### Question 14 — B, C

Answers: Trim, clean, and standardize the text values; Filter out the error rows and report them separately. Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving.
- **B:** Correct. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. In this case: Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving.
- **C:** Correct. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. In this case: Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving.
- **E:** Incorrect for this question. A locale-aware conversion stops day and month being swapped and stops decimal commas being interpreted as text. Why the correct answer wins: Standardizing text collapses duplicate members, and filtering the failing rows with a report keeps the load moving.

### Question 15 — D

Answer: Replace nulls with a defined placeholder or a filled-down value. Replacing blank with a defined value, or excluding it deliberately, keeps the average stable and documented. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Replacing blank with a defined value, or excluding it deliberately, keeps the average stable and documented.
- **B:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Replacing blank with a defined value, or excluding it deliberately, keeps the average stable and documented.
- **C:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Replacing blank with a defined value, or excluding it deliberately, keeps the average stable and documented.
- **D:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: Replacing blank with a defined value, or excluding it deliberately, keeps the average stable and documented.

### Question 16 — A

Answer: Identify the bad values → standardize text → convert types → document what was replaced. Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. In this case: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **B:** Incorrect for this question. Replacing everything with a default destroys real values and hides the pattern behind the error. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **C:** Incorrect for this question. Converting before trimming fails on values that only differ by whitespace and leaves duplicates behind. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **D:** Incorrect for this question. Silently dropping rows changes the totals and the business never learns what is missing. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.

### Question 17 — D

Answer: Add a custom column with an M expression. A custom column concatenates the fields row by row. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: A custom column concatenates the fields row by row.
- **B:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A custom column concatenates the fields row by row.
- **C:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: A custom column concatenates the fields row by row.
- **D:** Correct. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. In this case: A custom column concatenates the fields row by row.

### Question 18 — A, C

Answers: Correct the column data type before building the model; Add an aggregate step with the correct summarization. Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up.
- **B:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up.
- **C:** Correct. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. In this case: Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up.
- **D:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up.
- **E:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Converting the type makes the value measurable, and choosing sum as the aggregation produces the roll-up.

### Question 19 — D

Answer: Add a conditional column for rule-based bucketing. A conditional column applies the policy explicitly and is easy to review. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A conditional column applies the policy explicitly and is easy to review.
- **B:** Incorrect for this question. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Why the correct answer wins: A conditional column applies the policy explicitly and is easy to review.
- **C:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: A conditional column applies the policy explicitly and is easy to review.
- **D:** Correct. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. In this case: A conditional column applies the policy explicitly and is easy to review.

### Question 20 — A

Answer: Unpivot the month columns into rows. Unpivoting turns the entity columns into rows. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. In this case: Unpivoting turns the entity columns into rows.
- **B:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Unpivoting turns the entity columns into rows.
- **C:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Unpivoting turns the entity columns into rows.
- **D:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Unpivoting turns the entity columns into rows.

### Question 21 — C

Answer: Convert the XML or JSON list into a table of rows. Converting the XML elements to a table makes each entry addressable. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Converting the XML elements to a table makes each entry addressable.
- **B:** Incorrect for this question. Converting a list to a table preserves every element as a row instead of keeping only the first value. Why the correct answer wins: Converting the XML elements to a table makes each entry addressable.
- **C:** Correct. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. In this case: Converting the XML elements to a table makes each entry addressable.
- **D:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Converting the XML elements to a table makes each entry addressable.

### Question 22 — D

Answer: Expand the JSON record into typed columns. Expanding the record exposes the nested fields as columns. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Expanding the record exposes the nested fields as columns.
- **B:** Incorrect for this question. Converting a list to a table preserves every element as a row instead of keeping only the first value. Why the correct answer wins: Expanding the record exposes the nested fields as columns.
- **C:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Expanding the record exposes the nested fields as columns.
- **D:** Correct. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. In this case: Expanding the record exposes the nested fields as columns.

### Question 23 — A

Answer: Append the queries into one table. Appending stacks rows of the same shape. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. In this case: Appending stacks rows of the same shape.
- **B:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: Appending stacks rows of the same shape.
- **C:** Incorrect for this question. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. Why the correct answer wins: Appending stacks rows of the same shape.
- **D:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: Appending stacks rows of the same shape.

### Question 24 — A, C

Answers: Merge the two queries on a matching key; Use a left outer join to keep every fact row. A merge adds the mapping, and a left outer join keeps unmatched rows visible. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. In this case: A merge adds the mapping, and a left outer join keeps unmatched rows visible.
- **B:** Incorrect for this question. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Why the correct answer wins: A merge adds the mapping, and a left outer join keeps unmatched rows visible.
- **C:** Correct. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. In this case: A merge adds the mapping, and a left outer join keeps unmatched rows visible.
- **D:** Incorrect for this question. A single integer key is compact, stable, and avoids relationships built on text or composite columns. Why the correct answer wins: A merge adds the mapping, and a left outer join keeps unmatched rows visible.
- **E:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: A merge adds the mapping, and a left outer join keeps unmatched rows visible.

### Question 25 — A, D

Answers: Keep the steps foldable so the source does the work; Reuse a dataflow for the shared transformation. A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **B:** Incorrect for this question. A native query reduces what is transferred, but it can break folding for later steps and must be maintained as the schema changes. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **C:** Incorrect for this question. A duplicate copies the full step chain, so a change in one copy does not affect the other but the work is repeated. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **D:** Correct. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **E:** Incorrect for this question. Staging separates extraction from transformation, which makes each layer easier to test and reuse. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.

### Question 26 — D

Answer: Build a star schema with a fact table and conformed dimensions. A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **B:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **C:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **D:** Correct. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. In this case: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.

### Question 27 — A, E

Answers: Hide technical columns from the report view; Set the table and column properties, including hidden keys and format strings. Hiding identifiers removes them from the field list, and format strings fix how values display. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **B:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **C:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **D:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **E:** Correct. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.

### Question 28 — A

Answer: Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact. Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. In this case: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **B:** Incorrect for this question. A single wide table cannot be filtered cleanly by dimension and pushes duplication into every row. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **C:** Incorrect for this question. A dimension per column produces a hub of one-column tables and makes the model unmaintainable. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **D:** Incorrect for this question. Relationships built before the grain is agreed will be wrong and must be rebuilt. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.

### Question 29 — B

Answer: Flatten the lookup attributes into a single dimension. Flattening the region attributes into the entity dimension removes the hop. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: Flattening the region attributes into the entity dimension removes the hop.
- **B:** Correct. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. In this case: Flattening the region attributes into the entity dimension removes the hop.
- **C:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Flattening the region attributes into the entity dimension removes the hop.
- **D:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Flattening the region attributes into the entity dimension removes the hop.

### Question 30 — B

Answer: Inactive relationship activated with USERELATIONSHIP. Only one relationship can be active, so the second waits until a measure activates it. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **B:** Correct. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. In this case: Only one relationship can be active, so the second waits until a measure activates it.
- **C:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **D:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.

### Question 31 — B

Answer: Many-to-many relationship with a bridging table. The allocation bridge resolves the many-to-many and keeps the path explicit. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: The allocation bridge resolves the many-to-many and keeps the path explicit.
- **B:** Correct. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. In this case: The allocation bridge resolves the many-to-many and keeps the path explicit.
- **C:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: The allocation bridge resolves the many-to-many and keeps the path explicit.
- **D:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: The allocation bridge resolves the many-to-many and keeps the path explicit.

### Question 32 — C, D

Answers: Single-direction filter from dimension to fact; One-to-many relationship from the dimension to the fact. Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **B:** Incorrect for this question. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **C:** Correct. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **D:** Correct. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **E:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.

### Question 33 — B

Answer: Set the cross-filter direction on the relationship. Cross-filter direction decides whether the fact can filter the dimension. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **B:** Correct. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. In this case: Cross-filter direction decides whether the fact can filter the dimension.
- **C:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **D:** Incorrect for this question. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.

### Question 34 — D

Answer: Create a dedicated date table marked as the date table. A contiguous date table supplies every date so accumulation does not skip gaps. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **B:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **C:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **D:** Correct. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. In this case: A contiguous date table supplies every date so accumulation does not skip gaps.

### Question 35 — C

Answer: Create one date table and role-play it through several relationships. One date table related three times through role-playing dimensions avoids duplicate tables. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate tables.
- **B:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate tables.
- **C:** Correct. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. In this case: One date table related three times through role-playing dimensions avoids duplicate tables.
- **D:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate tables.

### Question 36 — D

Answer: Build the fiscal periods as columns in the date table. Fiscal period columns let time intelligence follow the group's year while preserving local reporting. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Fiscal period columns let time intelligence follow the group's year while preserving local reporting.
- **B:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: Fiscal period columns let time intelligence follow the group's year while preserving local reporting.
- **C:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Fiscal period columns let time intelligence follow the group's year while preserving local reporting.
- **D:** Correct. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. In this case: Fiscal period columns let time intelligence follow the group's year while preserving local reporting.

### Question 37 — A

Answer: Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it. Marking and relating the date table is what makes the measures obey the date slicer. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. In this case: Marking and relating the date table is what makes the measures obey the date slicer.
- **B:** Incorrect for this question. Several date tables multiply relationships and make every time measure ambiguous. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **C:** Incorrect for this question. An unrelated date table filters nothing, so the slicer appears to work while the visuals ignore it. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **D:** Incorrect for this question. A fact date column has gaps, so year-to-date silently skips missing days and the slicer shows no clean hierarchy. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.

### Question 38 — C

Answer: Create a measure for the aggregation. A measure is evaluated in the filter context the visual supplies. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **B:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **C:** Correct. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. In this case: A measure is evaluated in the filter context the visual supplies.
- **D:** Incorrect for this question. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.

### Question 39 — B

Answer: The row context inside an iterator. Row context exists in a calculated column, and RELATED is needed to reach the related table. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: Row context exists in a calculated column, and RELATED is needed to reach the related table.
- **B:** Correct. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. In this case: Row context exists in a calculated column, and RELATED is needed to reach the related table.
- **C:** Incorrect for this question. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Why the correct answer wins: Row context exists in a calculated column, and RELATED is needed to reach the related table.
- **D:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: Row context exists in a calculated column, and RELATED is needed to reach the related table.

### Question 40 — A, B

Answers: Use DIVIDE instead of the division operator; Use an iterator such as SUMX over the row-level expression. DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. In this case: DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating.
- **B:** Correct. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. In this case: DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating.
- **C:** Incorrect for this question. Distinct count answers how many unique customers or orders, which a plain count would overstate. Why the correct answer wins: DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating.
- **D:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating.
- **E:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: DIVIDE avoids a division error, and SUMX evaluates conversion row by row before aggregating.

### Question 41 — B

Answer: Wrap the aggregation in CALCULATE to change the filter context. CALCULATE evaluates the expression under modified filters. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **B:** Correct. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. In this case: CALCULATE evaluates the expression under modified filters.
- **C:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **D:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.

### Question 42 — B

Answer: Use ALLSELECTED to respect the slicer but ignore the visual. ALLSELECTED respects the reader's selection while removing the visual's grouping. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **B:** Correct. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. In this case: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **C:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **D:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.

### Question 43 — A

Answer: Store intermediate results in VAR and RETURN. Variables compute the expression once and make the measure readable. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. In this case: Variables compute the expression once and make the measure readable.
- **B:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **D:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: Variables compute the expression once and make the measure readable.

### Question 44 — B

Answer: Use ALL on the table to clear its filters. ALL clears filters from the table, which is the basis for a share-of-total denominator. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: ALL clears filters from the table, which is the basis for a share-of-total denominator.
- **B:** Correct. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. In this case: ALL clears filters from the table, which is the basis for a share-of-total denominator.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALL clears filters from the table, which is the basis for a share-of-total denominator.
- **D:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALL clears filters from the table, which is the basis for a share-of-total denominator.

### Question 45 — B

Answer: Use TOTALYTD or DATESYTD for year-to-date. Year-to-date accumulates from the start of the year defined by the marked date table. Year-to-date functions accumulate from the start of the year defined by the marked date table. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **B:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date accumulates from the start of the year defined by the marked date table.
- **C:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **D:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.

### Question 46 — B, D

Answers: Use TOTALYTD or DATESYTD for year-to-date; Use SAMEPERIODLASTYEAR or DATEADD for the comparable period. Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value. Year-to-date functions accumulate from the start of the year defined by the marked date table. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **B:** Correct. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. In this case: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **C:** Incorrect for this question. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **D:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **E:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.

### Question 47 — A

Answer: Create a calculation group for the time-intelligence variants. A calculation group applies the variants to every measure instead of triplicating them. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. In this case: A calculation group applies the variants to every measure instead of triplicating them.
- **B:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A calculation group applies the variants to every measure instead of triplicating them.
- **C:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A calculation group applies the variants to every measure instead of triplicating them.
- **D:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A calculation group applies the variants to every measure instead of triplicating them.

### Question 48 — B, C

Answers: Create a field parameter so the author can switch the measure or axis; Create a numeric range parameter for scenario analysis. A field parameter switches the measure in place, and a numeric range parameter drives the assumption. A field parameter lets one visual switch between measures or dimensions without duplicating pages. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **B:** Correct. A field parameter lets one visual switch between measures or dimensions without duplicating pages. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **C:** Correct. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **D:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **E:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.

### Question 49 — A

Answer: Run Performance Analyzer to find the slow visual. Performance Analyzer times each visual and separates DAX, query, and rendering cost. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. In this case: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **B:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **C:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **D:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.

### Question 50 — B

Answer: Remove the high-cardinality columns the report does not use. A column with almost unique values compresses badly and can dominate model size. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: A column with almost unique values compresses badly and can dominate model size.
- **B:** Correct. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. In this case: A column with almost unique values compresses badly and can dominate model size.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: A column with almost unique values compresses badly and can dominate model size.
- **D:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: A column with almost unique values compresses badly and can dominate model size.

### Question 51 — B

Answer: Add an aggregation table for the large fact. An aggregation table answers common summaries quickly while detail stays available. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: An aggregation table answers common summaries quickly while detail stays available.
- **B:** Correct. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. In this case: An aggregation table answers common summaries quickly while detail stays available.
- **C:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: An aggregation table answers common summaries quickly while detail stays available.
- **D:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: An aggregation table answers common summaries quickly while detail stays available.

### Question 52 — A, B

Answers: A line chart with a date axis; A KPI visual with a target. A line chart shows the trend, and a KPI visual shows progress against a target. A line chart shows a trend over a continuous axis, which is what time series need. A KPI visual states progress against a defined target, which a plain card cannot show. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A line chart shows a trend over a continuous axis, which is what time series need. In this case: A line chart shows the trend, and a KPI visual shows progress against a target.
- **B:** Correct. A KPI visual states progress against a defined target, which a plain card cannot show. In this case: A line chart shows the trend, and a KPI visual shows progress against a target.
- **C:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.
- **D:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.
- **E:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.

### Question 53 — A

Answer: A treemap. A treemap shows part-to-whole through area, which suits many categories. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. In this case: A treemap shows part-to-whole through area, which suits many categories.
- **B:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A treemap shows part-to-whole through area, which suits many categories.
- **C:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A treemap shows part-to-whole through area, which suits many categories.
- **D:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A treemap shows part-to-whole through area, which suits many categories.

### Question 54 — A

Answer: A scatter chart. A scatter plot shows the relationship between two numeric measures. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. In this case: A scatter plot shows the relationship between two numeric measures.
- **B:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.
- **C:** Incorrect for this question. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.
- **D:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.

### Question 55 — B

Answer: A slicer on the report page. A slicer puts the control on the canvas. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: A slicer puts the control on the canvas.
- **B:** Correct. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. In this case: A slicer puts the control on the canvas.
- **C:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: A slicer puts the control on the canvas.
- **D:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: A slicer puts the control on the canvas.

### Question 56 — C

Answer: Sync the slicer across the pages that share the same filter. Syncing the slicer keeps one selection consistent across pages. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **C:** Correct. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. In this case: Syncing the slicer keeps one selection consistent across pages.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.

### Question 57 — C

Answer: Set the filter pane scope by page, report, or visual. Filter scope decides whether a filter applies to a visual, a page, or the whole report. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **C:** Correct. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. In this case: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **D:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.

### Question 58 — A

Answer: Edit the interactions so the visual does not filter the others. Interaction settings decide whether a selection filters, highlights, or does nothing. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. In this case: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **C:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **D:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.

### Question 59 — D

Answer: Capture the view in a bookmark. A bookmark stores filter and visibility state. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: A bookmark stores filter and visibility state.
- **B:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A bookmark stores filter and visibility state.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A bookmark stores filter and visibility state.
- **D:** Correct. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. In this case: A bookmark stores filter and visibility state.

### Question 60 — C

Answer: Use the Selection pane to group and layer visuals. The Selection pane controls visibility and z-order. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: The Selection pane controls visibility and z-order.
- **B:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: The Selection pane controls visibility and z-order.
- **C:** Correct. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. In this case: The Selection pane controls visibility and z-order.
- **D:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: The Selection pane controls visibility and z-order.

### Question 61 — C

Answer: Create the views → capture each in a bookmark → add buttons → hide the visuals not in use. Bookmarks store state and buttons apply it. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Duplicating pages multiplies maintenance and the copies drift apart. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **B:** Incorrect for this question. A bookmark captures the state at the moment it is created, so filters set afterwards are not stored. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **C:** Correct. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. In this case: Bookmarks store state and buttons apply it.
- **D:** Incorrect for this question. A button with no action is decoration and the report still has no navigation. Why the correct answer wins: Bookmarks store state and buttons apply it.

### Question 62 — B

Answer: Add a page navigator for the report. A page navigator generates navigation from the pages themselves. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **B:** Correct. A page navigator generates navigation for every page automatically, which stays correct as pages are added. In this case: A page navigator generates navigation from the pages themselves.
- **C:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A page navigator generates navigation from the pages themselves.

### Question 63 — C

Answer: Configure a drillthrough page with the entity filter. Drillthrough passes the selected entity to a detail page through a filter. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **C:** Correct. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. In this case: Drillthrough passes the selected entity to a detail page through a filter.
- **D:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.

### Question 64 — B, D

Answers: Build a custom tooltip page; Set the tooltip to a report page and size it to the hover area. A tooltip page holds the extra measures, and the report-page tooltip setting displays it. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **B:** Correct. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **C:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **D:** Correct. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **E:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.

### Question 65 — A

Answer: Choose the entity field → create the drillthrough page → place the entity filter → add a back button. The drillthrough filter carries the selection, and the back button keeps the reader oriented. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. In this case: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **B:** Incorrect for this question. A page without the drillthrough filter does not carry the selected entity, so the detail is not about what was clicked. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **C:** Incorrect for this question. Without a back button the reader is stranded on the detail page and loses the summary context. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **D:** Incorrect for this question. Too many fields on one visual makes the click target ambiguous and the drill result unpredictable. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.

### Question 66 — D

Answer: Enable drill-down through the hierarchy. Drill-down moves through the hierarchy inside the same visual. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **C:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **D:** Correct. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. In this case: Drill-down moves through the hierarchy inside the same visual.

### Question 67 — A

Answer: Provide alt text for each meaningful visual. Alt text describes each visual for a screen reader. Alt text describes the visual for a screen reader, which is required for an accessible report. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Alt text describes the visual for a screen reader, which is required for an accessible report. In this case: Alt text describes each visual for a screen reader.
- **B:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **C:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **D:** Incorrect for this question. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Why the correct answer wins: Alt text describes each visual for a screen reader.

### Question 68 — D

Answer: Build the mobile layout in the mobile view. The mobile layout decides what appears first on a phone. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **B:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **C:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **D:** Correct. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. In this case: The mobile layout decides what appears first on a phone.

### Question 69 — A

Answer: Apply a report theme JSON. A theme applies a consistent palette across the report. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. In this case: A theme applies a consistent palette across the report.
- **B:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A theme applies a consistent palette across the report.
- **C:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: A theme applies a consistent palette across the report.
- **D:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: A theme applies a consistent palette across the report.

### Question 70 — D

Answer: Apply conditional formatting driven by a measure. Conditional formatting driven by a measure encodes the exception. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.
- **B:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.
- **D:** Correct. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. In this case: Conditional formatting driven by a measure encodes the exception.

### Question 71 — C, D

Answers: Set the axis range and units explicitly; Turn on and format data labels. An explicit axis range prevents exaggeration, and data labels remove the need to read the axis. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: An explicit axis range prevents exaggeration, and data labels remove the need to read the axis.
- **B:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: An explicit axis range prevents exaggeration, and data labels remove the need to read the axis.
- **C:** Correct. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. In this case: An explicit axis range prevents exaggeration, and data labels remove the need to read the axis.
- **D:** Correct. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. In this case: An explicit axis range prevents exaggeration, and data labels remove the need to read the axis.
- **E:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: An explicit axis range prevents exaggeration, and data labels remove the need to read the axis.

### Question 72 — B

Answer: Use the built-in forecast on a line chart. Forecasting extends the series statistically with a confidence band. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Binning turns a continuous value into ranges, which is how a distribution becomes readable. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.
- **B:** Correct. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. In this case: Forecasting extends the series statistically with a confidence band.
- **C:** Incorrect for this question. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.
- **D:** Incorrect for this question. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.

### Question 73 — B

Answer: Use the outlier detection feature on the visual. Outlier detection finds points that sit far from the pattern. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.
- **B:** Correct. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. In this case: Outlier detection finds points that sit far from the pattern.
- **C:** Incorrect for this question. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.
- **D:** Incorrect for this question. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.

### Question 74 — D

Answer: Use the Decomposition Tree visual. A decomposition tree supports open-ended drill paths. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: A decomposition tree supports open-ended drill paths.
- **B:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A decomposition tree supports open-ended drill paths.
- **C:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A decomposition tree supports open-ended drill paths.
- **D:** Correct. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. In this case: A decomposition tree supports open-ended drill paths.

### Question 75 — C, E

Answers: Use the Key Influencers visual; Use Copilot to create a narrative visual. Key Influencers ranks associated factors, and a narrative visual summarizes the page. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Key Influencers ranks associated factors, and a narrative visual summarizes the page.
- **B:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Key Influencers ranks associated factors, and a narrative visual summarizes the page.
- **C:** Correct. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. In this case: Key Influencers ranks associated factors, and a narrative visual summarizes the page.
- **D:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: Key Influencers ranks associated factors, and a narrative visual summarizes the page.
- **E:** Correct. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. In this case: Key Influencers ranks associated factors, and a narrative visual summarizes the page.

### Question 76 — A

Answer: Use Copilot to suggest a report page. Copilot can draft a page from a prompt, which the author then reviews. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. In this case: Copilot can draft a page from a prompt, which the author then reviews.
- **B:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.
- **C:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.
- **D:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.

### Question 77 — C

Answer: Create a workspace for the team that owns the content. A workspace is the collaboration and permission boundary for a team. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: A workspace is the collaboration and permission boundary for a team.
- **B:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: A workspace is the collaboration and permission boundary for a team.
- **C:** Correct. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. In this case: A workspace is the collaboration and permission boundary for a team.
- **D:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: A workspace is the collaboration and permission boundary for a team.

### Question 78 — C

Answer: Workspace Viewer role. Viewers read content without editing it. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Viewers read content without editing it.
- **B:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Viewers read content without editing it.
- **C:** Correct. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. In this case: Viewers read content without editing it.
- **D:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Viewers read content without editing it.

### Question 79 — D, E

Answers: Workspace Admin role; Workspace Member role. Admin manages the workspace and members, and Member can publish and add lower-privileged users. Admins manage the workspace, its members, and its settings, which is more than publishing content. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **B:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **C:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **D:** Correct. Admins manage the workspace, its members, and its settings, which is more than publishing content. In this case: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **E:** Correct. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. In this case: Admin manages the workspace and members, and Member can publish and add lower-privileged users.

### Question 80 — C

Answer: Define an app audience for each group of consumers. Audiences show different content to different groups from one app. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Audiences show different content to different groups from one app.
- **B:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Audiences show different content to different groups from one app.
- **C:** Correct. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. In this case: Audiences show different content to different groups from one app.
- **D:** Incorrect for this question. Consumers see the published app, so workspace edits stay invisible until the app is updated. Why the correct answer wins: Audiences show different content to different groups from one app.

### Question 81 — D

Answer: Build in the workspace → curate the app pages → assign audiences → publish and update the app. Audiences control who sees what, and consumers see changes only when the app is updated. Audiences control who sees what, and consumers only see changes when the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Publishing an unfinished report sets expectations you cannot meet and consumers see the version you last shipped. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **B:** Incorrect for this question. An app per person is unmaintainable and defeats the point of audiences. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **C:** Incorrect for this question. Direct workspace access exposes everything in the workspace and cannot be curated per audience. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **D:** Correct. Audiences control who sees what, and consumers only see changes when the app is updated. In this case: Audiences control who sees what, and consumers see changes only when the app is updated.

### Question 82 — A

Answer: Update the app after changing the workspace content. Consumers see the published app, so the app must be updated. Consumers see the published app, so workspace edits stay invisible until the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Consumers see the published app, so workspace edits stay invisible until the app is updated. In this case: Consumers see the published app, so the app must be updated.
- **B:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Consumers see the published app, so the app must be updated.
- **C:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: Consumers see the published app, so the app must be updated.
- **D:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Consumers see the published app, so the app must be updated.

### Question 83 — D

Answer: Create a dashboard in the service. A dashboard is a single canvas of tiles from several reports. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.
- **B:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.
- **C:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.
- **D:** Correct. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. In this case: A dashboard is a single canvas of tiles from several reports.

### Question 84 — C

Answer: Create a data alert on a dashboard tile. A data alert notifies when a tile value crosses a threshold. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **B:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **C:** Correct. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. In this case: A data alert notifies when a tile value crosses a threshold.
- **D:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.

### Question 85 — C, D

Answers: Configure incremental refresh with the range parameters; Set the RangeStart and RangeEnd parameters the refresh policy expects. An incremental refresh policy partitions the table, and the range parameters must filter the query. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **B:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **C:** Correct. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **D:** Correct. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **E:** Incorrect for this question. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.

### Question 86 — D

Answer: Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh. Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A later policy does not rewrite history that was never partitioned, so the load stays slow. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **B:** Incorrect for this question. A policy without the parameter filter has nothing to partition and falls back to loading everything. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **C:** Incorrect for this question. The policy is applied when the model is published and refreshed, so assuming it worked leaves a full load in place. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **D:** Correct. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. In this case: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.

### Question 87 — A

Answer: Test the role with View as role in the service. View as role shows the report exactly as a role member sees it. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. In this case: View as role shows the report exactly as a role member sees it.
- **B:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **C:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **D:** Incorrect for this question. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Why the correct answer wins: View as role shows the report exactly as a role member sees it.

### Question 88 — B

Answer: Apply a sensitivity label to the semantic model and report. A sensitivity label travels with the exported file. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: A sensitivity label travels with the exported file.
- **B:** Correct. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. In this case: A sensitivity label travels with the exported file.
- **C:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: A sensitivity label travels with the exported file.
- **D:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: A sensitivity label travels with the exported file.

### Question 89 — C

Answer: Connect to a shared semantic model instead of importing the source again. Connecting to the certified model inherits one definition, its refresh, and its security. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Connecting to the certified model inherits one definition, its refresh, and its security.
- **B:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: Connecting to the certified model inherits one definition, its refresh, and its security.
- **C:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Connecting to the certified model inherits one definition, its refresh, and its security.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Connecting to the certified model inherits one definition, its refresh, and its security.

### Question 90 — D

Answer: Profile the column with column quality, distribution, and profile views. Profiling reports valid, distinct, and empty values before shaping. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.
- **C:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.
- **D:** Correct. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. In this case: Profiling reports valid, distinct, and empty values before shaping.

### Question 91 — C

Answer: Group by the key and aggregate the measures. Grouping with an aggregate produces one row per entity and month. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Grouping with an aggregate produces one row per entity and month.
- **B:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Grouping with an aggregate produces one row per entity and month.
- **C:** Correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. In this case: Grouping with an aggregate produces one row per entity and month.
- **D:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Grouping with an aggregate produces one row per entity and month.

### Question 92 — B

Answer: Use LASTNONBLANK or LASTDATE for a semi-additive balance. A balance must be taken at a point in time, not added across dates. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **B:** Correct. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. In this case: A balance must be taken at a point in time, not added across dates.
- **C:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **D:** Incorrect for this question. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.

### Question 93 — B

Answer: Use PERCENTILE.INC for a distribution boundary. A percentile returns the boundary value, which describes the tail. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Descriptive statistics show the shape of the data, which an average alone hides. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.
- **B:** Correct. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. In this case: A percentile returns the boundary value, which describes the tail.
- **C:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.
- **D:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.

### Question 94 — C

Answer: Configure the export and download settings for the report. Export settings decide whether readers can take data out. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Export settings decide whether readers can take data out.
- **B:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Export settings decide whether readers can take data out.
- **C:** Correct. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. In this case: Export settings decide whether readers can take data out.
- **D:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Export settings decide whether readers can take data out.

### Question 95 — D

Answer: A clustered bar or column chart. A bar chart compares a measure across categories. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A bar chart compares a measure across categories.
- **B:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A bar chart compares a measure across categories.
- **C:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A bar chart compares a measure across categories.
- **D:** Correct. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. In this case: A bar chart compares a measure across categories.

### Question 96 — A

Answer: Add a reference line for the target or average. A reference line gives the comparison without a second visual. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. In this case: A reference line gives the comparison without a second visual.
- **B:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **C:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **D:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: A reference line gives the comparison without a second visual.

### Question 97 — D

Answer: Create a subscription for the report or dashboard. A subscription delivers a scheduled snapshot by email. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **B:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **C:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **D:** Correct. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. In this case: A subscription delivers a scheduled snapshot by email.

### Question 98 — C

Answer: Install an on-premises data gateway. An on-premises data gateway provides the outbound connection for cloud refresh. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.
- **B:** Incorrect for this question. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.
- **C:** Correct. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. In this case: An on-premises data gateway provides the outbound connection for cloud refresh.
- **D:** Incorrect for this question. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.

### Question 99 — B

Answer: Use a dynamic RLS rule based on USERPRINCIPALNAME. A dynamic rule matches the signed-in identity to a mapping table. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table.
- **B:** Correct. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. In this case: A dynamic rule matches the signed-in identity to a mapping table.
- **C:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table.
- **D:** Incorrect for this question. A static role is simple to reason about but must be maintained every time the org chart changes. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table.

### Question 100 — D

Answer: Certify the semantic model. Certification asserts organization-wide trust after a designated review. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **B:** Incorrect for this question. Build lets another author create reports on the model without editing it, which is how reuse is enabled safely. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **C:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **D:** Correct. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. In this case: Certification asserts organization-wide trust after a designated review.

# Microsoft PL-300 — Full-Length Mock Exam 5

AI Transformation Leader · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A finance analyst must report on margin using the model the commercial team already certifies. What should the analyst do?

Domain: Prepare the data

- A. Connect to a shared semantic model instead of importing the source again
- B. Live connection to a published semantic model
- C. Import mode
- D. DirectQuery

### 2. A store operations screen must show the current queue of online orders as it changes. Which connection fits?

Domain: Prepare the data

- A. DirectQuery
- B. Dual mode table
- C. Import mode
- D. DirectLake over a lakehouse

### 3. A retail group needs a nightly sales snapshot and a live view of fulfilment backlog. Which two storage choices fit? Select two.

Domain: Prepare the data

- A. Connect to a shared semantic model instead of importing the source again
- B. DirectQuery
- C. Import mode
- D. DirectLake over a lakehouse
- E. Live connection to a published semantic model

### 4. A query must be repointed to a renamed warehouse while keeping every transformation step. What should be changed?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Create a parameter for the server, path, or filter
- C. Change the data source settings rather than rebuilding the query
- D. Update the data source credentials in the semantic model settings

### 5. Thirty million basket lines are analysed by merchandisers all day, and the source must not be queried directly. Which mode fits?

Domain: Prepare the data

- A. DirectQuery
- B. Dual mode table
- C. DirectLake over a lakehouse
- D. Import mode

### 6. Delta tables in a Fabric lakehouse must be queried at Import-like speed with no duplicate copy. Which mode fits?

Domain: Prepare the data

- A. Dual mode table
- B. DirectQuery
- C. Import mode
- D. DirectLake over a lakehouse

### 7. A data-sharing agreement forbids storing customer transaction data outside the source platform. Which mode fits?

Domain: Prepare the data

- A. DirectQuery
- B. Dual mode table
- C. DirectLake over a lakehouse
- D. Import mode

### 8. A report must read a staging warehouse before release and the production warehouse afterwards. What should be created?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Update the data source credentials in the semantic model settings
- C. Change the data source settings rather than rebuilding the query
- D. Create a parameter for the server, path, or filter

### 9. The overnight refresh fails with an authentication error after the warehouse credential was rotated. What should be updated?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Change the data source settings rather than rebuilding the query
- C. Update the data source credentials in the semantic model settings
- D. Create a parameter for the server, path, or filter

### 10. A query joins loyalty data to payroll data, and the engine is folding values between the two sources. What should be configured?

Domain: Prepare the data

- A. Update the data source credentials in the semantic model settings
- B. Create a parameter for the server, path, or filter
- C. Change the data source settings rather than rebuilding the query
- D. Set privacy levels to isolate the sources

### 11. A basket value column arrives with a currency symbol, so totals and averages misbehave. What should be corrected?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Profile the column with column quality, distribution, and profile views
- C. Review column statistics and value distribution
- D. Replace nulls with a defined placeholder or a filled-down value

### 12. A merchandiser asks whether a few products dominate basket value. Which evidence answers that?

Domain: Prepare the data

- A. Review column statistics and value distribution
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Profile the column with column quality, distribution, and profile views
- D. Correct the column data type before building the model

### 13. A new franchise feed is arriving next month, and the team wants no rebuild. Which sequence is correct?

Domain: Prepare the data

- A. Load every column → profile in the report → patch the visual
- B. Profile the source → fix types and nulls → shape the table → load only the needed columns
- C. Load the table → discover the type errors in the report → re-import the source
- D. Shape the table → delete the profiling steps → load every column

### 14. Loyalty points double whenever a batch is re-run. What is the most likely cause?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Filter out the error rows and report them separately
- C. Trim, clean, and standardize the text values
- D. Remove duplicate rows using the natural business key

### 15. Store names differ only by trailing spaces and casing, and the basket-size column is blank for online orders. Which two fixes are required? Select two.

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Use a locale-aware conversion for dates and decimals
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Filter out the error rows and report them separately
- E. Remove duplicate rows using the natural business key

### 16. One row fails to load because a phone number sits in a numeric column. What should be investigated first?

Domain: Prepare the data

- A. Filter out the error rows and report them separately
- B. Trace the import error to the source type mismatch
- C. Trim, clean, and standardize the text values
- D. Replace nulls with a defined placeholder or a filled-down value

### 17. A store extract has stray characters, duplicated members, and mixed formats. Which sequence is defensible?

Domain: Prepare the data

- A. Convert types first → then look for duplicates → then trim
- B. Filter out the failing rows → load → ask the business later
- C. Replace all values with a default → convert types → load
- D. Identify the bad values → standardize text → convert types → document what was replaced

### 18. The report needs a single field that combines store number and channel for a label. What should be added?

Domain: Prepare the data

- A. Add a custom column with an M expression
- B. Group by the key and aggregate the measures
- C. Add a conditional column for rule-based bucketing
- D. Extract the needed part of the text with a delimiter or position

### 19. Baskets must be banded into small, medium, and large using defined value thresholds. What should be added?

Domain: Prepare the data

- A. Add a conditional column for rule-based bucketing
- B. Group by the key and aggregate the measures
- C. Add a custom column with an M expression
- D. Split the combined column into separate fields

### 20. A single address field holds street, city, and postcode separated by commas, and the report needs them apart. What should be used?

Domain: Prepare the data

- A. Add an aggregate step with the correct summarization
- B. Extract the needed part of the text with a delimiter or position
- C. Add a custom column with an M expression
- D. Split the combined column into separate fields

### 21. A category extract has one column per product family, and the model needs one family column and one value column. What should be done?

Domain: Prepare the data

- A. Expand the JSON record into typed columns
- B. Transpose the table so the header becomes a column
- C. Unpivot the month columns into rows
- D. Pivot the attribute values into columns

### 22. An order feed returns a JSON object per basket with nested line items. What should be done?

Domain: Prepare the data

- A. Convert the list value to a table and expand it
- B. Expand the JSON record into typed columns
- C. Convert the XML or JSON list into a table of rows
- D. Transpose the table so the header becomes a column

### 23. A stock file stores one row per store-attribute pair, and the report needs attributes as columns. What should be done?

Domain: Prepare the data

- A. Unpivot the month columns into rows
- B. Pivot the attribute values into columns
- C. Transpose the table so the header becomes a column
- D. Convert the XML or JSON list into a table of rows

### 24. Thirteen weekly sales files share the same columns and must become one table. What should be used?

Domain: Prepare the data

- A. Use a fuzzy merge with a similarity threshold
- B. Merge the two queries on a matching key
- C. Append the queries into one table
- D. Use a left outer join to keep every fact row

### 25. A sales fact must gain product hierarchy, and no sale may be lost when the product list is stale. Which two choices are required? Select two.

Domain: Prepare the data

- A. Use a left outer join to keep every fact row
- B. Use a fuzzy merge with a similarity threshold
- C. Append the queries into one table
- D. Merge the two queries on a matching key
- E. Create an integer surrogate key for the relationship

### 26. The same store transformation is repeated in four models, and every refresh must stay fast. Which two choices address that? Select two.

Domain: Prepare the data

- A. Stage the raw query and build a separate clean query on it
- B. Duplicate the query so the two are independent
- C. Keep the steps foldable so the source does the work
- D. Reuse a dataflow for the shared transformation
- E. Use a native query to select only the needed rows

### 27. A sales table repeats product name, category, and supplier on every row, and filters drag. What should be built?

Domain: Model the data

- A. Flatten the lookup attributes into a single dimension
- B. Normalize the dimension into a snowflake
- C. Set the table and column properties, including hidden keys and format strings
- D. Build a star schema with a fact table and conformed dimensions

### 28. Authors keep dragging transaction identifiers onto visuals, and revenue displays without a currency format. Which two actions fix that? Select two.

Domain: Model the data

- A. Set the table and column properties, including hidden keys and format strings
- B. Normalize the dimension into a snowflake
- C. Flatten the lookup attributes into a single dimension
- D. Build a star schema with a fact table and conformed dimensions
- E. Hide technical columns from the report view

### 29. A commercial model must be rebuilt from one wide export. Which sequence produces a model that lasts?

Domain: Model the data

- A. Keep one wide table → relate it to itself → build measures
- B. Build the relationships first → decide the grain afterwards → load
- C. Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact
- D. Create a dimension per column → relate each one to the fact

### 30. A shared supplier dimension is used by four facts, and supplier attributes change on their own schedule. Which design fits?

Domain: Model the data

- A. Set the table and column properties, including hidden keys and format strings
- B. Normalize the dimension into a snowflake
- C. Build a star schema with a fact table and conformed dimensions
- D. Flatten the lookup attributes into a single dimension

### 31. Order date and delivery date both relate to the date table, but only one filters the page. Why?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Single-direction filter from dimension to fact
- C. One-to-one relationship between two tables with the same grain
- D. Inactive relationship activated with USERELATIONSHIP

### 32. Products appear in many promotions and promotions cover many products, with a bridge table between them. Which relationship shape is required?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. One-to-one relationship between two tables with the same grain
- C. Many-to-many relationship with a bridging table
- D. Single-direction filter from dimension to fact

### 33. A new returns fact must filter from its dimensions and must never let one dimension filter another. Which two choices fit? Select two.

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Single-direction filter from dimension to fact
- C. Set the cross-filter direction on the relationship
- D. Many-to-many relationship with a bridging table
- E. Bi-directional cross-filtering on the relationship

### 34. A product visual ignores a selection made in a sales visual, and the model is suspected. Which setting decides that?

Domain: Model the data

- A. Bi-directional cross-filtering on the relationship
- B. Set the cross-filter direction on the relationship
- C. Single-direction filter from dimension to fact
- D. Inactive relationship activated with USERELATIONSHIP

### 35. The retail year starts in February, and reports keep showing calendar quarters. What must be added?

Domain: Model the data

- A. Create a dedicated date table marked as the date table
- B. Build the fiscal periods as columns in the date table
- C. Create one date table and role-play it through several relationships
- D. Mark the table as a date table

### 36. Order, ship, and return dates all need the same year-quarter-month logic. What should be used?

Domain: Model the data

- A. Mark the table as a date table
- B. Create a dedicated date table marked as the date table
- C. Create one date table and role-play it through several relationships
- D. Build the fiscal periods as columns in the date table

### 37. A trading review needs dependable year-to-date and prior-year sales. Which sequence delivers that?

Domain: Model the data

- A. Create a date table → leave it unrelated → filter with it
- B. Create one date table per date column → relate all of them to the fact
- C. Use the fact date column directly → write TOTALYTD → add a date slicer
- D. Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it

### 38. Basket size must respond to store and period slicers without adding a stored column. What should be created?

Domain: Model the data

- A. The filter context supplied by the visual, slicers, and page filters
- B. Create a measure for the aggregation
- C. Create a calculated column
- D. Create a calculated table

### 39. A price band must exist as a slicer field and depends on two columns in the same row. What should be created?

Domain: Model the data

- A. Create a calculated column
- B. Create a calculated table
- C. Create a measure for the aggregation
- D. The row context inside an iterator

### 40. A report needs conversion rate that survives a zero denominator and a count of unique shoppers. Which two functions fit? Select two.

Domain: Model the data

- A. Use DIVIDE instead of the division operator
- B. Use DISTINCT COUNT for unique entities
- C. Use an iterator such as SUMX over the row-level expression
- D. Create a measure for the aggregation
- E. Use an iterator function for row-level arithmetic

### 41. A measure must show each category's share of total sales while the visual lists categories. Which function changes the filter context?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Add KEEPFILTERS to intersect rather than replace the filter
- C. Store intermediate results in VAR and RETURN
- D. Wrap the aggregation in CALCULATE to change the filter context

### 42. A percentage of the chosen period must ignore the category breakdown that the visual applies. Which modifier fits?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Remove the filter with REMOVEFILTERS or ALL
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Use ALLSELECTED to respect the slicer but ignore the visual

### 43. A measure repeats the same filtered base twice and is hard to review. What should be used?

Domain: Model the data

- A. Wrap the aggregation in CALCULATE to change the filter context
- B. Use ALL on the table to clear its filters
- C. Store intermediate results in VAR and RETURN
- D. Add KEEPFILTERS to intersect rather than replace the filter

### 44. A share-of-department measure must compare each store with its whole department regardless of the store filter. Which modifier fits?

Domain: Model the data

- A. Use ALLSELECTED to respect the slicer but ignore the visual
- B. Wrap the aggregation in CALCULATE to change the filter context
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Remove the filter with REMOVEFILTERS or ALL

### 45. A merchandising review needs cumulative sales from the start of the financial year. Which pattern fits?

Domain: Model the data

- A. Use AVERAGEX over a rolling date window
- B. Use TOTALYTD or DATESYTD for year-to-date
- C. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- D. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period

### 46. A weekly pack needs the equivalent week last year and a four-week rolling average. Which two patterns are required? Select two.

Domain: Model the data

- A. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- B. Use AVERAGEX over a rolling date window
- C. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- D. Use TOTALYTD or DATESYTD for year-to-date
- E. Use DATESINPERIOD for a windowed calculation

### 47. Stock on hand is being summed across weeks and producing a meaningless peak. What should the measure do?

Domain: Model the data

- A. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- B. Use TOTALYTD or DATESYTD for year-to-date
- C. Use LASTNONBLANK when the balance is only recorded on some dates
- D. Use AVERAGEX over a rolling date window

### 48. An author needs a month-to-date figure and does not want to hand-write the DAX. What should be used?

Domain: Model the data

- A. Create a calculation group for the time-intelligence variants
- B. Create a field parameter so the author can switch the measure or axis
- C. Create a numeric range parameter for scenario analysis
- D. Use a quick measure for the standard pattern

### 49. Thirty measures need the same date variants, and readers must switch between measures on one chart. Which two features fit? Select two.

Domain: Model the data

- A. Use PERCENTILE.INC for a distribution boundary
- B. Create a field parameter so the author can switch the measure or axis
- C. Create a numeric range parameter for scenario analysis
- D. Use a quick measure for the standard pattern
- E. Create a calculation group for the time-intelligence variants

### 50. A buyer must test the effect of a discount rate on margin. What should be created?

Domain: Model the data

- A. Create a numeric range parameter for scenario analysis
- B. Create a field parameter so the author can switch the measure or axis
- C. Use PERCENTILE.INC for a distribution boundary
- D. Use a quick measure for the standard pattern

### 51. A store page takes half a minute, and the author must identify the slow visual. What should be used?

Domain: Model the data

- A. Inspect the query plan in DAX query view
- B. Reduce the granularity loaded into the model
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Run Performance Analyzer to find the slow visual

### 52. A single measure is suspected of a slow query, and the author needs to inspect the query plan. What should be used?

Domain: Model the data

- A. Add an aggregation table for the large fact
- B. Run Performance Analyzer to find the slow visual
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Inspect the query plan in DAX query view

### 53. A trading page needs a weekly sales trend and progress against the quarterly target. Which two visuals fit? Select two.

Domain: Visualize and analyze the data

- A. A matrix visual with row and column groups
- B. A gauge visual
- C. A pie or donut chart
- D. A KPI visual with a target
- E. A line chart with a date axis

### 54. A page must show the share of five channels in total revenue. Which visual fits?

Domain: Visualize and analyze the data

- A. A treemap
- B. A scatter chart
- C. A waterfall chart
- D. A pie or donut chart

### 55. A board page must explain how opening revenue became closing revenue across the quarter. Which visual fits?

Domain: Visualize and analyze the data

- A. A waterfall chart
- B. A gauge visual
- C. A funnel chart
- D. A matrix visual with row and column groups

### 56. Shoppers' analytics team needs a visible control for choosing a region on the page. What should be added?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Set the filter pane scope by page, report, or visual
- C. A slicer on the report page
- D. Sync the slicer across the pages that share the same filter

### 57. A group-wide filter must remain in force on every page rather than only on the page currently open. Where should it be placed?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. A slicer on the report page
- C. Set the filter pane scope by page, report, or visual
- D. Edit the interactions so the visual does not filter the others

### 58. Selecting a store on the page is filtering a fixed commentary card. What should be changed?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. A slicer on the report page
- C. Edit the interactions so the visual does not filter the others
- D. Set the filter pane scope by page, report, or visual

### 59. A regional view and a group view share one page, and readers must switch between saved states. What should be captured?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Add buttons with actions that navigate or apply a bookmark
- C. Use the Selection pane to group and layer visuals
- D. Capture the view in a bookmark

### 60. A pair of saved views is ready, and readers must trigger each one from the canvas with a single click. What should be added?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Add buttons with actions that navigate or apply a bookmark
- C. Use the Selection pane to group and layer visuals
- D. Capture the view in a bookmark

### 61. A trading page needs three saved views, each reachable from a button. Which sequence works?

Domain: Visualize and analyze the data

- A. Capture a bookmark before setting the filters → expect it to restore them
- B. Create the views → capture each in a bookmark → add buttons → hide the visuals not in use
- C. Use buttons without actions → tell readers to click twice
- D. Create a page per view → duplicate the visuals → maintain each page

### 62. The report will reach fifteen pages and needs navigation that stays current. What should be used?

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Capture the view in a bookmark
- C. Add a page navigator for the report
- D. Add buttons with actions that navigate or apply a bookmark

### 63. A reader must click a store and open a detail page about that store. What should be configured?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Configure a drillthrough page with the entity filter
- C. Enable drill-down through the hierarchy
- D. Set the filter pane scope by page, report, or visual

### 64. A commercial team is building its first drillthrough page. Which sequence works?

Domain: Visualize and analyze the data

- A. Put every field on the summary visual → expect drillthrough to work
- B. Set the drillthrough filter → publish → skip the back button
- C. Choose the entity field → create the drillthrough page → place the entity filter → add a back button
- D. Create the detail page → add a visual → tell readers to filter it manually

### 65. A chart must allow the reader to descend from region to store and then product in place. What should be enabled?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Build a custom tooltip page
- C. Enable drill-down through the hierarchy
- D. Configure a drillthrough page with the entity filter

### 66. Keyboard users cannot reach the slicers in a sensible order. What should be configured?

Domain: Visualize and analyze the data

- A. Set a logical tab order for the interactive elements
- B. Provide alt text for each meaningful visual
- C. Build the mobile layout in the mobile view
- D. Configure the export and download settings for the report

### 67. Readers want to change a visual from a column chart to a table without edit rights. What should be enabled?

Domain: Visualize and analyze the data

- A. Provide alt text for each meaningful visual
- B. Configure the export and download settings for the report
- C. Build the mobile layout in the mobile view
- D. Enable personalization for the visuals the reader may change

### 68. A consistent palette and font must apply across the whole report without styling visuals one by one. What should be applied?

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Turn on and format data labels
- C. Use the Selection pane to group and layer visuals
- D. Apply conditional formatting driven by a measure

### 69. A table must colour stores whose shrink exceeds the tolerance. What should be applied?

Domain: Visualize and analyze the data

- A. Apply conditional formatting driven by a measure
- B. Use the Selection pane to group and layer visuals
- C. Apply a report theme JSON
- D. Set the axis range and units explicitly

### 70. Two visuals must occupy the same space, and a line chart axis must not hide the baseline. Which two settings are required? Select two.

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Set the axis range and units explicitly
- C. Use the Selection pane to group and layer visuals
- D. Turn on and format data labels
- E. Apply conditional formatting driven by a measure

### 71. A weekly chart must show whether sales beat the plan each week. What should be added?

Domain: Visualize and analyze the data

- A. Use the built-in forecast on a line chart
- B. Add a reference line for the target or average
- C. Add error bars to show the uncertainty range
- D. Create groups for the categories that matter

### 72. A director asks why revenue fell last month, and the model has many dimensions. Which feature helps?

Domain: Visualize and analyze the data

- A. Use the outlier detection feature on the visual
- B. Use the Analyze feature to explain a change
- C. Use the built-in forecast on a line chart
- D. Use the Decomposition Tree visual

### 73. A team needs a root-cause visual in which analysts choose any dimension in any order. Which visual fits?

Domain: Visualize and analyze the data

- A. Use Q&A to answer a natural-language question
- B. Use the Decomposition Tree visual
- C. Use Copilot to suggest a report page
- D. Use the Key Influencers visual

### 74. The team wants the factors associated with basket size and a first-draft page from a prompt. Which two features fit? Select two.

Domain: Visualize and analyze the data

- A. Use Copilot to suggest a report page
- B. Use Copilot to create a narrative visual
- C. Use the Decomposition Tree visual
- D. Use the Key Influencers visual
- E. Use Q&A to answer a natural-language question

### 75. Staff want to type a business question and get a visual without another page being authored. What should be enabled?

Domain: Visualize and analyze the data

- A. Use the Key Influencers visual
- B. Use Q&A to answer a natural-language question
- C. Use the Decomposition Tree visual
- D. Use Copilot to create a narrative visual

### 76. A commercial analytics team needs one place where its authors collaborate. What should be created?

Domain: Manage and secure Power BI

- A. Publish an app from the workspace
- B. Create a workspace for the team that owns the content
- C. Workspace Viewer role
- D. Workspace Admin role

### 77. Six authors must publish and edit content but must not manage membership. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Member role
- B. Workspace Contributor role
- C. Workspace Viewer role
- D. Workspace Admin role

### 78. The team lead must manage membership, and one senior author must add lower-privileged users. Which two roles cover that? Select two.

Domain: Manage and secure Power BI

- A. Workspace Contributor role
- B. Workspace Viewer role
- C. Workspace Admin role
- D. Workspace Member role
- E. Publish an app from the workspace

### 79. Consumers should get a curated, read-only experience rather than access to every workspace item. What should be published?

Domain: Manage and secure Power BI

- A. Publish an app from the workspace
- B. Create a workspace for the team that owns the content
- C. Choose the distribution method that matches the audience
- D. Define an app audience for each group of consumers

### 80. The retail group is publishing its first app to two audiences. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Give every consumer the workspace Viewer role → skip the app
- B. Publish the app before the report is finished → update it never
- C. Build in the workspace → curate the app pages → assign audiences → publish and update the app
- D. Create one app per person → assign each audience manually

### 81. One app must show store pages to store staff and summary pages to buyers. What should be configured?

Domain: Manage and secure Power BI

- A. Define an app audience for each group of consumers
- B. Update the app after changing the workspace content
- C. Publish an app from the workspace
- D. Choose the distribution method that matches the audience

### 82. A trading director wants one page of pinned measures pulled from several reports. What should be created?

Domain: Manage and secure Power BI

- A. Create a dashboard in the service
- B. Pin the visual to a dashboard tile
- C. Create a data alert on a dashboard tile
- D. Create a subscription for the report or dashboard

### 83. A notification must fire on one specific card tile when stock cover drops. What should be used?

Domain: Manage and secure Power BI

- A. Create a data alert on a dashboard tile
- B. Create a subscription for the report or dashboard
- C. Set the alert threshold on the pinned card tile
- D. Pin the visual to a dashboard tile

### 84. The merchandising warehouse is on-premises and the service cannot reach it. What is required?

Domain: Manage and secure Power BI

- A. Virtual network data gateway
- B. Personal mode gateway
- C. Install an on-premises data gateway
- D. Configure scheduled refresh on the semantic model

### 85. A group is turning on scheduled refresh for a newly published model. Which sequence avoids a silent failure?

Domain: Manage and secure Power BI

- A. Confirm the gateway or cloud connection → store credentials → set the schedule → check refresh history
- B. Increase the refresh frequency to hourly → ignore the source load
- C. Use a personal gateway → schedule → leave the team to maintain it
- D. Set the schedule → publish → wait for the first failure email

### 86. A dynamic rule must compare a model column with the identity the service passes at query time. Which function is the basis?

Domain: Manage and secure Power BI

- A. A static RLS role per region with fixed members
- B. Define a row-level security role with a DAX filter
- C. Map the signed-in user with USERPRINCIPALNAME in the filter
- D. Use a dynamic RLS rule based on USERPRINCIPALNAME

### 87. A report contains customer contact data and must stay protected when exported. What should be applied?

Domain: Manage and secure Power BI

- A. Apply a sensitivity label to the semantic model and report
- B. Promote the content as endorsed
- C. Grant item-level access to the specific report
- D. Certify the semantic model

### 88. Another team must build its own reports on a governed model without editing it. What should be granted?

Domain: Manage and secure Power BI

- A. Promote the content as endorsed
- B. Certify the semantic model
- C. Grant Build permission on the semantic model
- D. Grant item-level access to the specific report

---

## Case study — Aurora Schools

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Schools must be segmented by attendance pattern without a predefined scheme. What should be used?

Domain: Visualize and analyze the data

- A. Use clustering to find segments in the data
- B. Use the outlier detection feature on the visual
- C. Create groups for the categories that matter
- D. Create bins for a continuous measure

### 90. The principal wants the weekly attendance report as an email snapshot. What should be configured?

Domain: Manage and secure Power BI

- A. Create a data alert on a dashboard tile
- B. Pin the visual to a dashboard tile
- C. Set the alert threshold on the pinned card tile
- D. Create a subscription for the report or dashboard

### 91. The attendance model must refresh every three hours, and the service account secret expires quarterly. Which two settings matter? Select two.

Domain: Manage and secure Power BI

- A. Configure scheduled refresh on the semantic model
- B. Configure incremental refresh with the range parameters
- C. Set the RangeStart and RangeEnd parameters the refresh policy expects
- D. Update the credentials used by the refresh schedule
- E. Install an on-premises data gateway

---

## Case study — Granite Public Works

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A contractor sends a works-order file with no documentation, and its completeness is unknown. What should be done first?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Correct the column data type before building the model
- C. Profile the column with column quality, distribution, and profile views
- D. Review column statistics and value distribution

### 93. Rolling works-order totals skip days when no crew was scheduled, and the running figure looks wrong. What is missing?

Domain: Model the data

- A. Mark the table as a date table
- B. Create a dedicated date table marked as the date table
- C. Create one date table and role-play it through several relationships
- D. Build the fiscal periods as columns in the date table

### 94. The public works dashboard must be usable by screen-reader users, and its visuals carry no descriptions. What must be added?

Domain: Visualize and analyze the data

- A. Set a logical tab order for the interactive elements
- B. Provide alt text for each meaningful visual
- C. Build the mobile layout in the mobile view
- D. Enable personalization for the visuals the reader may change

---

## Case study — Summit Retail Group

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A category manager must compare revenue across ten departments of the group. Which visual fits?

Domain: Visualize and analyze the data

- A. A clustered bar or column chart
- B. A line chart with a date axis
- C. A pie or donut chart
- D. A treemap

### 96. A hover must show sales, margin, and returns together without adding visuals to the page. Which two actions deliver that? Select two.

Domain: Visualize and analyze the data

- A. Enable drill-down through the hierarchy
- B. Configure a drillthrough page with the entity filter
- C. Use the Selection pane to group and layer visuals
- D. Set the tooltip to a report page and size it to the hover area
- E. Build a custom tooltip page

### 97. Store managers must see only their own store's rows in one shared group report. What should be created?

Domain: Manage and secure Power BI

- A. Add the security group to the role membership
- B. Define a row-level security role with a DAX filter
- C. Use a dynamic RLS rule based on USERPRINCIPALNAME
- D. Test the role with View as role in the service

---

## Case study — Willow Creek Health

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. A visit table must become one row per clinic per day, and the charge column must be decimal. Which two steps are required? Select two.

Domain: Prepare the data

- A. Add a custom column with an M expression
- B. Group by the key and aggregate the measures
- C. Correct the column data type before building the model
- D. Extract the needed part of the text with a delimiter or position
- E. Add a conditional column for rule-based bucketing

### 99. The encounter fact stores every line, but the report only ever looks at daily totals. What should be done?

Domain: Model the data

- A. Remove unnecessary rows and columns before optimizing measures
- B. Remove the high-cardinality columns the report does not use
- C. Add an aggregation table for the large fact
- D. Reduce the granularity loaded into the model

### 100. A chosen clinic network must stay applied across six report pages. What should be configured?

Domain: Visualize and analyze the data

- A. Set the filter pane scope by page, report, or visual
- B. A slicer on the report page
- C. Sync the slicer across the pages that share the same filter
- D. Edit the interactions so the visual does not filter the others

---

## Answer key and explanations

### Question 1 — A

Answer: Connect to a shared semantic model instead of importing the source again. Connecting to the certified model inherits its definitions, refresh, and security. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Connecting to the certified model inherits its definitions, refresh, and security.
- **B:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Connecting to the certified model inherits its definitions, refresh, and security.
- **C:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: Connecting to the certified model inherits its definitions, refresh, and security.
- **D:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Connecting to the certified model inherits its definitions, refresh, and security.

### Question 2 — A

Answer: DirectQuery. DirectQuery reads the source at report time, which current status requires. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery reads the source at report time, which current status requires.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.
- **C:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.

### Question 3 — B, C

Answers: Import mode; DirectQuery. The nightly snapshot is best imported, while the backlog must query the source live. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: The nightly snapshot is best imported, while the backlog must query the source live.
- **B:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: The nightly snapshot is best imported, while the backlog must query the source live.
- **C:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: The nightly snapshot is best imported, while the backlog must query the source live.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: The nightly snapshot is best imported, while the backlog must query the source live.
- **E:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: The nightly snapshot is best imported, while the backlog must query the source live.

### Question 4 — C

Answer: Change the data source settings rather than rebuilding the query. Data source settings repoint the connection and preserve the applied steps. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: Data source settings repoint the connection and preserve the applied steps.
- **B:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Data source settings repoint the connection and preserve the applied steps.
- **C:** Correct. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. In this case: Data source settings repoint the connection and preserve the applied steps.
- **D:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Data source settings repoint the connection and preserve the applied steps.

### Question 5 — D

Answer: Import mode. Import serves the volume from memory and protects the source. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import serves the volume from memory and protects the source.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Import serves the volume from memory and protects the source.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import serves the volume from memory and protects the source.
- **D:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import serves the volume from memory and protects the source.

### Question 6 — D

Answer: DirectLake over a lakehouse. DirectLake reads Delta tables directly when capacity and format allow it. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.
- **B:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.
- **C:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectLake reads Delta tables directly when capacity and format allow it.
- **D:** Correct. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. In this case: DirectLake reads Delta tables directly when capacity and format allow it.

### Question 7 — A

Answer: DirectQuery. DirectQuery leaves the data in the source and reads it at query time. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery leaves the data in the source and reads it at query time.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery leaves the data in the source and reads it at query time.

### Question 8 — D

Answer: Create a parameter for the server, path, or filter. A parameter swaps the environment without editing the M code. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **B:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **C:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **D:** Correct. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. In this case: A parameter swaps the environment without editing the M code.

### Question 9 — C

Answer: Update the data source credentials in the semantic model settings. The stored credential in the data source settings is what refresh uses. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **B:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **C:** Correct. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. In this case: The stored credential in the data source settings is what refresh uses.
- **D:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.

### Question 10 — D

Answer: Set privacy levels to isolate the sources. Privacy levels stop values being combined across sources that must stay separate. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **B:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **C:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **D:** Correct. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. In this case: Privacy levels stop values being combined across sources that must stay separate.

### Question 11 — A

Answer: Correct the column data type before building the model. A numeric value stored as text cannot be aggregated, so the type must be fixed. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **B:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **C:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.

### Question 12 — A

Answer: Review column statistics and value distribution. Value distribution shows whether the measure is concentrated in a few members. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. In this case: Value distribution shows whether the measure is concentrated in a few members.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **C:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **D:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.

### Question 13 — B

Answer: Profile the source → fix types and nulls → shape the table → load only the needed columns. Profiling comes first, shaping follows, and loading only needed columns keeps the model small. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Patching visuals hides the data problem instead of fixing it at the source. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **B:** Correct. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. In this case: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **C:** Incorrect for this question. Discovering type errors after load means the model was built on wrong data and the work restarts. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **D:** Incorrect for this question. Deleting profiling removes the evidence of quality problems and loading every column inflates the model. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.

### Question 14 — D

Answer: Remove duplicate rows using the natural business key. The same transaction key is being loaded twice, so de-duplicating on that key reverses the inflation. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: The same transaction key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: The same transaction key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **C:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: The same transaction key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **D:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: The same transaction key is being loaded twice, so de-duplicating on that key reverses the inflation.

### Question 15 — A, C

Answers: Trim, clean, and standardize the text values; Replace nulls with a defined placeholder or a filled-down value. Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. In this case: Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable.
- **B:** Incorrect for this question. A locale-aware conversion stops day and month being swapped and stops decimal commas being interpreted as text. Why the correct answer wins: Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable.
- **C:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable.
- **D:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable.
- **E:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Standardizing text collapses duplicate members, and a defined null replacement keeps online baskets countable.

### Question 16 — B

Answer: Trace the import error to the source type mismatch. Most import errors are a value that does not match the declared type, so the source column is the place to look. Most import errors come from a value that does not match the declared type, so the fix is at the source column or an explicit conversion. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **B:** Correct. Most import errors come from a value that does not match the declared type, so the fix is at the source column or an explicit conversion. In this case: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **C:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.

### Question 17 — D

Answer: Identify the bad values → standardize text → convert types → document what was replaced. Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Converting before trimming fails on values that only differ by whitespace and leaves duplicates behind. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **B:** Incorrect for this question. Silently dropping rows changes the totals and the business never learns what is missing. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **C:** Incorrect for this question. Replacing everything with a default destroys real values and hides the pattern behind the error. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **D:** Correct. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. In this case: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.

### Question 18 — A

Answer: Add a custom column with an M expression. A custom column concatenates the fields row by row. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. In this case: A custom column concatenates the fields row by row.
- **B:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A custom column concatenates the fields row by row.
- **C:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: A custom column concatenates the fields row by row.
- **D:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: A custom column concatenates the fields row by row.

### Question 19 — A

Answer: Add a conditional column for rule-based bucketing. A conditional column applies the thresholds explicitly and is easy to review. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. In this case: A conditional column applies the thresholds explicitly and is easy to review.
- **B:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A conditional column applies the thresholds explicitly and is easy to review.
- **C:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: A conditional column applies the thresholds explicitly and is easy to review.
- **D:** Incorrect for this question. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Why the correct answer wins: A conditional column applies the thresholds explicitly and is easy to review.

### Question 20 — D

Answer: Split the combined column into separate fields. Splitting on the delimiter separates the three parts. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Splitting on the delimiter separates the three parts.
- **B:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Splitting on the delimiter separates the three parts.
- **C:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Splitting on the delimiter separates the three parts.
- **D:** Correct. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. In this case: Splitting on the delimiter separates the three parts.

### Question 21 — C

Answer: Unpivot the month columns into rows. Unpivoting turns the family columns into rows. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Unpivoting turns the family columns into rows.
- **B:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Unpivoting turns the family columns into rows.
- **C:** Correct. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. In this case: Unpivoting turns the family columns into rows.
- **D:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Unpivoting turns the family columns into rows.

### Question 22 — B

Answer: Expand the JSON record into typed columns. Expanding the record exposes the nested fields as columns. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Converting a list to a table preserves every element as a row instead of keeping only the first value. Why the correct answer wins: Expanding the record exposes the nested fields as columns.
- **B:** Correct. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. In this case: Expanding the record exposes the nested fields as columns.
- **C:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Expanding the record exposes the nested fields as columns.
- **D:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Expanding the record exposes the nested fields as columns.

### Question 23 — B

Answer: Pivot the attribute values into columns. Pivoting turns attribute rows into columns. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Why the correct answer wins: Pivoting turns attribute rows into columns.
- **B:** Correct. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. In this case: Pivoting turns attribute rows into columns.
- **C:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Pivoting turns attribute rows into columns.
- **D:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Pivoting turns attribute rows into columns.

### Question 24 — C

Answer: Append the queries into one table. Appending stacks rows of the same shape. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: Appending stacks rows of the same shape.
- **B:** Incorrect for this question. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. Why the correct answer wins: Appending stacks rows of the same shape.
- **C:** Correct. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. In this case: Appending stacks rows of the same shape.
- **D:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: Appending stacks rows of the same shape.

### Question 25 — A, D

Answers: Merge the two queries on a matching key; Use a left outer join to keep every fact row. A merge adds the hierarchy, and a left outer join keeps unmatched sales. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. In this case: A merge adds the hierarchy, and a left outer join keeps unmatched sales.
- **B:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: A merge adds the hierarchy, and a left outer join keeps unmatched sales.
- **C:** Incorrect for this question. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Why the correct answer wins: A merge adds the hierarchy, and a left outer join keeps unmatched sales.
- **D:** Correct. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. In this case: A merge adds the hierarchy, and a left outer join keeps unmatched sales.
- **E:** Incorrect for this question. A single integer key is compact, stable, and avoids relationships built on text or composite columns. Why the correct answer wins: A merge adds the hierarchy, and a left outer join keeps unmatched sales.

### Question 26 — C, D

Answers: Keep the steps foldable so the source does the work; Reuse a dataflow for the shared transformation. A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Staging separates extraction from transformation, which makes each layer easier to test and reuse. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **B:** Incorrect for this question. A duplicate copies the full step chain, so a change in one copy does not affect the other but the work is repeated. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **C:** Correct. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **D:** Correct. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **E:** Incorrect for this question. A native query reduces what is transferred, but it can break folding for later steps and must be maintained as the schema changes. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.

### Question 27 — D

Answer: Build a star schema with a fact table and conformed dimensions. A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **B:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **C:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **D:** Correct. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. In this case: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.

### Question 28 — A, E

Answers: Hide technical columns from the report view; Set the table and column properties, including hidden keys and format strings. Hiding identifiers removes them from the field list, and format strings fix how values display. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **B:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **C:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **D:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **E:** Correct. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.

### Question 29 — C

Answer: Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact. Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A single wide table cannot be filtered cleanly by dimension and pushes duplication into every row. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **B:** Incorrect for this question. Relationships built before the grain is agreed will be wrong and must be rebuilt. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **C:** Correct. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. In this case: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **D:** Incorrect for this question. A dimension per column produces a hub of one-column tables and makes the model unmaintainable. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.

### Question 30 — B

Answer: Normalize the dimension into a snowflake. Normalizing the shared dimension into a snowflake keeps one copy of attributes that change independently. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: Normalizing the shared dimension into a snowflake keeps one copy of attributes that change independently.
- **B:** Correct. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. In this case: Normalizing the shared dimension into a snowflake keeps one copy of attributes that change independently.
- **C:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Normalizing the shared dimension into a snowflake keeps one copy of attributes that change independently.
- **D:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Normalizing the shared dimension into a snowflake keeps one copy of attributes that change independently.

### Question 31 — D

Answer: Inactive relationship activated with USERELATIONSHIP. Only one relationship can be active, so the second waits until a measure activates it. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **B:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **C:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **D:** Correct. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. In this case: Only one relationship can be active, so the second waits until a measure activates it.

### Question 32 — C

Answer: Many-to-many relationship with a bridging table. The bridge table resolves the many-to-many and keeps the path explicit. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the path explicit.
- **B:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the path explicit.
- **C:** Correct. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. In this case: The bridge table resolves the many-to-many and keeps the path explicit.
- **D:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the path explicit.

### Question 33 — A, B

Answers: One-to-many relationship from the dimension to the fact; Single-direction filter from dimension to fact. Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **B:** Correct. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **C:** Incorrect for this question. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **D:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **E:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.

### Question 34 — B

Answer: Set the cross-filter direction on the relationship. Cross-filter direction decides whether the fact can filter the dimension. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **B:** Correct. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. In this case: Cross-filter direction decides whether the fact can filter the dimension.
- **C:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **D:** Incorrect for this question. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.

### Question 35 — B

Answer: Build the fiscal periods as columns in the date table. Fiscal period columns let time intelligence follow the retail year. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Fiscal period columns let time intelligence follow the retail year.
- **B:** Correct. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. In this case: Fiscal period columns let time intelligence follow the retail year.
- **C:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Fiscal period columns let time intelligence follow the retail year.
- **D:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: Fiscal period columns let time intelligence follow the retail year.

### Question 36 — C

Answer: Create one date table and role-play it through several relationships. One date table related three times through role-playing dimensions avoids duplicate date tables. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate date tables.
- **B:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate date tables.
- **C:** Correct. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. In this case: One date table related three times through role-playing dimensions avoids duplicate date tables.
- **D:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: One date table related three times through role-playing dimensions avoids duplicate date tables.

### Question 37 — D

Answer: Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it. Marking and relating the date table is what makes the measures obey the date slicer. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. An unrelated date table filters nothing, so the slicer appears to work while the visuals ignore it. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **B:** Incorrect for this question. Several date tables multiply relationships and make every time measure ambiguous. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **C:** Incorrect for this question. A fact date column has gaps, so year-to-date silently skips missing days and the slicer shows no clean hierarchy. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **D:** Correct. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. In this case: Marking and relating the date table is what makes the measures obey the date slicer.

### Question 38 — B

Answer: Create a measure for the aggregation. A measure is evaluated in the filter context the visual supplies. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **B:** Correct. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. In this case: A measure is evaluated in the filter context the visual supplies.
- **C:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **D:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.

### Question 39 — A

Answer: Create a calculated column. A calculated column is computed row by row and stored, which a slicer field needs. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. In this case: A calculated column is computed row by row and stored, which a slicer field needs.
- **B:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A calculated column is computed row by row and stored, which a slicer field needs.
- **C:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: A calculated column is computed row by row and stored, which a slicer field needs.
- **D:** Incorrect for this question. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. Why the correct answer wins: A calculated column is computed row by row and stored, which a slicer field needs.

### Question 40 — A, B

Answers: Use DIVIDE instead of the division operator; Use DISTINCT COUNT for unique entities. DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. Distinct count answers how many unique customers or orders, which a plain count would overstate. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. In this case: DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question.
- **B:** Correct. Distinct count answers how many unique customers or orders, which a plain count would overstate. In this case: DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question.
- **C:** Incorrect for this question. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. Why the correct answer wins: DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question.
- **D:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question.
- **E:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: DIVIDE avoids a division error, and DISTINCT COUNT answers the unique-shopper question.

### Question 41 — D

Answer: Wrap the aggregation in CALCULATE to change the filter context. CALCULATE evaluates the expression under modified filters. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **B:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **C:** Incorrect for this question. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **D:** Correct. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. In this case: CALCULATE evaluates the expression under modified filters.

### Question 42 — D

Answer: Use ALLSELECTED to respect the slicer but ignore the visual. ALLSELECTED respects the reader's selection while removing the visual's grouping. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **B:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **D:** Correct. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. In this case: ALLSELECTED respects the reader's selection while removing the visual's grouping.

### Question 43 — C

Answer: Store intermediate results in VAR and RETURN. Variables compute the expression once and make the measure readable. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **B:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **C:** Correct. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. In this case: Variables compute the expression once and make the measure readable.
- **D:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Variables compute the expression once and make the measure readable.

### Question 44 — D

Answer: Remove the filter with REMOVEFILTERS or ALL. Removing the store filter lets the denominator cover the whole department. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: Removing the store filter lets the denominator cover the whole department.
- **B:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Removing the store filter lets the denominator cover the whole department.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Removing the store filter lets the denominator cover the whole department.
- **D:** Correct. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. In this case: Removing the store filter lets the denominator cover the whole department.

### Question 45 — B

Answer: Use TOTALYTD or DATESYTD for year-to-date. Year-to-date accumulates from the start of the year defined by the marked date table. Year-to-date functions accumulate from the start of the year defined by the marked date table. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **B:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date accumulates from the start of the year defined by the marked date table.
- **C:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **D:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.

### Question 46 — A, B

Answers: Use SAMEPERIODLASTYEAR or DATEADD for the comparable period; Use AVERAGEX over a rolling date window. The comparable-period shift supplies last year, and a rolling window averages the recent weeks. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. In this case: The comparable-period shift supplies last year, and a rolling window averages the recent weeks.
- **B:** Correct. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. In this case: The comparable-period shift supplies last year, and a rolling window averages the recent weeks.
- **C:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: The comparable-period shift supplies last year, and a rolling window averages the recent weeks.
- **D:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: The comparable-period shift supplies last year, and a rolling window averages the recent weeks.
- **E:** Incorrect for this question. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Why the correct answer wins: The comparable-period shift supplies last year, and a rolling window averages the recent weeks.

### Question 47 — A

Answer: Use LASTNONBLANK or LASTDATE for a semi-additive balance. A balance must be taken at a point in time, not added across dates. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. In this case: A balance must be taken at a point in time, not added across dates.
- **B:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **C:** Incorrect for this question. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **D:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.

### Question 48 — D

Answer: Use a quick measure for the standard pattern. A quick measure generates the standard pattern. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A quick measure generates the standard pattern.
- **B:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A quick measure generates the standard pattern.
- **C:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A quick measure generates the standard pattern.
- **D:** Correct. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. In this case: A quick measure generates the standard pattern.

### Question 49 — B, E

Answers: Create a calculation group for the time-intelligence variants; Create a field parameter so the author can switch the measure or axis. A calculation group applies the variants to every measure, and a field parameter switches the measure in place. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **B:** Correct. A field parameter lets one visual switch between measures or dimensions without duplicating pages. In this case: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **C:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **D:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **E:** Correct. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. In this case: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.

### Question 50 — A

Answer: Create a numeric range parameter for scenario analysis. A numeric range parameter drives a measure with the selected assumption. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. In this case: A numeric range parameter drives a measure with the selected assumption.
- **B:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.
- **C:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.
- **D:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.

### Question 51 — D

Answer: Run Performance Analyzer to find the slow visual. Performance Analyzer times each visual and separates DAX, query, and rendering cost. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **B:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **D:** Correct. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. In this case: Performance Analyzer times each visual and separates DAX, query, and rendering cost.

### Question 52 — D

Answer: Inspect the query plan in DAX query view. DAX query view shows the generated query and its timings. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: DAX query view shows the generated query and its timings.
- **B:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: DAX query view shows the generated query and its timings.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: DAX query view shows the generated query and its timings.
- **D:** Correct. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. In this case: DAX query view shows the generated query and its timings.

### Question 53 — D, E

Answers: A line chart with a date axis; A KPI visual with a target. A line chart shows the trend, and a KPI visual shows progress against a target. A line chart shows a trend over a continuous axis, which is what time series need. A KPI visual states progress against a defined target, which a plain card cannot show. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.
- **B:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.
- **C:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a target.
- **D:** Correct. A KPI visual states progress against a defined target, which a plain card cannot show. In this case: A line chart shows the trend, and a KPI visual shows progress against a target.
- **E:** Correct. A line chart shows a trend over a continuous axis, which is what time series need. In this case: A line chart shows the trend, and a KPI visual shows progress against a target.

### Question 54 — D

Answer: A pie or donut chart. A pie chart shows part-to-whole for a few categories. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A pie chart shows part-to-whole for a few categories.
- **B:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A pie chart shows part-to-whole for a few categories.
- **C:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A pie chart shows part-to-whole for a few categories.
- **D:** Correct. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. In this case: A pie chart shows part-to-whole for a few categories.

### Question 55 — A

Answer: A waterfall chart. A waterfall explains movement between a starting and ending value. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A waterfall explains how a starting value moves to an ending value through additions and subtractions. In this case: A waterfall explains movement between a starting and ending value.
- **B:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A waterfall explains movement between a starting and ending value.
- **C:** Incorrect for this question. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Why the correct answer wins: A waterfall explains movement between a starting and ending value.
- **D:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A waterfall explains movement between a starting and ending value.

### Question 56 — C

Answer: A slicer on the report page. A slicer puts the control on the canvas. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: A slicer puts the control on the canvas.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: A slicer puts the control on the canvas.
- **C:** Correct. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. In this case: A slicer puts the control on the canvas.
- **D:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: A slicer puts the control on the canvas.

### Question 57 — C

Answer: Set the filter pane scope by page, report, or visual. Filter scope decides whether a filter applies to a visual, a page, or the whole report. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **B:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **C:** Correct. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. In this case: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.

### Question 58 — C

Answer: Edit the interactions so the visual does not filter the others. Interaction settings decide whether a selection filters, highlights, or does nothing. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **B:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **C:** Correct. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. In this case: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **D:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.

### Question 59 — D

Answer: Capture the view in a bookmark. A bookmark stores filter and visibility state. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: A bookmark stores filter and visibility state.
- **B:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A bookmark stores filter and visibility state.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A bookmark stores filter and visibility state.
- **D:** Correct. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. In this case: A bookmark stores filter and visibility state.

### Question 60 — B

Answer: Add buttons with actions that navigate or apply a bookmark. Buttons with bookmark actions turn a stored state into a click. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: Buttons with bookmark actions turn a stored state into a click.
- **B:** Correct. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. In this case: Buttons with bookmark actions turn a stored state into a click.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Buttons with bookmark actions turn a stored state into a click.
- **D:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: Buttons with bookmark actions turn a stored state into a click.

### Question 61 — B

Answer: Create the views → capture each in a bookmark → add buttons → hide the visuals not in use. Bookmarks store state and buttons apply it. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark captures the state at the moment it is created, so filters set afterwards are not stored. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **B:** Correct. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. In this case: Bookmarks store state and buttons apply it.
- **C:** Incorrect for this question. A button with no action is decoration and the report still has no navigation. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **D:** Incorrect for this question. Duplicating pages multiplies maintenance and the copies drift apart. Why the correct answer wins: Bookmarks store state and buttons apply it.

### Question 62 — C

Answer: Add a page navigator for the report. A page navigator generates navigation from the pages themselves. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **B:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **C:** Correct. A page navigator generates navigation for every page automatically, which stays correct as pages are added. In this case: A page navigator generates navigation from the pages themselves.
- **D:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A page navigator generates navigation from the pages themselves.

### Question 63 — B

Answer: Configure a drillthrough page with the entity filter. Drillthrough passes the selected entity to a detail page through a filter. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **B:** Correct. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. In this case: Drillthrough passes the selected entity to a detail page through a filter.
- **C:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **D:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.

### Question 64 — C

Answer: Choose the entity field → create the drillthrough page → place the entity filter → add a back button. The drillthrough filter carries the selection, and the back button keeps the reader oriented. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Too many fields on one visual makes the click target ambiguous and the drill result unpredictable. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **B:** Incorrect for this question. Without a back button the reader is stranded on the detail page and loses the summary context. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **C:** Correct. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. In this case: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **D:** Incorrect for this question. A page without the drillthrough filter does not carry the selected entity, so the detail is not about what was clicked. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.

### Question 65 — C

Answer: Enable drill-down through the hierarchy. Drill-down moves through the hierarchy inside the same visual. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **B:** Incorrect for this question. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **C:** Correct. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. In this case: Drill-down moves through the hierarchy inside the same visual.
- **D:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.

### Question 66 — A

Answer: Set a logical tab order for the interactive elements. Tab order decides the keyboard sequence through interactive elements. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. In this case: Tab order decides the keyboard sequence through interactive elements.
- **B:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Tab order decides the keyboard sequence through interactive elements.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Tab order decides the keyboard sequence through interactive elements.
- **D:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: Tab order decides the keyboard sequence through interactive elements.

### Question 67 — D

Answer: Enable personalization for the visuals the reader may change. Personalization lets a reader change the visual while the author keeps the default. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the default.
- **B:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the default.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the default.
- **D:** Correct. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. In this case: Personalization lets a reader change the visual while the author keeps the default.

### Question 68 — A

Answer: Apply a report theme JSON. A theme applies a consistent palette across the report. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. In this case: A theme applies a consistent palette across the report.
- **B:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: A theme applies a consistent palette across the report.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A theme applies a consistent palette across the report.
- **D:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: A theme applies a consistent palette across the report.

### Question 69 — A

Answer: Apply conditional formatting driven by a measure. Conditional formatting driven by a measure encodes the exception. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. In this case: Conditional formatting driven by a measure encodes the exception.
- **B:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.
- **C:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.
- **D:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception.

### Question 70 — B, C

Answers: Use the Selection pane to group and layer visuals; Set the axis range and units explicitly. The Selection pane controls layering, and an explicit axis range prevents a misleading scale. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **B:** Correct. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. In this case: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **C:** Correct. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. In this case: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **D:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **E:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.

### Question 71 — B

Answer: Add a reference line for the target or average. A reference line gives the comparison without a second visual. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **B:** Correct. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. In this case: A reference line gives the comparison without a second visual.
- **C:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **D:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: A reference line gives the comparison without a second visual.

### Question 72 — B

Answer: Use the Analyze feature to explain a change. The Analyze feature decomposes the change across dimensions. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Why the correct answer wins: The Analyze feature decomposes the change across dimensions.
- **B:** Correct. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. In this case: The Analyze feature decomposes the change across dimensions.
- **C:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: The Analyze feature decomposes the change across dimensions.
- **D:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: The Analyze feature decomposes the change across dimensions.

### Question 73 — B

Answer: Use the Decomposition Tree visual. A decomposition tree supports open-ended drill paths. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: A decomposition tree supports open-ended drill paths.
- **B:** Correct. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. In this case: A decomposition tree supports open-ended drill paths.
- **C:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A decomposition tree supports open-ended drill paths.
- **D:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A decomposition tree supports open-ended drill paths.

### Question 74 — A, D

Answers: Use the Key Influencers visual; Use Copilot to suggest a report page. Key Influencers ranks associated factors, and Copilot can draft a page for the author to review. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. In this case: Key Influencers ranks associated factors, and Copilot can draft a page for the author to review.
- **B:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Key Influencers ranks associated factors, and Copilot can draft a page for the author to review.
- **C:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Key Influencers ranks associated factors, and Copilot can draft a page for the author to review.
- **D:** Correct. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. In this case: Key Influencers ranks associated factors, and Copilot can draft a page for the author to review.
- **E:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Key Influencers ranks associated factors, and Copilot can draft a page for the author to review.

### Question 75 — B

Answer: Use Q&A to answer a natural-language question. Q&A maps a typed question to the model and returns a visual. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.
- **B:** Correct. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. In this case: Q&A maps a typed question to the model and returns a visual.
- **C:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.
- **D:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.

### Question 76 — B

Answer: Create a workspace for the team that owns the content. A workspace is the collaboration and permission boundary for the team. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **B:** Correct. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. In this case: A workspace is the collaboration and permission boundary for the team.
- **C:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **D:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.

### Question 77 — B

Answer: Workspace Contributor role. Contributors publish and edit without controlling membership. Contributors can publish and edit content, which is the role for authors who should not manage membership. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Contributors publish and edit without controlling membership.
- **B:** Correct. Contributors can publish and edit content, which is the role for authors who should not manage membership. In this case: Contributors publish and edit without controlling membership.
- **C:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Contributors publish and edit without controlling membership.
- **D:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Contributors publish and edit without controlling membership.

### Question 78 — C, D

Answers: Workspace Admin role; Workspace Member role. Admin manages the workspace and members, and Member can publish and add lower-privileged users. Admins manage the workspace, its members, and its settings, which is more than publishing content. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **B:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **C:** Correct. Admins manage the workspace, its members, and its settings, which is more than publishing content. In this case: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **D:** Correct. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. In this case: Admin manages the workspace and members, and Member can publish and add lower-privileged users.
- **E:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Admin manages the workspace and members, and Member can publish and add lower-privileged users.

### Question 79 — A

Answer: Publish an app from the workspace. An app gives consumers a curated experience with its own audience list. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. In this case: An app gives consumers a curated experience with its own audience list.
- **B:** Incorrect for this question. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.
- **C:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.
- **D:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.

### Question 80 — C

Answer: Build in the workspace → curate the app pages → assign audiences → publish and update the app. Audiences control who sees what, and consumers see changes only when the app is updated. Audiences control who sees what, and consumers only see changes when the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Direct workspace access exposes everything in the workspace and cannot be curated per audience. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **B:** Incorrect for this question. Publishing an unfinished report sets expectations you cannot meet and consumers see the version you last shipped. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **C:** Correct. Audiences control who sees what, and consumers only see changes when the app is updated. In this case: Audiences control who sees what, and consumers see changes only when the app is updated.
- **D:** Incorrect for this question. An app per person is unmaintainable and defeats the point of audiences. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.

### Question 81 — A

Answer: Define an app audience for each group of consumers. Audiences show different content to different groups from one app. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. In this case: Audiences show different content to different groups from one app.
- **B:** Incorrect for this question. Consumers see the published app, so workspace edits stay invisible until the app is updated. Why the correct answer wins: Audiences show different content to different groups from one app.
- **C:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Audiences show different content to different groups from one app.
- **D:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Audiences show different content to different groups from one app.

### Question 82 — A

Answer: Create a dashboard in the service. A dashboard is a single canvas of tiles from several reports. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. In this case: A dashboard is a single canvas of tiles from several reports.
- **B:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.
- **C:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.
- **D:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A dashboard is a single canvas of tiles from several reports.

### Question 83 — C

Answer: Set the alert threshold on the pinned card tile. Alerts are configured per tile, so the tile must expose a single value. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.
- **B:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.
- **C:** Correct. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. In this case: Alerts are configured per tile, so the tile must expose a single value.
- **D:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.

### Question 84 — C

Answer: Install an on-premises data gateway. An on-premises data gateway provides the outbound connection for cloud refresh. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.
- **B:** Incorrect for this question. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.
- **C:** Correct. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. In this case: An on-premises data gateway provides the outbound connection for cloud refresh.
- **D:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An on-premises data gateway provides the outbound connection for cloud refresh.

### Question 85 — A

Answer: Confirm the gateway or cloud connection → store credentials → set the schedule → check refresh history. Connectivity and credentials must be proven first, and history is how a failure is detected. Refresh depends on connectivity and credentials before the schedule matters, and history is how a failure is detected. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Refresh depends on connectivity and credentials before the schedule matters, and history is how a failure is detected. In this case: Connectivity and credentials must be proven first, and history is how a failure is detected.
- **B:** Incorrect for this question. Refreshing hourly without checking source capacity overloads the source and can exceed the refresh window. Why the correct answer wins: Connectivity and credentials must be proven first, and history is how a failure is detected.
- **C:** Incorrect for this question. A personal gateway fails when the individual is unavailable or changes machines. Why the correct answer wins: Connectivity and credentials must be proven first, and history is how a failure is detected.
- **D:** Incorrect for this question. Scheduling before connectivity and credentials are proven guarantees a failed first refresh. Why the correct answer wins: Connectivity and credentials must be proven first, and history is how a failure is detected.

### Question 86 — C

Answer: Map the signed-in user with USERPRINCIPALNAME in the filter. USERPRINCIPALNAME supplies the signed-in identity for the comparison. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A static role is simple to reason about but must be maintained every time the org chart changes. Why the correct answer wins: USERPRINCIPALNAME supplies the signed-in identity for the comparison.
- **B:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: USERPRINCIPALNAME supplies the signed-in identity for the comparison.
- **C:** Correct. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. In this case: USERPRINCIPALNAME supplies the signed-in identity for the comparison.
- **D:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: USERPRINCIPALNAME supplies the signed-in identity for the comparison.

### Question 87 — A

Answer: Apply a sensitivity label to the semantic model and report. A sensitivity label travels with the exported file. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. In this case: A sensitivity label travels with the exported file.
- **B:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: A sensitivity label travels with the exported file.
- **C:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: A sensitivity label travels with the exported file.
- **D:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: A sensitivity label travels with the exported file.

### Question 88 — C

Answer: Grant Build permission on the semantic model. Build permission allows downstream reports without model edits. Build lets another author create reports on the model without editing it, which is how reuse is enabled safely. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: Build permission allows downstream reports without model edits.
- **B:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: Build permission allows downstream reports without model edits.
- **C:** Correct. Build lets another author create reports on the model without editing it, which is how reuse is enabled safely. In this case: Build permission allows downstream reports without model edits.
- **D:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: Build permission allows downstream reports without model edits.

### Question 89 — A

Answer: Use clustering to find segments in the data. Clustering groups rows that behave similarly. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. In this case: Clustering groups rows that behave similarly.
- **B:** Incorrect for this question. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Why the correct answer wins: Clustering groups rows that behave similarly.
- **C:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: Clustering groups rows that behave similarly.
- **D:** Incorrect for this question. Binning turns a continuous value into ranges, which is how a distribution becomes readable. Why the correct answer wins: Clustering groups rows that behave similarly.

### Question 90 — D

Answer: Create a subscription for the report or dashboard. A subscription delivers a scheduled snapshot by email. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **B:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **C:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **D:** Correct. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. In this case: A subscription delivers a scheduled snapshot by email.

### Question 91 — A, D

Answers: Configure scheduled refresh on the semantic model; Update the credentials used by the refresh schedule. The schedule controls freshness, and the stored credential must be current or refresh fails. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. In this case: The schedule controls freshness, and the stored credential must be current or refresh fails.
- **B:** Incorrect for this question. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or refresh fails.
- **C:** Incorrect for this question. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or refresh fails.
- **D:** Correct. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. In this case: The schedule controls freshness, and the stored credential must be current or refresh fails.
- **E:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or refresh fails.

### Question 92 — C

Answer: Profile the column with column quality, distribution, and profile views. Profiling reports valid, distinct, and empty values before shaping. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.
- **B:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.
- **C:** Correct. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. In this case: Profiling reports valid, distinct, and empty values before shaping.
- **D:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: Profiling reports valid, distinct, and empty values before shaping.

### Question 93 — B

Answer: Create a dedicated date table marked as the date table. A contiguous date table supplies every date so accumulation does not skip gaps. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **B:** Correct. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. In this case: A contiguous date table supplies every date so accumulation does not skip gaps.
- **C:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **D:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.

### Question 94 — B

Answer: Provide alt text for each meaningful visual. Alt text describes each visual for a screen reader. Alt text describes the visual for a screen reader, which is required for an accessible report. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **B:** Correct. Alt text describes the visual for a screen reader, which is required for an accessible report. In this case: Alt text describes each visual for a screen reader.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **D:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Alt text describes each visual for a screen reader.

### Question 95 — A

Answer: A clustered bar or column chart. A bar chart compares a measure across categories. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. In this case: A bar chart compares a measure across categories.
- **B:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A bar chart compares a measure across categories.
- **C:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A bar chart compares a measure across categories.
- **D:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A bar chart compares a measure across categories.

### Question 96 — D, E

Answers: Build a custom tooltip page; Set the tooltip to a report page and size it to the hover area. A tooltip page holds the extra measures, and the report-page tooltip setting displays it. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **B:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **D:** Correct. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **E:** Correct. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.

### Question 97 — B

Answer: Define a row-level security role with a DAX filter. RLS roles filter the model per user at query time. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Why the correct answer wins: RLS roles filter the model per user at query time.
- **B:** Correct. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. In this case: RLS roles filter the model per user at query time.
- **C:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: RLS roles filter the model per user at query time.
- **D:** Incorrect for this question. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. Why the correct answer wins: RLS roles filter the model per user at query time.

### Question 98 — B, C

Answers: Group by the key and aggregate the measures; Correct the column data type before building the model. Grouping produces one row per store and day, and converting the type makes the sum correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Grouping produces one row per store and day, and converting the type makes the sum correct.
- **B:** Correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. In this case: Grouping produces one row per store and day, and converting the type makes the sum correct.
- **C:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: Grouping produces one row per store and day, and converting the type makes the sum correct.
- **D:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Grouping produces one row per store and day, and converting the type makes the sum correct.
- **E:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Grouping produces one row per store and day, and converting the type makes the sum correct.

### Question 99 — D

Answer: Reduce the granularity loaded into the model. Loading at the grain the report needs removes unused rows. Loading to the grain the report actually needs removes rows the visuals never use. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: Loading at the grain the report needs removes unused rows.
- **B:** Incorrect for this question. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. Why the correct answer wins: Loading at the grain the report needs removes unused rows.
- **C:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: Loading at the grain the report needs removes unused rows.
- **D:** Correct. Loading to the grain the report actually needs removes rows the visuals never use. In this case: Loading at the grain the report needs removes unused rows.

### Question 100 — C

Answer: Sync the slicer across the pages that share the same filter. Syncing the slicer keeps one selection consistent across pages. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **B:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **C:** Correct. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. In this case: Syncing the slicer keeps one selection consistent across pages.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.

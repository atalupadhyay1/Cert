# Microsoft PL-300 — Full-Length Mock Exam 1

AI Transformation Leader · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A retail operations team must see stock movements within a minute of the source transaction, and the source can carry a predictable query load. Which connection should the model use?

Domain: Prepare the data

- A. Import mode
- B. DirectQuery
- C. Live connection to a published semantic model
- D. DirectLake over a lakehouse

### 2. A distributor needs near-real-time stock for operations and a nightly snapshot for finance reporting. Which two storage choices fit? Select two.

Domain: Prepare the data

- A. Connect to a shared semantic model instead of importing the source again
- B. DirectLake over a lakehouse
- C. Import mode
- D. Live connection to a published semantic model
- E. DirectQuery

### 3. The server for an existing query has moved, and every applied step must be preserved. What should the author change?

Domain: Prepare the data

- A. Change the data source settings rather than rebuilding the query
- B. Set privacy levels to isolate the sources
- C. Create a parameter for the server, path, or filter
- D. Update the data source credentials in the semantic model settings

### 4. A Fabric lakehouse holds Delta tables and the team wants Import-like speed without a second copy. Which mode fits?

Domain: Prepare the data

- A. Import mode
- B. Dual mode table
- C. DirectQuery
- D. DirectLake over a lakehouse

### 5. A 200-million-row fact must serve 300 analysts, and the source cannot take interactive load. Which mode fits?

Domain: Prepare the data

- A. Import mode
- B. Dual mode table
- C. DirectLake over a lakehouse
- D. DirectQuery

### 6. A composite model imports its dimensions but leaves the fact in DirectQuery, and round trips are slowing reports. Which setting reduces them?

Domain: Prepare the data

- A. DirectLake over a lakehouse
- B. DirectQuery
- C. Dual mode table
- D. Import mode

### 7. A query must point at a development server during testing and a production server after release, without editing the M code. What should be created?

Domain: Prepare the data

- A. Create a parameter for the server, path, or filter
- B. Set privacy levels to isolate the sources
- C. Update the data source credentials in the semantic model settings
- D. Change the data source settings rather than rebuilding the query

### 8. Scheduled refresh starts failing with an authentication error after the database password was rotated. What must be updated?

Domain: Prepare the data

- A. Update the data source credentials in the semantic model settings
- B. Change the data source settings rather than rebuilding the query
- C. Create a parameter for the server, path, or filter
- D. Set privacy levels to isolate the sources

### 9. Two sources are combined in one query and the engine is folding values across them. Which setting prevents that?

Domain: Prepare the data

- A. Change the data source settings rather than rebuilding the query
- B. Create a parameter for the server, path, or filter
- C. Update the data source credentials in the semantic model settings
- D. Set privacy levels to isolate the sources

### 10. A newly supplied supplier file has unknown quality, and the team wants evidence before shaping it. What should be done first?

Domain: Prepare the data

- A. Profile the column with column quality, distribution, and profile views
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Correct the column data type before building the model
- D. Review column statistics and value distribution

### 11. A date column arrives as text, and yearly comparisons fail to group correctly. What should be corrected first?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Review column statistics and value distribution
- D. Profile the column with column quality, distribution, and profile views

### 12. A team is taking on a supplier file nobody has inspected before. Which sequence keeps bad data out of the model?

Domain: Prepare the data

- A. Load every column → profile in the report → patch the visual
- B. Profile the source → fix types and nulls → shape the table → load only the needed columns
- C. Load the table → discover the type errors in the report → re-import the source
- D. Shape the table → delete the profiling steps → load every column

### 13. A discount column is empty for four percent of rows, and monthly totals that should show zero sometimes show blank. What should be done?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Filter out the error rows and report them separately
- C. Trim, clean, and standardize the text values
- D. Remove duplicate rows using the natural business key

### 14. A nightly extract repeats order lines when a batch is re-run and also leaves freight as null. Which two fixes are required? Select two.

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Filter out the error rows and report them separately
- C. Use a locale-aware conversion for dates and decimals
- D. Remove duplicate rows using the natural business key
- E. Replace nulls with a defined placeholder or a filled-down value

### 15. Revenue doubles every time the source batch is reprocessed. What is the most likely cause?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Remove duplicate rows using the natural business key
- C. Trim, clean, and standardize the text values
- D. Filter out the error rows and report them separately

### 16. A customer list has inconsistent casing, stray spaces, and mixed date formats. Which sequence is defensible?

Domain: Prepare the data

- A. Convert types first → then look for duplicates → then trim
- B. Filter out the failing rows → load → ask the business later
- C. Replace all values with a default → convert types → load
- D. Identify the bad values → standardize text → convert types → document what was replaced

### 17. A table holds separate first-name and last-name columns, and the report needs one display name. What should be added?

Domain: Prepare the data

- A. Add an aggregate step with the correct summarization
- B. Add a conditional column for rule-based bucketing
- C. Add a custom column with an M expression
- D. Group by the key and aggregate the measures

### 18. Customers must be banded into bronze, silver, and gold using published spend thresholds. What should be added?

Domain: Prepare the data

- A. Add a custom column with an M expression
- B. Add an aggregate step with the correct summarization
- C. Add a conditional column for rule-based bucketing
- D. Group by the key and aggregate the measures

### 19. Product codes begin with a three-letter region prefix that the report needs as its own field. What should be done?

Domain: Prepare the data

- A. Extract the needed part of the text with a delimiter or position
- B. Add a custom column with an M expression
- C. Split the combined column into separate fields
- D. Add an aggregate step with the correct summarization

### 20. A sales extract has one column per month, and the model needs a single date column and a single value column. What should be done?

Domain: Prepare the data

- A. Unpivot the month columns into rows
- B. Expand the JSON record into typed columns
- C. Pivot the attribute values into columns
- D. Transpose the table so the header becomes a column

### 21. A source holds one row per product-attribute pair, and the report needs the attributes as columns. What should be done?

Domain: Prepare the data

- A. Transpose the table so the header becomes a column
- B. Pivot the attribute values into columns
- C. Expand the JSON record into typed columns
- D. Unpivot the month columns into rows

### 22. An order API returns a JSON object per order with nested customer fields. What should be done?

Domain: Prepare the data

- A. Convert the list value to a table and expand it
- B. Expand the JSON record into typed columns
- C. Convert the XML or JSON list into a table of rows
- D. Transpose the table so the header becomes a column

### 23. Twelve monthly files share the same columns and must become one table. What should be used?

Domain: Prepare the data

- A. Use a fuzzy merge with a similarity threshold
- B. Append the queries into one table
- C. Merge the two queries on a matching key
- D. Use a left outer join to keep every fact row

### 24. A fact table must gain product category, and no sales row may be dropped when a product is missing from the lookup. Which two choices are required? Select two.

Domain: Prepare the data

- A. Append the queries into one table
- B. Use a fuzzy merge with a similarity threshold
- C. Use a left outer join to keep every fact row
- D. Create an integer surrogate key for the relationship
- E. Merge the two queries on a matching key

### 25. The same transformation is repeated in five models, and every refresh must stay fast. Which two choices address that? Select two.

Domain: Prepare the data

- A. Stage the raw query and build a separate clean query on it
- B. Use a native query to select only the needed rows
- C. Keep the steps foldable so the source does the work
- D. Reuse a dataflow for the shared transformation
- E. Duplicate the query so the two are independent

### 26. Report authors keep dragging technical key columns onto visuals, and totals display with no format. Which two actions fix that? Select two.

Domain: Model the data

- A. Hide technical columns from the report view
- B. Set the table and column properties, including hidden keys and format strings
- C. Build a star schema with a fact table and conformed dimensions
- D. Normalize the dimension into a snowflake
- E. Flatten the lookup attributes into a single dimension

### 27. A team is rebuilding a model that grew out of one wide spreadsheet. Which sequence produces a model that scales?

Domain: Model the data

- A. Keep one wide table → relate it to itself → build measures
- B. Build the relationships first → decide the grain afterwards → load
- C. Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact
- D. Create a dimension per column → relate each one to the fact

### 28. A legacy model places a region table between customer and fact, and every filter takes an extra hop. What should be done?

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Flatten the lookup attributes into a single dimension
- C. Set the table and column properties, including hidden keys and format strings
- D. Build a star schema with a fact table and conformed dimensions

### 29. Two relationships link the same date table to order date and ship date, and only one filters at a time. What explains that?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Single-direction filter from dimension to fact
- C. Inactive relationship activated with USERELATIONSHIP
- D. Bi-directional cross-filtering on the relationship

### 30. Students enrol in many courses and courses have many students, with an enrolment table between them. Which relationship shape is required?

Domain: Model the data

- A. One-to-one relationship between two tables with the same grain
- B. Single-direction filter from dimension to fact
- C. Many-to-many relationship with a bridging table
- D. One-to-many relationship from the dimension to the fact

### 31. A new fact table must filter from its dimensions and must never let a dimension filter another dimension. Which two choices fit? Select two.

Domain: Model the data

- A. Many-to-many relationship with a bridging table
- B. Bi-directional cross-filtering on the relationship
- C. One-to-one relationship between two tables with the same grain
- D. Single-direction filter from dimension to fact
- E. One-to-many relationship from the dimension to the fact

### 32. A visual on a dimension table does not respond when a fact visual is selected. Which setting decides that behaviour?

Domain: Model the data

- A. Single-direction filter from dimension to fact
- B. Bi-directional cross-filtering on the relationship
- C. Inactive relationship activated with USERELATIONSHIP
- D. Set the cross-filter direction on the relationship

### 33. The model has a proper date table, but the engine still treats a fact date column as its date source. What should be done?

Domain: Model the data

- A. Create a dedicated date table marked as the date table
- B. Build the fiscal periods as columns in the date table
- C. Mark the table as a date table
- D. Create one date table and role-play it through several relationships

### 34. The organization's year runs April to March, and reports keep showing calendar quarters. What must be added?

Domain: Model the data

- A. Build the fiscal periods as columns in the date table
- B. Mark the table as a date table
- C. Create one date table and role-play it through several relationships
- D. Create a dedicated date table marked as the date table

### 35. A report needs reliable year-to-date and year-over-year values for every page. Which sequence delivers that?

Domain: Model the data

- A. Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it
- B. Create one date table per date column → relate all of them to the fact
- C. Use the fact date column directly → write TOTALYTD → add a date slicer
- D. Create a date table → leave it unrelated → filter with it

### 36. A measure returns the same value on every row of a matrix, and the author expected each row to differ. What explains the result?

Domain: Model the data

- A. Create a measure for the aggregation
- B. The filter context supplied by the visual, slicers, and page filters
- C. The row context inside an iterator
- D. Create a calculated column

### 37. A margin measure shows an error wherever revenue is zero. What should be used?

Domain: Model the data

- A. Use an iterator such as SUMX over the row-level expression
- B. Use DIVIDE instead of the division operator
- C. Use DISTINCT COUNT for unique entities
- D. Use an iterator function for row-level arithmetic

### 38. A report needs the number of unique customers and a revenue-per-unit figure that multiplies before it sums. Which two functions fit? Select two.

Domain: Model the data

- A. Use an iterator function for row-level arithmetic
- B. Create a measure for the aggregation
- C. Use an iterator such as SUMX over the row-level expression
- D. Use DIVIDE instead of the division operator
- E. Use DISTINCT COUNT for unique entities

### 39. A percent-of-total measure must honour the region the reader selected but ignore the visual's category grouping. Which modifier fits?

Domain: Model the data

- A. Remove the filter with REMOVEFILTERS or ALL
- B. Use ALLSELECTED to respect the slicer but ignore the visual
- C. Use ALL on the table to clear its filters
- D. Add KEEPFILTERS to intersect rather than replace the filter

### 40. A measure that should stay inside the selected year is returning values from every year. Which modifier fixes it?

Domain: Model the data

- A. Use ALLSELECTED to respect the slicer but ignore the visual
- B. Remove the filter with REMOVEFILTERS or ALL
- C. Use ALL on the table to clear its filters
- D. Add KEEPFILTERS to intersect rather than replace the filter

### 41. A complex measure repeats the same filter expression three times, and the author fears the copies have drifted. What should be used?

Domain: Model the data

- A. Add KEEPFILTERS to intersect rather than replace the filter
- B. Wrap the aggregation in CALCULATE to change the filter context
- C. Use ALL on the table to clear its filters
- D. Store intermediate results in VAR and RETURN

### 42. A share-of-category measure must compare each product with its whole category regardless of the product filter. Which modifier fits?

Domain: Model the data

- A. Use ALLSELECTED to respect the slicer but ignore the visual
- B. Remove the filter with REMOVEFILTERS or ALL
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Wrap the aggregation in CALCULATE to change the filter context

### 43. A report needs cumulative revenue from the start of the fiscal year to the selected date. Which pattern fits?

Domain: Model the data

- A. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- B. Use TOTALYTD or DATESYTD for year-to-date
- C. Use AVERAGEX over a rolling date window
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance

### 44. A monthly review needs cumulative revenue and the same figure for the equivalent month last year. Which two patterns are required? Select two.

Domain: Model the data

- A. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- B. Use TOTALYTD or DATESYTD for year-to-date
- C. Use DATESINPERIOD for a windowed calculation
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- E. Use AVERAGEX over a rolling date window

### 45. An author needs a running total and does not want to hand-write the DAX. What should be used?

Domain: Model the data

- A. Create a numeric range parameter for scenario analysis
- B. Create a calculation group for the time-intelligence variants
- C. Create a field parameter so the author can switch the measure or axis
- D. Use a quick measure for the standard pattern

### 46. One page must let readers switch between revenue and margin, and test a price-change assumption. Which two features fit? Select two.

Domain: Model the data

- A. Use a quick measure for the standard pattern
- B. Use PERCENTILE.INC for a distribution boundary
- C. Create a calculation group for the time-intelligence variants
- D. Create a numeric range parameter for scenario analysis
- E. Create a field parameter so the author can switch the measure or axis

### 47. A service team must state the response time below which 95 percent of tickets fall. What should be used?

Domain: Model the data

- A. Use a quick measure for the standard pattern
- B. Create a calculation group for the time-intelligence variants
- C. Use a statistical function such as STDEV.P or MEDIAN to describe the spread
- D. Use PERCENTILE.INC for a distribution boundary

### 48. A report page takes 30 seconds, and the author needs to know which visual is responsible. What should be used?

Domain: Model the data

- A. Inspect the query plan in DAX query view
- B. Reduce the granularity loaded into the model
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Run Performance Analyzer to find the slow visual

### 49. A model is several gigabytes, and a consultant proposes rewriting every DAX measure first. What should be examined first?

Domain: Model the data

- A. Add an aggregation table for the large fact
- B. Remove unnecessary rows and columns before optimizing measures
- C. Remove the high-cardinality columns the report does not use
- D. Reduce the granularity loaded into the model

### 50. A single measure is suspected of generating an expensive query, and the author needs to inspect the generated query plan. What should be used?

Domain: Model the data

- A. Inspect the query plan in DAX query view
- B. Add an aggregation table for the large fact
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Run Performance Analyzer to find the slow visual

### 51. A weekly executive page needs a revenue trend and progress against a quarterly target. Which two visuals fit? Select two.

Domain: Visualize and analyze the data

- A. A clustered bar or column chart
- B. A line chart with a date axis
- C. A matrix visual with row and column groups
- D. A gauge visual
- E. A KPI visual with a target

### 52. A page must show the share of four product families in total revenue. Which visual fits?

Domain: Visualize and analyze the data

- A. A pie or donut chart
- B. A treemap
- C. A waterfall chart
- D. A clustered bar or column chart

### 53. A sales team must show how many opportunities survive each stage of the pipeline. Which visual fits?

Domain: Visualize and analyze the data

- A. A waterfall chart
- B. A gauge visual
- C. A funnel chart
- D. A scatter chart

### 54. Readers need an obvious control on the page for choosing a year. What should be added?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. Set the filter pane scope by page, report, or visual
- C. A slicer on the report page
- D. Edit the interactions so the visual does not filter the others

### 55. The same region filter must stay applied as readers move across five report pages. What should be configured?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Set the filter pane scope by page, report, or visual
- C. Sync the slicer across the pages that share the same filter
- D. A slicer on the report page

### 56. Selecting a bar on the summary page is filtering the detail visuals and confusing readers. What should be changed?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. Edit the interactions so the visual does not filter the others
- C. Set the filter pane scope by page, report, or visual
- D. A slicer on the report page

### 57. One filter must cover all pages of the report instead of only the page in view. Where should it be placed?

Domain: Visualize and analyze the data

- A. A slicer on the report page
- B. Sync the slicer across the pages that share the same filter
- C. Set the filter pane scope by page, report, or visual
- D. Edit the interactions so the visual does not filter the others

### 58. A report will grow to fifteen pages and needs consistent navigation without manual maintenance. What should be used?

Domain: Visualize and analyze the data

- A. Add buttons with actions that navigate or apply a bookmark
- B. Capture the view in a bookmark
- C. Add a page navigator for the report
- D. Use the Selection pane to group and layer visuals

### 59. A single page must present three saved views controlled by buttons. Which sequence works?

Domain: Visualize and analyze the data

- A. Capture a bookmark before setting the filters → expect it to restore them
- B. Create a page per view → duplicate the visuals → maintain each page
- C. Use buttons without actions → tell readers to click twice
- D. Create the views → capture each in a bookmark → add buttons → hide the visuals not in use

### 60. Two saved views exist as bookmarks, and readers must switch between them with one click. What should be added?

Domain: Visualize and analyze the data

- A. Capture the view in a bookmark
- B. Add a page navigator for the report
- C. Use the Selection pane to group and layer visuals
- D. Add buttons with actions that navigate or apply a bookmark

### 61. A reader must click a customer on a summary page and open a detail page about that customer. What should be configured?

Domain: Visualize and analyze the data

- A. Configure a drillthrough page with the entity filter
- B. Enable drill-down through the hierarchy
- C. Set the filter pane scope by page, report, or visual
- D. Edit the interactions so the visual does not filter the others

### 62. A hover must show three related measures without adding a visual to the page. Which two actions deliver that? Select two.

Domain: Visualize and analyze the data

- A. Configure a drillthrough page with the entity filter
- B. Build a custom tooltip page
- C. Use the Selection pane to group and layer visuals
- D. Set the tooltip to a report page and size it to the hover area
- E. Enable drill-down through the hierarchy

### 63. A team is building its first drillthrough page for a retail summary. Which sequence works?

Domain: Visualize and analyze the data

- A. Set the drillthrough filter → publish → skip the back button
- B. Choose the entity field → create the drillthrough page → place the entity filter → add a back button
- C. Put every field on the summary visual → expect drillthrough to work
- D. Create the detail page → add a visual → tell readers to filter it manually

### 64. A single chart must let the reader go from year down to quarter and then month without opening another visual. What should be enabled?

Domain: Visualize and analyze the data

- A. Enable drill-down through the hierarchy
- B. Build a custom tooltip page
- C. Edit the interactions so the visual does not filter the others
- D. Configure a drillthrough page with the entity filter

### 65. A report must be usable by screen-reader users, and the visuals have no descriptions. What must be added?

Domain: Visualize and analyze the data

- A. Set a logical tab order for the interactive elements
- B. Enable personalization for the visuals the reader may change
- C. Build the mobile layout in the mobile view
- D. Provide alt text for each meaningful visual

### 66. Field engineers will open the report on a phone and only need two measures first. What should be built?

Domain: Visualize and analyze the data

- A. Provide alt text for each meaningful visual
- B. Enable personalization for the visuals the reader may change
- C. Build the mobile layout in the mobile view
- D. Configure the export and download settings for the report

### 67. Readers want to switch a visual from a bar to a line without edit rights. What should be enabled?

Domain: Visualize and analyze the data

- A. Configure the export and download settings for the report
- B. Provide alt text for each meaningful visual
- C. Build the mobile layout in the mobile view
- D. Enable personalization for the visuals the reader may change

### 68. Forty visuals must share one palette and font without individual styling. What should be applied?

Domain: Visualize and analyze the data

- A. Apply conditional formatting driven by a measure
- B. Use the Selection pane to group and layer visuals
- C. Apply a report theme JSON
- D. Set the axis range and units explicitly

### 69. A table must highlight stores whose margin falls below a threshold. What should be applied?

Domain: Visualize and analyze the data

- A. Apply conditional formatting driven by a measure
- B. Set the axis range and units explicitly
- C. Use the Selection pane to group and layer visuals
- D. Apply a report theme JSON

### 70. Overlapping visuals must be layered deliberately, and a bar chart axis must not start at a misleading value. Which two settings are required? Select two.

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Turn on and format data labels
- C. Set the axis range and units explicitly
- D. Apply a report theme JSON
- E. Apply conditional formatting driven by a measure

### 71. Order values must be shown as ranges so the distribution becomes readable. What should be used?

Domain: Visualize and analyze the data

- A. Use clustering to find segments in the data
- B. Create bins for a continuous measure
- C. Create groups for the categories that matter
- D. Use the built-in forecast on a line chart

### 72. A stable monthly series must be projected two quarters ahead with a confidence band. What should be used?

Domain: Visualize and analyze the data

- A. Use the built-in forecast on a line chart
- B. Add a reference line for the target or average
- C. Use the Analyze feature to explain a change
- D. Add error bars to show the uncertainty range

### 73. A retention team must know which factors are associated with churn. Which visual fits?

Domain: Visualize and analyze the data

- A. Use Copilot to create a narrative visual
- B. Use Q&A to answer a natural-language question
- C. Use the Key Influencers visual
- D. Use the Decomposition Tree visual

### 74. A root-cause page must explore any dimension in any order, and executives want a written summary. Which two features fit? Select two.

Domain: Visualize and analyze the data

- A. Use the Key Influencers visual
- B. Use Copilot to create a narrative visual
- C. Use Q&A to answer a natural-language question
- D. Use the Decomposition Tree visual
- E. Use Copilot to suggest a report page

### 75. Managers want to type a question and get a visual without the author building another page. What should be enabled?

Domain: Visualize and analyze the data

- A. Use the Key Influencers visual
- B. Use Copilot to create a narrative visual
- C. Use Q&A to answer a natural-language question
- D. Use the Decomposition Tree visual

### 76. Four report authors must publish and edit content but must not manage membership. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Member role
- B. Workspace Admin role
- C. Workspace Viewer role
- D. Workspace Contributor role

### 77. Auditors need to read the reports but must not change them. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Viewer role
- B. Workspace Member role
- C. Workspace Contributor role
- D. Workspace Admin role

### 78. A workspace owner is leaving, and the team must decide who manages membership and who may add lower-privileged users. Which two roles cover that? Select two.

Domain: Manage and secure Power BI

- A. Workspace Contributor role
- B. Workspace Admin role
- C. Publish an app from the workspace
- D. Workspace Member role
- E. Workspace Viewer role

### 79. A team is publishing its first app to two audiences. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Build in the workspace → curate the app pages → assign audiences → publish and update the app
- B. Publish the app before the report is finished → update it never
- C. Create one app per person → assign each audience manually
- D. Give every consumer the workspace Viewer role → skip the app

### 80. A report was changed in the workspace, but consumers still see the old version. What was missed?

Domain: Manage and secure Power BI

- A. Define an app audience for each group of consumers
- B. Update the app after changing the workspace content
- C. Choose the distribution method that matches the audience
- D. Publish an app from the workspace

### 81. A board wants a single canvas that combines pinned metrics from three separate reports. What should be created?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Create a dashboard in the service
- C. Create a data alert on a dashboard tile
- D. Pin the visual to a dashboard tile

### 82. A director wants the sales report as an email snapshot every Monday at 7 a.m. What should be configured?

Domain: Manage and secure Power BI

- A. Create a data alert on a dashboard tile
- B. Set the alert threshold on the pinned card tile
- C. Pin the visual to a dashboard tile
- D. Create a subscription for the report or dashboard

### 83. A manager must be notified when daily revenue falls below a threshold. What should be created?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Pin the visual to a dashboard tile
- C. Set the alert threshold on the pinned card tile
- D. Create a data alert on a dashboard tile

### 84. A three-year fact must refresh in under ten minutes, and only recent partitions change. Which two steps are required? Select two.

Domain: Manage and secure Power BI

- A. Install an on-premises data gateway
- B. Configure incremental refresh with the range parameters
- C. Configure scheduled refresh on the semantic model
- D. Set the RangeStart and RangeEnd parameters the refresh policy expects
- E. Update the credentials used by the refresh schedule

### 85. Refresh is being scheduled for a newly published model for the first time. Which sequence avoids a silent failure?

Domain: Manage and secure Power BI

- A. Set the schedule → publish → wait for the first failure email
- B. Confirm the gateway or cloud connection → store credentials → set the schedule → check refresh history
- C. Use a personal gateway → schedule → leave the team to maintain it
- D. Increase the refresh frequency to hourly → ignore the source load

### 86. Regional managers must see only their own region's rows in one shared report. What should be created?

Domain: Manage and secure Power BI

- A. Test the role with View as role in the service
- B. Add the security group to the role membership
- C. Use a dynamic RLS rule based on USERPRINCIPALNAME
- D. Define a row-level security role with a DAX filter

### 87. Four hundred users must be filtered through a mapping table rather than a role per person. What should be used?

Domain: Manage and secure Power BI

- A. Map the signed-in user with USERPRINCIPALNAME in the filter
- B. Use a dynamic RLS rule based on USERPRINCIPALNAME
- C. Define a row-level security role with a DAX filter
- D. A static RLS role per region with fixed members

### 88. One semantic model should become the organization standard that other teams can trust. What should be done?

Domain: Manage and secure Power BI

- A. Grant Build permission on the semantic model
- B. Promote the content as endorsed
- C. Grant item-level access to the specific report
- D. Certify the semantic model

---

## Case study — Litware Financial

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A regional manager must rank twelve branches by revenue. Which visual fits?

Domain: Visualize and analyze the data

- A. A clustered bar or column chart
- B. A pie or donut chart
- C. A treemap
- D. A line chart with a date axis

### 90. Readers need a reset control that restores the default filters and visible visuals. What should be captured?

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Add a page navigator for the report
- C. Capture the view in a bookmark
- D. Add buttons with actions that navigate or apply a bookmark

### 91. A trend chart must show whether each month beat the target cost-to-income percentage. What should be added?

Domain: Visualize and analyze the data

- A. Add error bars to show the uncertainty range
- B. Create groups for the categories that matter
- C. Use the built-in forecast on a line chart
- D. Add a reference line for the target or average

---

## Case study — Proseware Health

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. A single encounter table repeats patient region, clinic, and payer on every row, and slicers are slow. What should be built?

Domain: Model the data

- A. Set the table and column properties, including hidden keys and format strings
- B. Flatten the lookup attributes into a single dimension
- C. Build a star schema with a fact table and conformed dimensions
- D. Normalize the dimension into a snowflake

### 93. Year-to-date admission totals skip days when no activity was recorded, and the running figure resets oddly. What is missing?

Domain: Model the data

- A. Mark the table as a date table
- B. Build the fiscal periods as columns in the date table
- C. Create a dedicated date table marked as the date table
- D. Create one date table and role-play it through several relationships

### 94. Bed-days available is being summed across months and shows a meaningless peak. What should the measure do instead?

Domain: Model the data

- A. Use TOTALYTD or DATESYTD for year-to-date
- B. Use AVERAGEX over a rolling date window
- C. Use LASTNONBLANK when the balance is only recorded on some dates
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance

---

## Case study — Thornbury Consulting

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. One app must show sales pages to sales staff and finance pages to finance staff. What should be configured?

Domain: Manage and secure Power BI

- A. Choose the distribution method that matches the audience
- B. Update the app after changing the workspace content
- C. Define an app audience for each group of consumers
- D. Publish an app from the workspace

### 96. The model refreshes from an on-premises SQL Server that the cloud service cannot reach. What is required?

Domain: Manage and secure Power BI

- A. Configure scheduled refresh on the semantic model
- B. Personal mode gateway
- C. Virtual network data gateway
- D. Install an on-premises data gateway

### 97. Exported files must retain their protection after they leave the workspace. What should be applied?

Domain: Manage and secure Power BI

- A. Apply a sensitivity label to the semantic model and report
- B. Promote the content as endorsed
- C. Certify the semantic model
- D. Grant item-level access to the specific report

---

## Case study — Wingfield Retail

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. A new analyst must build a sales report without creating a second definition of net sales. Which action fits?

Domain: Prepare the data

- A. DirectQuery
- B. Connect to a shared semantic model instead of importing the source again
- C. Import mode
- D. DirectLake over a lakehouse

### 99. A buying manager asks whether order values are dominated by a few large suppliers. Which evidence answers that?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Correct the column data type before building the model
- C. Review column statistics and value distribution
- D. Profile the column with column quality, distribution, and profile views

### 100. A transactional sales table must become one row per store per day, and the sales column must be numeric. Which two steps are required? Select two.

Domain: Prepare the data

- A. Add a conditional column for rule-based bucketing
- B. Extract the needed part of the text with a delimiter or position
- C. Correct the column data type before building the model
- D. Add a custom column with an M expression
- E. Group by the key and aggregate the measures

---

## Answer key and explanations

### Question 1 — B

Answer: DirectQuery. DirectQuery queries the source at report time, which is what a one-minute freshness requirement demands. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery queries the source at report time, which is what a one-minute freshness requirement demands.
- **B:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery queries the source at report time, which is what a one-minute freshness requirement demands.
- **C:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: DirectQuery queries the source at report time, which is what a one-minute freshness requirement demands.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery queries the source at report time, which is what a one-minute freshness requirement demands.

### Question 2 — C, E

Answers: DirectQuery; Import mode. Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported.
- **B:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported.
- **C:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported.
- **D:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported.
- **E:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: Near-real-time stock needs DirectQuery, and the nightly finance snapshot is best imported.

### Question 3 — A

Answer: Change the data source settings rather than rebuilding the query. Editing the data source settings repoints the query without rebuilding its steps. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. In this case: Editing the data source settings repoints the query without rebuilding its steps.
- **B:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: Editing the data source settings repoints the query without rebuilding its steps.
- **C:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Editing the data source settings repoints the query without rebuilding its steps.
- **D:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Editing the data source settings repoints the query without rebuilding its steps.

### Question 4 — D

Answer: DirectLake over a lakehouse. DirectLake reads the Delta tables directly, which gives that speed when capacity and the table format allow it. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectLake reads the Delta tables directly, which gives that speed when capacity and the table format allow it.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectLake reads the Delta tables directly, which gives that speed when capacity and the table format allow it.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: DirectLake reads the Delta tables directly, which gives that speed when capacity and the table format allow it.
- **D:** Correct. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. In this case: DirectLake reads the Delta tables directly, which gives that speed when capacity and the table format allow it.

### Question 5 — A

Answer: Import mode. Import moves the query load off the source and gives the fastest reports. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import moves the query load off the source and gives the fastest reports.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Import moves the query load off the source and gives the fastest reports.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import moves the query load off the source and gives the fastest reports.
- **D:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import moves the query load off the source and gives the fastest reports.

### Question 6 — C

Answer: Dual mode table. A Dual dimension can satisfy some queries from memory instead of going back to the source. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: A Dual dimension can satisfy some queries from memory instead of going back to the source.
- **B:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: A Dual dimension can satisfy some queries from memory instead of going back to the source.
- **C:** Correct. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. In this case: A Dual dimension can satisfy some queries from memory instead of going back to the source.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: A Dual dimension can satisfy some queries from memory instead of going back to the source.

### Question 7 — A

Answer: Create a parameter for the server, path, or filter. A parameter lets the same query swap environments by changing one value. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. In this case: A parameter lets the same query swap environments by changing one value.
- **B:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: A parameter lets the same query swap environments by changing one value.
- **C:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: A parameter lets the same query swap environments by changing one value.
- **D:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: A parameter lets the same query swap environments by changing one value.

### Question 8 — A

Answer: Update the data source credentials in the semantic model settings. The stored credential in the data source settings is what the service uses for refresh. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. In this case: The stored credential in the data source settings is what the service uses for refresh.
- **B:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: The stored credential in the data source settings is what the service uses for refresh.
- **C:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: The stored credential in the data source settings is what the service uses for refresh.
- **D:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: The stored credential in the data source settings is what the service uses for refresh.

### Question 9 — D

Answer: Set privacy levels to isolate the sources. Privacy levels stop the engine combining data across sources that should stay separate. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: Privacy levels stop the engine combining data across sources that should stay separate.
- **B:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Privacy levels stop the engine combining data across sources that should stay separate.
- **C:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Privacy levels stop the engine combining data across sources that should stay separate.
- **D:** Correct. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. In this case: Privacy levels stop the engine combining data across sources that should stay separate.

### Question 10 — A

Answer: Profile the column with column quality, distribution, and profile views. Profiling shows valid, distinct, and empty values per column before any transformation is chosen. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. In this case: Profiling shows valid, distinct, and empty values per column before any transformation is chosen.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Profiling shows valid, distinct, and empty values per column before any transformation is chosen.
- **C:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Profiling shows valid, distinct, and empty values per column before any transformation is chosen.
- **D:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: Profiling shows valid, distinct, and empty values per column before any transformation is chosen.

### Question 11 — A

Answer: Correct the column data type before building the model. A text date cannot drive time intelligence, so the type must be corrected before the model is built. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: A text date cannot drive time intelligence, so the type must be corrected before the model is built.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be corrected before the model is built.
- **C:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be corrected before the model is built.
- **D:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be corrected before the model is built.

### Question 12 — B

Answer: Profile the source → fix types and nulls → shape the table → load only the needed columns. Profiling comes before shaping, and loading only the needed columns keeps the model small. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Patching visuals hides the data problem instead of fixing it at the source. Why the correct answer wins: Profiling comes before shaping, and loading only the needed columns keeps the model small.
- **B:** Correct. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. In this case: Profiling comes before shaping, and loading only the needed columns keeps the model small.
- **C:** Incorrect for this question. Discovering type errors after load means the model was built on wrong data and the work restarts. Why the correct answer wins: Profiling comes before shaping, and loading only the needed columns keeps the model small.
- **D:** Incorrect for this question. Deleting profiling removes the evidence of quality problems and loading every column inflates the model. Why the correct answer wins: Profiling comes before shaping, and loading only the needed columns keeps the model small.

### Question 13 — A

Answer: Replace nulls with a defined placeholder or a filled-down value. Replacing nulls with a defined value makes the aggregation reproducible and the assumption documented. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: Replacing nulls with a defined value makes the aggregation reproducible and the assumption documented.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Replacing nulls with a defined value makes the aggregation reproducible and the assumption documented.
- **C:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Replacing nulls with a defined value makes the aggregation reproducible and the assumption documented.
- **D:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Replacing nulls with a defined value makes the aggregation reproducible and the assumption documented.

### Question 14 — D, E

Answers: Replace nulls with a defined placeholder or a filled-down value; Remove duplicate rows using the natural business key. De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct.
- **C:** Incorrect for this question. A locale-aware conversion stops day and month being swapped and stops decimal commas being interpreted as text. Why the correct answer wins: De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct.
- **D:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct.
- **E:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: De-duplicating on the order key removes the repeats, and a defined null replacement makes freight totals correct.

### Question 15 — B

Answer: Remove duplicate rows using the natural business key. The same business key is being loaded twice, so de-duplicating on that key reverses the inflation. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **B:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **C:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.
- **D:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: The same business key is being loaded twice, so de-duplicating on that key reverses the inflation.

### Question 16 — D

Answer: Identify the bad values → standardize text → convert types → document what was replaced. Standardizing text before conversion fixes the cause, and documenting the replacement keeps it auditable. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Converting before trimming fails on values that only differ by whitespace and leaves duplicates behind. Why the correct answer wins: Standardizing text before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **B:** Incorrect for this question. Silently dropping rows changes the totals and the business never learns what is missing. Why the correct answer wins: Standardizing text before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **C:** Incorrect for this question. Replacing everything with a default destroys real values and hides the pattern behind the error. Why the correct answer wins: Standardizing text before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **D:** Correct. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. In this case: Standardizing text before conversion fixes the cause, and documenting the replacement keeps it auditable.

### Question 17 — C

Answer: Add a custom column with an M expression. A custom column concatenates the two fields row by row. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: A custom column concatenates the two fields row by row.
- **B:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: A custom column concatenates the two fields row by row.
- **C:** Correct. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. In this case: A custom column concatenates the two fields row by row.
- **D:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A custom column concatenates the two fields row by row.

### Question 18 — C

Answer: Add a conditional column for rule-based bucketing. A conditional column applies the published thresholds explicitly and is easy to review. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: A conditional column applies the published thresholds explicitly and is easy to review.
- **B:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: A conditional column applies the published thresholds explicitly and is easy to review.
- **C:** Correct. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. In this case: A conditional column applies the published thresholds explicitly and is easy to review.
- **D:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A conditional column applies the published thresholds explicitly and is easy to review.

### Question 19 — A

Answer: Extract the needed part of the text with a delimiter or position. Extracting by position keeps the prefix without importing the whole identifier twice. Extraction keeps the useful part of an identifier without importing the whole string into the model. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Extraction keeps the useful part of an identifier without importing the whole string into the model. In this case: Extracting by position keeps the prefix without importing the whole identifier twice.
- **B:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Extracting by position keeps the prefix without importing the whole identifier twice.
- **C:** Incorrect for this question. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Why the correct answer wins: Extracting by position keeps the prefix without importing the whole identifier twice.
- **D:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Extracting by position keeps the prefix without importing the whole identifier twice.

### Question 20 — A

Answer: Unpivot the month columns into rows. Unpivoting turns the month columns into rows, which is the shape a tabular model needs. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. In this case: Unpivoting turns the month columns into rows, which is the shape a tabular model needs.
- **B:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Unpivoting turns the month columns into rows, which is the shape a tabular model needs.
- **C:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Unpivoting turns the month columns into rows, which is the shape a tabular model needs.
- **D:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Unpivoting turns the month columns into rows, which is the shape a tabular model needs.

### Question 21 — B

Answer: Pivot the attribute values into columns. Pivoting turns attribute rows into columns, which produces the wide table the report needs. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Pivoting turns attribute rows into columns, which produces the wide table the report needs.
- **B:** Correct. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. In this case: Pivoting turns attribute rows into columns, which produces the wide table the report needs.
- **C:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Pivoting turns attribute rows into columns, which produces the wide table the report needs.
- **D:** Incorrect for this question. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Why the correct answer wins: Pivoting turns attribute rows into columns, which produces the wide table the report needs.

### Question 22 — B

Answer: Expand the JSON record into typed columns. Expanding the record exposes the nested fields as columns that can be typed and modelled. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Converting a list to a table preserves every element as a row instead of keeping only the first value. Why the correct answer wins: Expanding the record exposes the nested fields as columns that can be typed and modelled.
- **B:** Correct. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. In this case: Expanding the record exposes the nested fields as columns that can be typed and modelled.
- **C:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Expanding the record exposes the nested fields as columns that can be typed and modelled.
- **D:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Expanding the record exposes the nested fields as columns that can be typed and modelled.

### Question 23 — B

Answer: Append the queries into one table. Appending stacks rows of the same shape, which is exactly what monthly files are. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: Appending stacks rows of the same shape, which is exactly what monthly files are.
- **B:** Correct. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. In this case: Appending stacks rows of the same shape, which is exactly what monthly files are.
- **C:** Incorrect for this question. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. Why the correct answer wins: Appending stacks rows of the same shape, which is exactly what monthly files are.
- **D:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: Appending stacks rows of the same shape, which is exactly what monthly files are.

### Question 24 — C, E

Answers: Merge the two queries on a matching key; Use a left outer join to keep every fact row. A merge adds the category column, and a left outer join keeps unmatched fact rows. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Why the correct answer wins: A merge adds the category column, and a left outer join keeps unmatched fact rows.
- **B:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: A merge adds the category column, and a left outer join keeps unmatched fact rows.
- **C:** Correct. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. In this case: A merge adds the category column, and a left outer join keeps unmatched fact rows.
- **D:** Incorrect for this question. A single integer key is compact, stable, and avoids relationships built on text or composite columns. Why the correct answer wins: A merge adds the category column, and a left outer join keeps unmatched fact rows.
- **E:** Correct. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. In this case: A merge adds the category column, and a left outer join keeps unmatched fact rows.

### Question 25 — C, D

Answers: Keep the steps foldable so the source does the work; Reuse a dataflow for the shared transformation. A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Staging separates extraction from transformation, which makes each layer easier to test and reuse. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **B:** Incorrect for this question. A native query reduces what is transferred, but it can break folding for later steps and must be maintained as the schema changes. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **C:** Correct. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **D:** Correct. A dataflow centralizes preparation so several models consume one governed set of cleaned tables. In this case: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.
- **E:** Incorrect for this question. A duplicate copies the full step chain, so a change in one copy does not affect the other but the work is repeated. Why the correct answer wins: A dataflow centralizes the transformation once, and keeping steps foldable lets the source do the work.

### Question 26 — A, B

Answers: Set the table and column properties, including hidden keys and format strings; Hide technical columns from the report view. Hiding technical keys removes them from the field list, and format strings control how values display. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. In this case: Hiding technical keys removes them from the field list, and format strings control how values display.
- **B:** Correct. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. In this case: Hiding technical keys removes them from the field list, and format strings control how values display.
- **C:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Hiding technical keys removes them from the field list, and format strings control how values display.
- **D:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Hiding technical keys removes them from the field list, and format strings control how values display.
- **E:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Hiding technical keys removes them from the field list, and format strings control how values display.

### Question 27 — C

Answer: Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact. Agreeing the grain first decides what a row means, and separating descriptive attributes is what makes the star work. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A single wide table cannot be filtered cleanly by dimension and pushes duplication into every row. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes is what makes the star work.
- **B:** Incorrect for this question. Relationships built before the grain is agreed will be wrong and must be rebuilt. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes is what makes the star work.
- **C:** Correct. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. In this case: Agreeing the grain first decides what a row means, and separating descriptive attributes is what makes the star work.
- **D:** Incorrect for this question. A dimension per column produces a hub of one-column tables and makes the model unmaintainable. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes is what makes the star work.

### Question 28 — B

Answer: Flatten the lookup attributes into a single dimension. Flattening the lookup attributes into the customer dimension removes the hop. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Flattening the lookup attributes into the customer dimension removes the hop.
- **B:** Correct. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. In this case: Flattening the lookup attributes into the customer dimension removes the hop.
- **C:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: Flattening the lookup attributes into the customer dimension removes the hop.
- **D:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Flattening the lookup attributes into the customer dimension removes the hop.

### Question 29 — C

Answer: Inactive relationship activated with USERELATIONSHIP. Only one relationship between two tables can be active, so the second stays inactive until a measure activates it. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: Only one relationship between two tables can be active, so the second stays inactive until a measure activates it.
- **B:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Only one relationship between two tables can be active, so the second stays inactive until a measure activates it.
- **C:** Correct. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. In this case: Only one relationship between two tables can be active, so the second stays inactive until a measure activates it.
- **D:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Only one relationship between two tables can be active, so the second stays inactive until a measure activates it.

### Question 30 — C

Answer: Many-to-many relationship with a bridging table. The bridge table resolves the many-to-many and keeps the filter path explicit. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the filter path explicit.
- **B:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the filter path explicit.
- **C:** Correct. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. In this case: The bridge table resolves the many-to-many and keeps the filter path explicit.
- **D:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: The bridge table resolves the many-to-many and keeps the filter path explicit.

### Question 31 — D, E

Answers: One-to-many relationship from the dimension to the fact; Single-direction filter from dimension to fact. One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable.
- **B:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable.
- **C:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable.
- **D:** Correct. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. In this case: One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable.
- **E:** Correct. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. In this case: One-to-many from dimension to fact is the standard shape, and single-direction filtering keeps the path predictable.

### Question 32 — D

Answer: Set the cross-filter direction on the relationship. Cross-filter direction on the relationship decides whether the fact can filter the dimension. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Cross-filter direction on the relationship decides whether the fact can filter the dimension.
- **B:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Cross-filter direction on the relationship decides whether the fact can filter the dimension.
- **C:** Incorrect for this question. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Why the correct answer wins: Cross-filter direction on the relationship decides whether the fact can filter the dimension.
- **D:** Correct. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. In this case: Cross-filter direction on the relationship decides whether the fact can filter the dimension.

### Question 33 — C

Answer: Mark the table as a date table. Marking the table as the date table removes that ambiguity. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Marking the table as the date table removes that ambiguity.
- **B:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: Marking the table as the date table removes that ambiguity.
- **C:** Correct. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. In this case: Marking the table as the date table removes that ambiguity.
- **D:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Marking the table as the date table removes that ambiguity.

### Question 34 — A

Answer: Build the fiscal periods as columns in the date table. Fiscal period columns let time intelligence follow the organization's year. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. In this case: Fiscal period columns let time intelligence follow the organization's year.
- **B:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: Fiscal period columns let time intelligence follow the organization's year.
- **C:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Fiscal period columns let time intelligence follow the organization's year.
- **D:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Fiscal period columns let time intelligence follow the organization's year.

### Question 35 — A

Answer: Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it. Marking and relating the date table is what makes the measures respond correctly to date slicers. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. In this case: Marking and relating the date table is what makes the measures respond correctly to date slicers.
- **B:** Incorrect for this question. Several date tables multiply relationships and make every time measure ambiguous. Why the correct answer wins: Marking and relating the date table is what makes the measures respond correctly to date slicers.
- **C:** Incorrect for this question. A fact date column has gaps, so year-to-date silently skips missing days and the slicer shows no clean hierarchy. Why the correct answer wins: Marking and relating the date table is what makes the measures respond correctly to date slicers.
- **D:** Incorrect for this question. An unrelated date table filters nothing, so the slicer appears to work while the visuals ignore it. Why the correct answer wins: Marking and relating the date table is what makes the measures respond correctly to date slicers.

### Question 36 — B

Answer: The filter context supplied by the visual, slicers, and page filters. The measure is evaluated in the filter context the visual supplies, so the row grouping must reach it through the model. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: The measure is evaluated in the filter context the visual supplies, so the row grouping must reach it through the model.
- **B:** Correct. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. In this case: The measure is evaluated in the filter context the visual supplies, so the row grouping must reach it through the model.
- **C:** Incorrect for this question. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. Why the correct answer wins: The measure is evaluated in the filter context the visual supplies, so the row grouping must reach it through the model.
- **D:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: The measure is evaluated in the filter context the visual supplies, so the row grouping must reach it through the model.

### Question 37 — B

Answer: Use DIVIDE instead of the division operator. DIVIDE returns blank instead of an error when the denominator is zero. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. Why the correct answer wins: DIVIDE returns blank instead of an error when the denominator is zero.
- **B:** Correct. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. In this case: DIVIDE returns blank instead of an error when the denominator is zero.
- **C:** Incorrect for this question. Distinct count answers how many unique customers or orders, which a plain count would overstate. Why the correct answer wins: DIVIDE returns blank instead of an error when the denominator is zero.
- **D:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: DIVIDE returns blank instead of an error when the denominator is zero.

### Question 38 — C, E

Answers: Use DISTINCT COUNT for unique entities; Use an iterator such as SUMX over the row-level expression. DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating. Distinct count answers how many unique customers or orders, which a plain count would overstate. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating.
- **B:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating.
- **C:** Correct. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. In this case: DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating.
- **D:** Incorrect for this question. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. Why the correct answer wins: DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating.
- **E:** Correct. Distinct count answers how many unique customers or orders, which a plain count would overstate. In this case: DISTINCT COUNT answers the unique-entity question, and SUMX evaluates the row-level arithmetic before aggregating.

### Question 39 — B

Answer: Use ALLSELECTED to respect the slicer but ignore the visual. ALLSELECTED respects the slicer selection while removing the visual's own filter. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALLSELECTED respects the slicer selection while removing the visual's own filter.
- **B:** Correct. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. In this case: ALLSELECTED respects the slicer selection while removing the visual's own filter.
- **C:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: ALLSELECTED respects the slicer selection while removing the visual's own filter.
- **D:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALLSELECTED respects the slicer selection while removing the visual's own filter.

### Question 40 — D

Answer: Add KEEPFILTERS to intersect rather than replace the filter. KEEPFILTERS intersects the new filter with the existing one instead of replacing it. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one instead of replacing it.
- **B:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one instead of replacing it.
- **C:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one instead of replacing it.
- **D:** Correct. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. In this case: KEEPFILTERS intersects the new filter with the existing one instead of replacing it.

### Question 41 — D

Answer: Store intermediate results in VAR and RETURN. Variables compute the expression once and make the measure readable. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **B:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **C:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **D:** Correct. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. In this case: Variables compute the expression once and make the measure readable.

### Question 42 — B

Answer: Remove the filter with REMOVEFILTERS or ALL. Removing the product filter lets the denominator cover the whole category. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: Removing the product filter lets the denominator cover the whole category.
- **B:** Correct. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. In this case: Removing the product filter lets the denominator cover the whole category.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Removing the product filter lets the denominator cover the whole category.
- **D:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Removing the product filter lets the denominator cover the whole category.

### Question 43 — B

Answer: Use TOTALYTD or DATESYTD for year-to-date. Year-to-date accumulates from the start of the year defined by the marked date table. Year-to-date functions accumulate from the start of the year defined by the marked date table. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **B:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date accumulates from the start of the year defined by the marked date table.
- **C:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **D:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.

### Question 44 — A, B

Answers: Use TOTALYTD or DATESYTD for year-to-date; Use SAMEPERIODLASTYEAR or DATEADD for the comparable period. Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value. Year-to-date functions accumulate from the start of the year defined by the marked date table. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. In this case: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **B:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **C:** Incorrect for this question. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **D:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.
- **E:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date supplies the cumulative figure, and the comparable-period shift supplies last year's value.

### Question 45 — D

Answer: Use a quick measure for the standard pattern. A quick measure generates the standard pattern, which is faster and less error-prone. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A quick measure generates the standard pattern, which is faster and less error-prone.
- **B:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A quick measure generates the standard pattern, which is faster and less error-prone.
- **C:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A quick measure generates the standard pattern, which is faster and less error-prone.
- **D:** Correct. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. In this case: A quick measure generates the standard pattern, which is faster and less error-prone.

### Question 46 — D, E

Answers: Create a field parameter so the author can switch the measure or axis; Create a numeric range parameter for scenario analysis. A field parameter switches the measure in place, and a numeric range parameter drives the assumption. A field parameter lets one visual switch between measures or dimensions without duplicating pages. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **B:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **C:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **D:** Correct. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **E:** Correct. A field parameter lets one visual switch between measures or dimensions without duplicating pages. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.

### Question 47 — D

Answer: Use PERCENTILE.INC for a distribution boundary. A percentile returns the boundary value, which describes the tail an average hides. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A percentile returns the boundary value, which describes the tail an average hides.
- **B:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A percentile returns the boundary value, which describes the tail an average hides.
- **C:** Incorrect for this question. Descriptive statistics show the shape of the data, which an average alone hides. Why the correct answer wins: A percentile returns the boundary value, which describes the tail an average hides.
- **D:** Correct. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. In this case: A percentile returns the boundary value, which describes the tail an average hides.

### Question 48 — D

Answer: Run Performance Analyzer to find the slow visual. Performance Analyzer times each visual and separates DAX, query, and rendering cost. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **B:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **D:** Correct. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. In this case: Performance Analyzer times each visual and separates DAX, query, and rendering cost.

### Question 49 — B

Answer: Remove unnecessary rows and columns before optimizing measures. Size work starts with what is loaded, because no DAX rewrite compensates for data the report never queries. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: Size work starts with what is loaded, because no DAX rewrite compensates for data the report never queries.
- **B:** Correct. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. In this case: Size work starts with what is loaded, because no DAX rewrite compensates for data the report never queries.
- **C:** Incorrect for this question. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. Why the correct answer wins: Size work starts with what is loaded, because no DAX rewrite compensates for data the report never queries.
- **D:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: Size work starts with what is loaded, because no DAX rewrite compensates for data the report never queries.

### Question 50 — A

Answer: Inspect the query plan in DAX query view. DAX query view shows the query and its timings, which isolates the measure from the visual. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. In this case: DAX query view shows the query and its timings, which isolates the measure from the visual.
- **B:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: DAX query view shows the query and its timings, which isolates the measure from the visual.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: DAX query view shows the query and its timings, which isolates the measure from the visual.
- **D:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: DAX query view shows the query and its timings, which isolates the measure from the visual.

### Question 51 — B, E

Answers: A line chart with a date axis; A KPI visual with a target. A line chart shows the trend, and a KPI visual shows progress against a defined target. A line chart shows a trend over a continuous axis, which is what time series need. A KPI visual states progress against a defined target, which a plain card cannot show. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a defined target.
- **B:** Correct. A line chart shows a trend over a continuous axis, which is what time series need. In this case: A line chart shows the trend, and a KPI visual shows progress against a defined target.
- **C:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a defined target.
- **D:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A line chart shows the trend, and a KPI visual shows progress against a defined target.
- **E:** Correct. A KPI visual states progress against a defined target, which a plain card cannot show. In this case: A line chart shows the trend, and a KPI visual shows progress against a defined target.

### Question 52 — A

Answer: A pie or donut chart. A pie chart shows part-to-whole for a few categories, and four is few enough to read. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. In this case: A pie chart shows part-to-whole for a few categories, and four is few enough to read.
- **B:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A pie chart shows part-to-whole for a few categories, and four is few enough to read.
- **C:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A pie chart shows part-to-whole for a few categories, and four is few enough to read.
- **D:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A pie chart shows part-to-whole for a few categories, and four is few enough to read.

### Question 53 — C

Answer: A funnel chart. A funnel shows stage-by-stage attrition, which is what a pipeline needs. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A funnel shows stage-by-stage attrition, which is what a pipeline needs.
- **B:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A funnel shows stage-by-stage attrition, which is what a pipeline needs.
- **C:** Correct. A funnel shows sequential stage attrition, which suits a sales or process pipeline. In this case: A funnel shows stage-by-stage attrition, which is what a pipeline needs.
- **D:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A funnel shows stage-by-stage attrition, which is what a pipeline needs.

### Question 54 — C

Answer: A slicer on the report page. A slicer puts the control on the canvas where the reader can see it. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: A slicer puts the control on the canvas where the reader can see it.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: A slicer puts the control on the canvas where the reader can see it.
- **C:** Correct. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. In this case: A slicer puts the control on the canvas where the reader can see it.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: A slicer puts the control on the canvas where the reader can see it.

### Question 55 — C

Answer: Sync the slicer across the pages that share the same filter. Syncing the slicer keeps one selection consistent across pages. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **C:** Correct. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. In this case: Syncing the slicer keeps one selection consistent across pages.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.

### Question 56 — B

Answer: Edit the interactions so the visual does not filter the others. Interaction settings decide whether a selection filters, highlights, or does nothing. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **B:** Correct. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. In this case: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **C:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.

### Question 57 — C

Answer: Set the filter pane scope by page, report, or visual. Filter pane scope decides whether a filter applies to the visual, the page, or the whole report. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Filter pane scope decides whether a filter applies to the visual, the page, or the whole report.
- **B:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Filter pane scope decides whether a filter applies to the visual, the page, or the whole report.
- **C:** Correct. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. In this case: Filter pane scope decides whether a filter applies to the visual, the page, or the whole report.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Filter pane scope decides whether a filter applies to the visual, the page, or the whole report.

### Question 58 — C

Answer: Add a page navigator for the report. A page navigator generates navigation from the pages themselves. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **B:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **C:** Correct. A page navigator generates navigation for every page automatically, which stays correct as pages are added. In this case: A page navigator generates navigation from the pages themselves.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A page navigator generates navigation from the pages themselves.

### Question 59 — D

Answer: Create the views → capture each in a bookmark → add buttons → hide the visuals not in use. Bookmarks store state and buttons apply it, which is what makes one page behave like three. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark captures the state at the moment it is created, so filters set afterwards are not stored. Why the correct answer wins: Bookmarks store state and buttons apply it, which is what makes one page behave like three.
- **B:** Incorrect for this question. Duplicating pages multiplies maintenance and the copies drift apart. Why the correct answer wins: Bookmarks store state and buttons apply it, which is what makes one page behave like three.
- **C:** Incorrect for this question. A button with no action is decoration and the report still has no navigation. Why the correct answer wins: Bookmarks store state and buttons apply it, which is what makes one page behave like three.
- **D:** Correct. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. In this case: Bookmarks store state and buttons apply it, which is what makes one page behave like three.

### Question 60 — D

Answer: Add buttons with actions that navigate or apply a bookmark. Buttons with bookmark actions turn a stored view into a single click. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: Buttons with bookmark actions turn a stored view into a single click.
- **B:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: Buttons with bookmark actions turn a stored view into a single click.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Buttons with bookmark actions turn a stored view into a single click.
- **D:** Correct. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. In this case: Buttons with bookmark actions turn a stored view into a single click.

### Question 61 — A

Answer: Configure a drillthrough page with the entity filter. Drillthrough passes the selected entity to a detail page through a filter. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. In this case: Drillthrough passes the selected entity to a detail page through a filter.
- **B:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **C:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.

### Question 62 — B, D

Answers: Build a custom tooltip page; Set the tooltip to a report page and size it to the hover area. A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover.
- **B:** Correct. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover.
- **D:** Correct. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover.
- **E:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it on hover.

### Question 63 — B

Answer: Choose the entity field → create the drillthrough page → place the entity filter → add a back button. The drillthrough filter is what carries the selection, and the back button keeps the reader oriented. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Without a back button the reader is stranded on the detail page and loses the summary context. Why the correct answer wins: The drillthrough filter is what carries the selection, and the back button keeps the reader oriented.
- **B:** Correct. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. In this case: The drillthrough filter is what carries the selection, and the back button keeps the reader oriented.
- **C:** Incorrect for this question. Too many fields on one visual makes the click target ambiguous and the drill result unpredictable. Why the correct answer wins: The drillthrough filter is what carries the selection, and the back button keeps the reader oriented.
- **D:** Incorrect for this question. A page without the drillthrough filter does not carry the selected entity, so the detail is not about what was clicked. Why the correct answer wins: The drillthrough filter is what carries the selection, and the back button keeps the reader oriented.

### Question 64 — A

Answer: Enable drill-down through the hierarchy. Drill-down moves through the hierarchy inside the same visual. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. In this case: Drill-down moves through the hierarchy inside the same visual.
- **B:** Incorrect for this question. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **C:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **D:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.

### Question 65 — D

Answer: Provide alt text for each meaningful visual. Alt text describes each visual for a screen reader. Alt text describes the visual for a screen reader, which is required for an accessible report. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **B:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **D:** Correct. Alt text describes the visual for a screen reader, which is required for an accessible report. In this case: Alt text describes each visual for a screen reader.

### Question 66 — C

Answer: Build the mobile layout in the mobile view. The mobile layout decides what appears first on a phone. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **B:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **C:** Correct. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. In this case: The mobile layout decides what appears first on a phone.
- **D:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: The mobile layout decides what appears first on a phone.

### Question 67 — D

Answer: Enable personalization for the visuals the reader may change. Personalization lets a reader change the visual while the author keeps the published default. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the published default.
- **B:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the published default.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Personalization lets a reader change the visual while the author keeps the published default.
- **D:** Correct. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. In this case: Personalization lets a reader change the visual while the author keeps the published default.

### Question 68 — C

Answer: Apply a report theme JSON. A theme applies a consistent palette across the whole report. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: A theme applies a consistent palette across the whole report.
- **B:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A theme applies a consistent palette across the whole report.
- **C:** Correct. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. In this case: A theme applies a consistent palette across the whole report.
- **D:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: A theme applies a consistent palette across the whole report.

### Question 69 — A

Answer: Apply conditional formatting driven by a measure. Conditional formatting driven by a measure encodes the exception directly. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. In this case: Conditional formatting driven by a measure encodes the exception directly.
- **B:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception directly.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception directly.
- **D:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Conditional formatting driven by a measure encodes the exception directly.

### Question 70 — A, C

Answers: Use the Selection pane to group and layer visuals; Set the axis range and units explicitly. The Selection pane controls layering, and an explicit axis range prevents a misleading scale. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. In this case: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **B:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **C:** Correct. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. In this case: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **D:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.
- **E:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: The Selection pane controls layering, and an explicit axis range prevents a misleading scale.

### Question 71 — B

Answer: Create bins for a continuous measure. Binning turns a continuous measure into ranges. Binning turns a continuous value into ranges, which is how a distribution becomes readable. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Why the correct answer wins: Binning turns a continuous measure into ranges.
- **B:** Correct. Binning turns a continuous value into ranges, which is how a distribution becomes readable. In this case: Binning turns a continuous measure into ranges.
- **C:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: Binning turns a continuous measure into ranges.
- **D:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: Binning turns a continuous measure into ranges.

### Question 72 — A

Answer: Use the built-in forecast on a line chart. Forecasting extends the series statistically and shows the uncertainty band. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. In this case: Forecasting extends the series statistically and shows the uncertainty band.
- **B:** Incorrect for this question. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Why the correct answer wins: Forecasting extends the series statistically and shows the uncertainty band.
- **C:** Incorrect for this question. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. Why the correct answer wins: Forecasting extends the series statistically and shows the uncertainty band.
- **D:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: Forecasting extends the series statistically and shows the uncertainty band.

### Question 73 — C

Answer: Use the Key Influencers visual. Key Influencers ranks the factors associated with a metric. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.
- **B:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.
- **C:** Correct. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. In this case: Key Influencers ranks the factors associated with a metric.
- **D:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.

### Question 74 — B, D

Answers: Use the Decomposition Tree visual; Use Copilot to create a narrative visual. A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page.
- **B:** Correct. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. In this case: A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page.
- **C:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page.
- **D:** Correct. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. In this case: A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page.
- **E:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and a narrative visual summarizes the page.

### Question 75 — C

Answer: Use Q&A to answer a natural-language question. Q&A maps a typed question to the model and returns a visual. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.
- **B:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.
- **C:** Correct. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. In this case: Q&A maps a typed question to the model and returns a visual.
- **D:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Q&A maps a typed question to the model and returns a visual.

### Question 76 — D

Answer: Workspace Contributor role. Contributors publish and edit without controlling workspace membership. Contributors can publish and edit content, which is the role for authors who should not manage membership. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Contributors publish and edit without controlling workspace membership.
- **B:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Contributors publish and edit without controlling workspace membership.
- **C:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Contributors publish and edit without controlling workspace membership.
- **D:** Correct. Contributors can publish and edit content, which is the role for authors who should not manage membership. In this case: Contributors publish and edit without controlling workspace membership.

### Question 77 — A

Answer: Workspace Viewer role. Viewers can read content without editing it. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. In this case: Viewers can read content without editing it.
- **B:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Viewers can read content without editing it.
- **C:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Viewers can read content without editing it.
- **D:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Viewers can read content without editing it.

### Question 78 — B, D

Answers: Workspace Admin role; Workspace Member role. Admin manages the workspace and its members, and Member can publish and add lower-privileged users. Admins manage the workspace, its members, and its settings, which is more than publishing content. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Admin manages the workspace and its members, and Member can publish and add lower-privileged users.
- **B:** Correct. Admins manage the workspace, its members, and its settings, which is more than publishing content. In this case: Admin manages the workspace and its members, and Member can publish and add lower-privileged users.
- **C:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Admin manages the workspace and its members, and Member can publish and add lower-privileged users.
- **D:** Correct. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. In this case: Admin manages the workspace and its members, and Member can publish and add lower-privileged users.
- **E:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Admin manages the workspace and its members, and Member can publish and add lower-privileged users.

### Question 79 — A

Answer: Build in the workspace → curate the app pages → assign audiences → publish and update the app. Audiences control who sees what, and consumers see changes only when the app is updated. Audiences control who sees what, and consumers only see changes when the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Audiences control who sees what, and consumers only see changes when the app is updated. In this case: Audiences control who sees what, and consumers see changes only when the app is updated.
- **B:** Incorrect for this question. Publishing an unfinished report sets expectations you cannot meet and consumers see the version you last shipped. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **C:** Incorrect for this question. An app per person is unmaintainable and defeats the point of audiences. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **D:** Incorrect for this question. Direct workspace access exposes everything in the workspace and cannot be curated per audience. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.

### Question 80 — B

Answer: Update the app after changing the workspace content. Consumers see the published app, so the app must be updated after workspace changes. Consumers see the published app, so workspace edits stay invisible until the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: Consumers see the published app, so the app must be updated after workspace changes.
- **B:** Correct. Consumers see the published app, so workspace edits stay invisible until the app is updated. In this case: Consumers see the published app, so the app must be updated after workspace changes.
- **C:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Consumers see the published app, so the app must be updated after workspace changes.
- **D:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Consumers see the published app, so the app must be updated after workspace changes.

### Question 81 — B

Answer: Create a dashboard in the service. A dashboard is a single canvas of tiles from multiple reports. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A dashboard is a single canvas of tiles from multiple reports.
- **B:** Correct. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. In this case: A dashboard is a single canvas of tiles from multiple reports.
- **C:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A dashboard is a single canvas of tiles from multiple reports.
- **D:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A dashboard is a single canvas of tiles from multiple reports.

### Question 82 — D

Answer: Create a subscription for the report or dashboard. A subscription delivers a snapshot on a schedule. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A subscription delivers a snapshot on a schedule.
- **B:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A subscription delivers a snapshot on a schedule.
- **C:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A subscription delivers a snapshot on a schedule.
- **D:** Correct. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. In this case: A subscription delivers a snapshot on a schedule.

### Question 83 — D

Answer: Create a data alert on a dashboard tile. A data alert notifies when a tile value crosses a threshold. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **B:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **C:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **D:** Correct. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. In this case: A data alert notifies when a tile value crosses a threshold.

### Question 84 — B, D

Answers: Configure incremental refresh with the range parameters; Set the RangeStart and RangeEnd parameters the refresh policy expects. An incremental refresh policy partitions the table, and the range parameters must filter the source query. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the source query.
- **B:** Correct. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the source query.
- **C:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the source query.
- **D:** Correct. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the source query.
- **E:** Incorrect for this question. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the source query.

### Question 85 — B

Answer: Confirm the gateway or cloud connection → store credentials → set the schedule → check refresh history. Connectivity and credentials must be proven before the schedule matters, and history is how a failure is detected. Refresh depends on connectivity and credentials before the schedule matters, and history is how a failure is detected. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Scheduling before connectivity and credentials are proven guarantees a failed first refresh. Why the correct answer wins: Connectivity and credentials must be proven before the schedule matters, and history is how a failure is detected.
- **B:** Correct. Refresh depends on connectivity and credentials before the schedule matters, and history is how a failure is detected. In this case: Connectivity and credentials must be proven before the schedule matters, and history is how a failure is detected.
- **C:** Incorrect for this question. A personal gateway fails when the individual is unavailable or changes machines. Why the correct answer wins: Connectivity and credentials must be proven before the schedule matters, and history is how a failure is detected.
- **D:** Incorrect for this question. Refreshing hourly without checking source capacity overloads the source and can exceed the refresh window. Why the correct answer wins: Connectivity and credentials must be proven before the schedule matters, and history is how a failure is detected.

### Question 86 — D

Answer: Define a row-level security role with a DAX filter. RLS roles filter the model per user at query time. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. Why the correct answer wins: RLS roles filter the model per user at query time.
- **B:** Incorrect for this question. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Why the correct answer wins: RLS roles filter the model per user at query time.
- **C:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: RLS roles filter the model per user at query time.
- **D:** Correct. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. In this case: RLS roles filter the model per user at query time.

### Question 87 — B

Answer: Use a dynamic RLS rule based on USERPRINCIPALNAME. A dynamic rule matches the signed-in identity to a mapping table, which scales without one role per user. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table, which scales without one role per user.
- **B:** Correct. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. In this case: A dynamic rule matches the signed-in identity to a mapping table, which scales without one role per user.
- **C:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table, which scales without one role per user.
- **D:** Incorrect for this question. A static role is simple to reason about but must be maintained every time the org chart changes. Why the correct answer wins: A dynamic rule matches the signed-in identity to a mapping table, which scales without one role per user.

### Question 88 — D

Answer: Certify the semantic model. Certification asserts organization-wide trust after a designated review. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Build lets another author create reports on the model without editing it, which is how reuse is enabled safely. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **B:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **C:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: Certification asserts organization-wide trust after a designated review.
- **D:** Correct. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. In this case: Certification asserts organization-wide trust after a designated review.

### Question 89 — A

Answer: A clustered bar or column chart. A bar chart compares a measure across categories, which is what a ranking needs. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. In this case: A bar chart compares a measure across categories, which is what a ranking needs.
- **B:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A bar chart compares a measure across categories, which is what a ranking needs.
- **C:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A bar chart compares a measure across categories, which is what a ranking needs.
- **D:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A bar chart compares a measure across categories, which is what a ranking needs.

### Question 90 — C

Answer: Capture the view in a bookmark. A bookmark stores filter and visibility state, which a reset button can reapply. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A bookmark stores filter and visibility state, which a reset button can reapply.
- **B:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: A bookmark stores filter and visibility state, which a reset button can reapply.
- **C:** Correct. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. In this case: A bookmark stores filter and visibility state, which a reset button can reapply.
- **D:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A bookmark stores filter and visibility state, which a reset button can reapply.

### Question 91 — D

Answer: Add a reference line for the target or average. A reference line gives the comparison without a second visual. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **B:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **C:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **D:** Correct. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. In this case: A reference line gives the comparison without a second visual.

### Question 92 — C

Answer: Build a star schema with a fact table and conformed dimensions. A star schema separates descriptive attributes into a dimension and leaves keys and measures in the fact. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: A star schema separates descriptive attributes into a dimension and leaves keys and measures in the fact.
- **B:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: A star schema separates descriptive attributes into a dimension and leaves keys and measures in the fact.
- **C:** Correct. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. In this case: A star schema separates descriptive attributes into a dimension and leaves keys and measures in the fact.
- **D:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: A star schema separates descriptive attributes into a dimension and leaves keys and measures in the fact.

### Question 93 — C

Answer: Create a dedicated date table marked as the date table. A contiguous date table supplies every date, so accumulation does not skip gaps in the fact. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: A contiguous date table supplies every date, so accumulation does not skip gaps in the fact.
- **B:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: A contiguous date table supplies every date, so accumulation does not skip gaps in the fact.
- **C:** Correct. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. In this case: A contiguous date table supplies every date, so accumulation does not skip gaps in the fact.
- **D:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: A contiguous date table supplies every date, so accumulation does not skip gaps in the fact.

### Question 94 — D

Answer: Use LASTNONBLANK or LASTDATE for a semi-additive balance. A balance must be taken at a point in time, not added across dates. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **B:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **C:** Incorrect for this question. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. Why the correct answer wins: A balance must be taken at a point in time, not added across dates.
- **D:** Correct. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. In this case: A balance must be taken at a point in time, not added across dates.

### Question 95 — C

Answer: Define an app audience for each group of consumers. Audiences show different content to different groups from one app. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Audiences show different content to different groups from one app.
- **B:** Incorrect for this question. Consumers see the published app, so workspace edits stay invisible until the app is updated. Why the correct answer wins: Audiences show different content to different groups from one app.
- **C:** Correct. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. In this case: Audiences show different content to different groups from one app.
- **D:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Audiences show different content to different groups from one app.

### Question 96 — D

Answer: Install an on-premises data gateway. An on-premises data gateway provides the outbound connection that cloud refresh needs. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An on-premises data gateway provides the outbound connection that cloud refresh needs.
- **B:** Incorrect for this question. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. Why the correct answer wins: An on-premises data gateway provides the outbound connection that cloud refresh needs.
- **C:** Incorrect for this question. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. Why the correct answer wins: An on-premises data gateway provides the outbound connection that cloud refresh needs.
- **D:** Correct. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. In this case: An on-premises data gateway provides the outbound connection that cloud refresh needs.

### Question 97 — A

Answer: Apply a sensitivity label to the semantic model and report. A sensitivity label travels with the exported file. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. In this case: A sensitivity label travels with the exported file.
- **B:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: A sensitivity label travels with the exported file.
- **C:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: A sensitivity label travels with the exported file.
- **D:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: A sensitivity label travels with the exported file.

### Question 98 — B

Answer: Connect to a shared semantic model instead of importing the source again. Connecting to the certified semantic model reuses one definition and inherits its refresh and security. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Connecting to the certified semantic model reuses one definition and inherits its refresh and security.
- **B:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Connecting to the certified semantic model reuses one definition and inherits its refresh and security.
- **C:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: Connecting to the certified semantic model reuses one definition and inherits its refresh and security.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Connecting to the certified semantic model reuses one definition and inherits its refresh and security.

### Question 99 — C

Answer: Review column statistics and value distribution. Value distribution shows whether a handful of values dominate, which a row count cannot reveal. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Value distribution shows whether a handful of values dominate, which a row count cannot reveal.
- **B:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Value distribution shows whether a handful of values dominate, which a row count cannot reveal.
- **C:** Correct. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. In this case: Value distribution shows whether a handful of values dominate, which a row count cannot reveal.
- **D:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: Value distribution shows whether a handful of values dominate, which a row count cannot reveal.

### Question 100 — C, E

Answers: Group by the key and aggregate the measures; Correct the column data type before building the model. Grouping produces one row per store and day, and converting the column type makes the sum numeric. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Grouping produces one row per store and day, and converting the column type makes the sum numeric.
- **B:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Grouping produces one row per store and day, and converting the column type makes the sum numeric.
- **C:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: Grouping produces one row per store and day, and converting the column type makes the sum numeric.
- **D:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Grouping produces one row per store and day, and converting the column type makes the sum numeric.
- **E:** Correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. In this case: Grouping produces one row per store and day, and converting the column type makes the sum numeric.

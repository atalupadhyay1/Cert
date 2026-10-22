# Microsoft PL-300 — Full-Length Mock Exam 4

AI Transformation Leader · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A plant reports on yesterday's production, and the historian holds nine years of readings that are queried all day. Which connection fits?

Domain: Prepare the data

- A. Live connection to a published semantic model
- B. Import mode
- C. DirectLake over a lakehouse
- D. DirectQuery

### 2. An engineer must report on downtime using the definitions the reliability team already publishes. What should the engineer do?

Domain: Prepare the data

- A. DirectQuery
- B. Connect to a shared semantic model instead of importing the source again
- C. Import mode
- D. Dual mode table

### 3. A plant needs live line status for supervisors and a nightly shift summary for planning. Which two storage choices fit? Select two.

Domain: Prepare the data

- A. DirectQuery
- B. Connect to a shared semantic model instead of importing the source again
- C. Live connection to a published semantic model
- D. DirectLake over a lakehouse
- E. Import mode

### 4. An analyst must build pages on a model that only the platform team may edit. What should be used?

Domain: Prepare the data

- A. Live connection to a published semantic model
- B. DirectQuery
- C. Connect to a shared semantic model instead of importing the source again
- D. Import mode

### 5. A composite model imports its machine dimension and queries the fact directly, and machine lookups cause extra round trips. Which setting helps?

Domain: Prepare the data

- A. DirectQuery
- B. Import mode
- C. Dual mode table
- D. DirectLake over a lakehouse

### 6. Shop-floor screens must reflect the current work order status, and the MES can serve those queries. Which mode fits?

Domain: Prepare the data

- A. Dual mode table
- B. DirectLake over a lakehouse
- C. DirectQuery
- D. Import mode

### 7. A quality archive of 40 million measurements is analysed weekly, and the source must not be queried ad hoc. Which mode fits?

Domain: Prepare the data

- A. DirectLake over a lakehouse
- B. Dual mode table
- C. DirectQuery
- D. Import mode

### 8. The same query must read a pilot plant server and then the main plant server after go-live. What should be created?

Domain: Prepare the data

- A. Update the data source credentials in the semantic model settings
- B. Change the data source settings rather than rebuilding the query
- C. Set privacy levels to isolate the sources
- D. Create a parameter for the server, path, or filter

### 9. Refresh fails at 2 a.m. with an authentication error after the SQL login was recreated. Where should the fix go?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Update the data source credentials in the semantic model settings
- C. Create a parameter for the server, path, or filter
- D. Change the data source settings rather than rebuilding the query

### 10. One query combines machine telemetry with HR shift data, and the engine is folding values across them. Which setting prevents that?

Domain: Prepare the data

- A. Create a parameter for the server, path, or filter
- B. Change the data source settings rather than rebuilding the query
- C. Set privacy levels to isolate the sources
- D. Update the data source credentials in the semantic model settings

### 11. A supervisor asks whether downtime is concentrated in a few machines. Which evidence answers that?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Profile the column with column quality, distribution, and profile views
- C. Review column statistics and value distribution
- D. Replace nulls with a defined placeholder or a filled-down value

### 12. A cycle-time column arrives as text, so averages and charts behave strangely. What should be corrected?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Correct the column data type before building the model
- C. Review column statistics and value distribution
- D. Profile the column with column quality, distribution, and profile views

### 13. A plant is onboarding a new sensor feed and wants no rework later. Which sequence is correct?

Domain: Prepare the data

- A. Load the table → discover the type errors in the report → re-import the source
- B. Shape the table → delete the profiling steps → load every column
- C. Profile the source → fix types and nulls → shape the table → load only the needed columns
- D. Load every column → profile in the report → patch the visual

### 14. A scrap-reason column is blank when nothing was scrapped, so scrap rates distort on good days. What should be done?

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Filter out the error rows and report them separately
- C. Remove duplicate rows using the natural business key
- D. Replace nulls with a defined placeholder or a filled-down value

### 15. A re-run batch duplicates work-order rows, and machine names differ only by trailing spaces. Which two fixes are required? Select two.

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Filter out the error rows and report them separately
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Use a locale-aware conversion for dates and decimals
- E. Remove duplicate rows using the natural business key

### 16. Twelve rows fail conversion because a sensor value is recorded as "n/a", and the load must proceed. What should be done?

Domain: Prepare the data

- A. Trim, clean, and standardize the text values
- B. Trace the import error to the source type mismatch
- C. Filter out the error rows and report them separately
- D. Replace nulls with a defined placeholder or a filled-down value

### 17. A shift extract has stray characters, duplicate rows, and mixed number formats. Which sequence is defensible?

Domain: Prepare the data

- A. Replace all values with a default → convert types → load
- B. Convert types first → then look for duplicates → then trim
- C. Identify the bad values → standardize text → convert types → document what was replaced
- D. Filter out the failing rows → load → ask the business later

### 18. Individual readings must be rolled up to one row per machine per hour before loading. What should be used?

Domain: Prepare the data

- A. Group by the key and aggregate the measures
- B. Add a custom column with an M expression
- C. Add an aggregate step with the correct summarization
- D. Add a conditional column for rule-based bucketing

### 19. Downtime must be classified as planned, unplanned, or unknown using the maintenance policy. What should be added?

Domain: Prepare the data

- A. Add a custom column with an M expression
- B. Extract the needed part of the text with a delimiter or position
- C. Add a conditional column for rule-based bucketing
- D. Group by the key and aggregate the measures

### 20. An asset tag contains plant, line, and asset number in one field that must become three, and a display label must combine line and asset. Which two transformations are required? Select two.

Domain: Prepare the data

- A. Extract the needed part of the text with a delimiter or position
- B. Add a conditional column for rule-based bucketing
- C. Add an aggregate step with the correct summarization
- D. Split the combined column into separate fields
- E. Add a custom column with an M expression

### 21. Batch numbers end with a two-digit week that the report needs as a field. What should be done?

Domain: Prepare the data

- A. Add a custom column with an M expression
- B. Extract the needed part of the text with a delimiter or position
- C. Split the combined column into separate fields
- D. Add an aggregate step with the correct summarization

### 22. A source holds one row per asset-attribute pair, and the report needs the attributes as columns. What should be done?

Domain: Prepare the data

- A. Pivot the attribute values into columns
- B. Transpose the table so the header becomes a column
- C. Expand the JSON record into typed columns
- D. Unpivot the month columns into rows

### 23. An inspection log has one column per defect category, and the model needs one category column and one count column. What should be done?

Domain: Prepare the data

- A. Unpivot the month columns into rows
- B. Pivot the attribute values into columns
- C. Transpose the table so the header becomes a column
- D. Convert the XML or JSON list into a table of rows

### 24. A supplier sheet has headings down the first column and values across the top, so nothing loads correctly. What should be done?

Domain: Prepare the data

- A. Pivot the attribute values into columns
- B. Unpivot the month columns into rows
- C. Expand the JSON record into typed columns
- D. Transpose the table so the header becomes a column

### 25. Twelve weekly line extracts share the same columns and must become one table. What should be used?

Domain: Prepare the data

- A. Merge the two queries on a matching key
- B. Append the queries into one table
- C. Use a left outer join to keep every fact row
- D. Use a fuzzy merge with a similarity threshold

### 26. A work-order fact must gain machine criticality, and no work order may be lost when the asset list is incomplete. Which two choices are required? Select two.

Domain: Prepare the data

- A. Use a left outer join to keep every fact row
- B. Append the queries into one table
- C. Disable load on the staging query
- D. Merge the two queries on a matching key
- E. Use a fuzzy merge with a similarity threshold

### 27. A complex transformation must be tested on its own, and working tables must not appear in the model. Which two choices fit? Select two.

Domain: Prepare the data

- A. Reference the query so later steps can diverge
- B. Use a native query to select only the needed rows
- C. Duplicate the query so the two are independent
- D. Stage the raw query and build a separate clean query on it
- E. Disable load on the staging query

### 28. Authors keep dragging asset identifiers onto visuals, and cycle times display with six decimals. Which two actions fix that? Select two.

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Flatten the lookup attributes into a single dimension
- C. Set the table and column properties, including hidden keys and format strings
- D. Build a star schema with a fact table and conformed dimensions
- E. Hide technical columns from the report view

### 29. A plant model must be rebuilt from one wide extract. Which sequence produces a model that lasts?

Domain: Model the data

- A. Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact
- B. Build the relationships first → decide the grain afterwards → load
- C. Keep one wide table → relate it to itself → build measures
- D. Create a dimension per column → relate each one to the fact

### 30. A line table sits between machine and fact, and every filter crosses two hops. What should be done?

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Build a star schema with a fact table and conformed dimensions
- C. Set the table and column properties, including hidden keys and format strings
- D. Flatten the lookup attributes into a single dimension

### 31. Production date and maintenance date both relate to the date table, but only one filters the page. Why?

Domain: Model the data

- A. Single-direction filter from dimension to fact
- B. One-to-one relationship between two tables with the same grain
- C. One-to-many relationship from the dimension to the fact
- D. Inactive relationship activated with USERELATIONSHIP

### 32. Two tables describe the same machine at the same grain, one from the asset register and one from the historian. Which relationship fits?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Single-direction filter from dimension to fact
- C. One-to-one relationship between two tables with the same grain
- D. Many-to-many relationship with a bridging table

### 33. A new production fact must filter from its dimensions and must never let one dimension filter another. Which two choices fit? Select two.

Domain: Model the data

- A. Many-to-many relationship with a bridging table
- B. One-to-one relationship between two tables with the same grain
- C. Bi-directional cross-filtering on the relationship
- D. One-to-many relationship from the dimension to the fact
- E. Single-direction filter from dimension to fact

### 34. A machine visual ignores a selection made in a production visual, and the model is suspected. Which setting decides that?

Domain: Model the data

- A. Set the cross-filter direction on the relationship
- B. Single-direction filter from dimension to fact
- C. Bi-directional cross-filtering on the relationship
- D. Inactive relationship activated with USERELATIONSHIP

### 35. Produced, shipped, and invoiced dates all need the same year-quarter-month logic. What should be used?

Domain: Model the data

- A. Create one date table and role-play it through several relationships
- B. Create a dedicated date table marked as the date table
- C. Mark the table as a date table
- D. Build the fiscal periods as columns in the date table

### 36. A date table exists, but the engine still picks a production timestamp column. What should be done?

Domain: Model the data

- A. Build the fiscal periods as columns in the date table
- B. Create one date table and role-play it through several relationships
- C. Mark the table as a date table
- D. Create a dedicated date table marked as the date table

### 37. An operations review needs dependable year-to-date and prior-year output. Which sequence delivers that?

Domain: Model the data

- A. Use the fact date column directly → write TOTALYTD → add a date slicer
- B. Create a date table → leave it unrelated → filter with it
- C. Create one date table per date column → relate all of them to the fact
- D. Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it

### 38. Overall equipment effectiveness must respond to line and shift slicers without a stored column. What should be created?

Domain: Model the data

- A. Create a calculated column
- B. Create a calculated table
- C. The filter context supplied by the visual, slicers, and page filters
- D. Create a measure for the aggregation

### 39. A small calendar of plant shutdown periods must exist as its own table for filtering. What should be created?

Domain: Model the data

- A. Create a calculated column
- B. Create a calculated table
- C. Create a measure for the aggregation
- D. The row context inside an iterator

### 40. A measure must compare each line's output with total plant output while the visual lists lines. Which function changes the filter context?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Wrap the aggregation in CALCULATE to change the filter context
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Store intermediate results in VAR and RETURN

### 41. A share must be computed against the selected shift while ignoring the line rows the visual happens to show. Which modifier fits?

Domain: Model the data

- A. Add KEEPFILTERS to intersect rather than replace the filter
- B. Remove the filter with REMOVEFILTERS or ALL
- C. Use ALL on the table to clear its filters
- D. Use ALLSELECTED to respect the slicer but ignore the visual

### 42. A measure repeats the same filtered base three times and is hard to review. What should be used?

Domain: Model the data

- A. Wrap the aggregation in CALCULATE to change the filter context
- B. Use ALL on the table to clear its filters
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Store intermediate results in VAR and RETURN

### 43. A share-of-line measure must compare each machine with its whole line regardless of the machine filter. Which modifier fits?

Domain: Model the data

- A. Remove the filter with REMOVEFILTERS or ALL
- B. Add KEEPFILTERS to intersect rather than replace the filter
- C. Use ALLSELECTED to respect the slicer but ignore the visual
- D. Wrap the aggregation in CALCULATE to change the filter context

### 44. A plant needs cumulative output from the start of the fiscal year to the selected week. Which pattern fits?

Domain: Model the data

- A. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- B. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- C. Use TOTALYTD or DATESYTD for year-to-date
- D. Use AVERAGEX over a rolling date window

### 45. A weekly review needs the equivalent week last year and a rolling 28-day window. Which two patterns are required? Select two.

Domain: Model the data

- A. Use TOTALYTD or DATESYTD for year-to-date
- B. Use AVERAGEX over a rolling date window
- C. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- E. Use DATESINPERIOD for a windowed calculation

### 46. A planner must test the effect of a change in shift length on capacity. What should be created?

Domain: Model the data

- A. Use a quick measure for the standard pattern
- B. Create a numeric range parameter for scenario analysis
- C. Create a field parameter so the author can switch the measure or axis
- D. Use PERCENTILE.INC for a distribution boundary

### 47. Forty measures need the same year-to-date variants, and readers must switch between measures on one visual. Which two features fit? Select two.

Domain: Model the data

- A. Use PERCENTILE.INC for a distribution boundary
- B. Create a calculation group for the time-intelligence variants
- C. Create a field parameter so the author can switch the measure or axis
- D. Use a quick measure for the standard pattern
- E. Create a numeric range parameter for scenario analysis

### 48. An operations wallboard is slow, and the author must identify the visual responsible. What should be used?

Domain: Model the data

- A. Reduce the granularity loaded into the model
- B. Run Performance Analyzer to find the slow visual
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Inspect the query plan in DAX query view

### 49. A sensor fact stores a reading every second, but the report only ever looks at minutes. What should be done?

Domain: Model the data

- A. Remove the high-cardinality columns the report does not use
- B. Remove unnecessary rows and columns before optimizing measures
- C. Add an aggregation table for the large fact
- D. Reduce the granularity loaded into the model

### 50. A model stores a free-text defect comment with hundreds of thousands of distinct values. Which storage behaviour makes that expensive?

Domain: Model the data

- A. Inspect the query plan in DAX query view
- B. Run Performance Analyzer to find the slow visual
- C. Reduce column cardinality and width to shrink the VertiPaq store
- D. Add an aggregation table for the large fact

### 51. A plant manager must see output trend across 52 weeks. Which visual fits?

Domain: Visualize and analyze the data

- A. A pie or donut chart
- B. A line chart with a date axis
- C. A scatter chart
- D. A clustered bar or column chart

### 52. A line page must show one utilization value against its target band and the drop-off across production stages. Which two visuals fit? Select two.

Domain: Visualize and analyze the data

- A. A pie or donut chart
- B. A funnel chart
- C. A treemap
- D. A matrix visual with row and column groups
- E. A gauge visual

### 53. A supervisor must compare scrap rate across eight cells. Which visual fits?

Domain: Visualize and analyze the data

- A. A gauge visual
- B. A clustered bar or column chart
- C. A treemap
- D. A line chart with a date axis

### 54. A quality report must show cell by week with subtotals in both directions. Which visual fits?

Domain: Visualize and analyze the data

- A. A waterfall chart
- B. A clustered bar or column chart
- C. A scatter chart
- D. A matrix visual with row and column groups

### 55. Operators need a visible control to choose a line on the page. What should be added?

Domain: Visualize and analyze the data

- A. Set the filter pane scope by page, report, or visual
- B. Sync the slicer across the pages that share the same filter
- C. A slicer on the report page
- D. Edit the interactions so the visual does not filter the others

### 56. Selecting a cell on the page is filtering a fixed safety card. What should be changed?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. Edit the interactions so the visual does not filter the others
- C. Set the filter pane scope by page, report, or visual
- D. A slicer on the report page

### 57. A plant-wide restriction must stay in force as readers move between pages. Where should it be placed?

Domain: Visualize and analyze the data

- A. Set the filter pane scope by page, report, or visual
- B. Edit the interactions so the visual does not filter the others
- C. A slicer on the report page
- D. Sync the slicer across the pages that share the same filter

### 58. Two charts occupy the same space, and only one should be visible at a time. What should be used?

Domain: Visualize and analyze the data

- A. Use the Selection pane to group and layer visuals
- B. Add a page navigator for the report
- C. Capture the view in a bookmark
- D. Add buttons with actions that navigate or apply a bookmark

### 59. A cell view and a plant view share one page, and readers must switch between saved states. What should be captured?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Capture the view in a bookmark
- C. Add buttons with actions that navigate or apply a bookmark
- D. Use the Selection pane to group and layer visuals

### 60. A plant page needs three saved views, each reachable from a button. Which sequence works?

Domain: Visualize and analyze the data

- A. Use buttons without actions → tell readers to click twice
- B. Capture a bookmark before setting the filters → expect it to restore them
- C. Create a page per view → duplicate the visuals → maintain each page
- D. Create the views → capture each in a bookmark → add buttons → hide the visuals not in use

### 61. The report will reach eighteen pages and needs navigation that stays current. What should be used?

Domain: Visualize and analyze the data

- A. Capture the view in a bookmark
- B. Add buttons with actions that navigate or apply a bookmark
- C. Add a page navigator for the report
- D. Use the Selection pane to group and layer visuals

### 62. A reader must click a machine and open a detail page about that machine. What should be configured?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. Configure a drillthrough page with the entity filter
- C. Set the filter pane scope by page, report, or visual
- D. Enable drill-down through the hierarchy

### 63. A hover must show output, scrap, and downtime together without adding visuals. Which two actions deliver that? Select two.

Domain: Visualize and analyze the data

- A. Build a custom tooltip page
- B. Set the tooltip to a report page and size it to the hover area
- C. Configure a drillthrough page with the entity filter
- D. Use the Selection pane to group and layer visuals
- E. Enable drill-down through the hierarchy

### 64. A production team is building its first drillthrough page. Which sequence works?

Domain: Visualize and analyze the data

- A. Create the detail page → add a visual → tell readers to filter it manually
- B. Choose the entity field → create the drillthrough page → place the entity filter → add a back button
- C. Set the drillthrough filter → publish → skip the back button
- D. Put every field on the summary visual → expect drillthrough to work

### 65. A chart must step from plant to line to machine while remaining the same visual throughout. What should be enabled?

Domain: Visualize and analyze the data

- A. Enable drill-down through the hierarchy
- B. Build a custom tooltip page
- C. Configure a drillthrough page with the entity filter
- D. Edit the interactions so the visual does not filter the others

### 66. A safety report must be usable by screen-reader users, and its visuals carry no descriptions. What must be added?

Domain: Visualize and analyze the data

- A. Set a logical tab order for the interactive elements
- B. Provide alt text for each meaningful visual
- C. Enable personalization for the visuals the reader may change
- D. Build the mobile layout in the mobile view

### 67. Maintenance technicians will open the report on a phone and need two measures first. What should be built?

Domain: Visualize and analyze the data

- A. Configure the export and download settings for the report
- B. Build the mobile layout in the mobile view
- C. Enable personalization for the visuals the reader may change
- D. Provide alt text for each meaningful visual

### 68. Line-level data must not be downloaded by contractors who view the report. What should be configured?

Domain: Visualize and analyze the data

- A. Enable personalization for the visuals the reader may change
- B. Configure the export and download settings for the report
- C. Build the mobile layout in the mobile view
- D. Provide alt text for each meaningful visual

### 69. A five-bar chart must show exact values without the reader reading the axis. What should be enabled?

Domain: Visualize and analyze the data

- A. Set the axis range and units explicitly
- B. Apply conditional formatting driven by a measure
- C. Turn on and format data labels
- D. Apply a report theme JSON

### 70. Cells over the scrap threshold must stand out, and a column axis must begin at zero. Which two settings are required? Select two.

Domain: Visualize and analyze the data

- A. Turn on and format data labels
- B. Apply conditional formatting driven by a measure
- C. Apply a report theme JSON
- D. Use the Selection pane to group and layer visuals
- E. Set the axis range and units explicitly

### 71. A weekly chart must show whether output beat the plan. What should be added?

Domain: Visualize and analyze the data

- A. Create groups for the categories that matter
- B. Add error bars to show the uncertainty range
- C. Add a reference line for the target or average
- D. Use the built-in forecast on a line chart

### 72. Machines must be segmented by behaviour without a predefined scheme. What should be used?

Domain: Visualize and analyze the data

- A. Use clustering to find segments in the data
- B. Create bins for a continuous measure
- C. Use the outlier detection feature on the visual
- D. Create groups for the categories that matter

### 73. A stable demand series must be projected a quarter ahead with a confidence band. What should be used?

Domain: Visualize and analyze the data

- A. Add error bars to show the uncertainty range
- B. Add a reference line for the target or average
- C. Use the Analyze feature to explain a change
- D. Use the built-in forecast on a line chart

### 74. A quality team must know which factors are associated with higher defect rates. Which visual fits?

Domain: Visualize and analyze the data

- A. Use the Decomposition Tree visual
- B. Use Q&A to answer a natural-language question
- C. Use the Key Influencers visual
- D. Use Copilot to suggest a report page

### 75. A shift handover needs the page summarized in words for the incoming supervisor. Which feature fits?

Domain: Visualize and analyze the data

- A. Use Copilot to create a narrative visual
- B. Use Copilot to suggest a report page
- C. Use the Key Influencers visual
- D. Use Q&A to answer a natural-language question

### 76. A reliability team needs one place where its analysts collaborate on shared content. What should be created?

Domain: Manage and secure Power BI

- A. Create a workspace for the team that owns the content
- B. Workspace Viewer role
- C. Workspace Admin role
- D. Publish an app from the workspace

### 77. The platform team must manage membership, and the analysts must publish without managing it. Which two roles cover that? Select two.

Domain: Manage and secure Power BI

- A. Workspace Admin role
- B. Workspace Contributor role
- C. Publish an app from the workspace
- D. Workspace Member role
- E. Workspace Viewer role

### 78. A transit authority must decide between an app, a direct link, and embedding for its board pack. What is being decided?

Domain: Manage and secure Power BI

- A. Choose the distribution method that matches the audience
- B. Update the app after changing the workspace content
- C. Create a workspace for the team that owns the content
- D. Define an app audience for each group of consumers

### 79. The transit authority is publishing its first app to two audiences. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Publish the app before the report is finished → update it never
- B. Give every consumer the workspace Viewer role → skip the app
- C. Create one app per person → assign each audience manually
- D. Build in the workspace → curate the app pages → assign audiences → publish and update the app

### 80. Yesterday's numbers are still on screen for consumers even though the workspace was updated. What was missed?

Domain: Manage and secure Power BI

- A. Update the app after changing the workspace content
- B. Publish an app from the workspace
- C. Define an app audience for each group of consumers
- D. Choose the distribution method that matches the audience

### 81. One output metric must sit on a monitoring page and stay linked to its report. What should be created?

Domain: Manage and secure Power BI

- A. Pin the visual to a dashboard tile
- B. Create a data alert on a dashboard tile
- C. Create a subscription for the report or dashboard
- D. Create a dashboard in the service

### 82. The operations director wants the weekly report as an email snapshot. What should be configured?

Domain: Manage and secure Power BI

- A. Set the alert threshold on the pinned card tile
- B. Create a data alert on a dashboard tile
- C. Create a subscription for the report or dashboard
- D. Create a dashboard in the service

### 83. One analyst wants to refresh a personal model from a desktop database, and no server install is possible. What fits that limited case?

Domain: Manage and secure Power BI

- A. Configure scheduled refresh on the semantic model
- B. Virtual network data gateway
- C. Install an on-premises data gateway
- D. Personal mode gateway

### 84. A plant is moving a large sensor table to incremental refresh. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Configure the policy in Desktop → publish → assume partitions were created
- B. Load all history every refresh → add a policy later → hope it rebuilds
- C. Filter the query by date → set the policy → skip the parameters
- D. Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh

### 85. A security role is written, and the team wants to confirm what a supervisor actually sees. What should be used?

Domain: Manage and secure Power BI

- A. Define a row-level security role with a DAX filter
- B. Use a dynamic RLS rule based on USERPRINCIPALNAME
- C. Add the security group to the role membership
- D. Test the role with View as role in the service

### 86. Five plants each need a fixed set of members, and membership changes rarely. What should be created?

Domain: Manage and secure Power BI

- A. A static RLS role per region with fixed members
- B. Map the signed-in user with USERPRINCIPALNAME in the filter
- C. Define a row-level security role with a DAX filter
- D. Use a dynamic RLS rule based on USERPRINCIPALNAME

### 87. A platform team must see which reports depend on a model before changing it. Which view shows that?

Domain: Manage and secure Power BI

- A. Run impact analysis before changing the model
- B. Promote the content as endorsed
- C. Apply a sensitivity label to the semantic model and report
- D. Review lineage view

### 88. Before retiring a column, the team needs the list of downstream items that will break. What should be used?

Domain: Manage and secure Power BI

- A. Grant item-level access to the specific report
- B. Review lineage view
- C. Run impact analysis before changing the model
- D. Promote the content as endorsed

---

## Case study — Evergreen University

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A chosen intake year must stay applied across five pages of the report. What should be configured?

Domain: Visualize and analyze the data

- A. Sync the slicer across the pages that share the same filter
- B. Edit the interactions so the visual does not filter the others
- C. Set the filter pane scope by page, report, or visual
- D. A slicer on the report page

### 90. A root-cause page must explore any dimension in any order, and faculty want to type questions. Which two features fit? Select two.

Domain: Visualize and analyze the data

- A. Use the Key Influencers visual
- B. Use Q&A to answer a natural-language question
- C. Use the Decomposition Tree visual
- D. Use Copilot to suggest a report page
- E. Use Copilot to create a narrative visual

### 91. External accreditors must read the reports but must not change them. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Contributor role
- B. Workspace Member role
- C. Workspace Admin role
- D. Workspace Viewer role

---

## Case study — Lakeshore Library

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. Every branch page must share one palette and font without individual styling. What should be applied?

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Turn on and format data labels
- C. Apply conditional formatting driven by a measure
- D. Use the Selection pane to group and layer visuals

### 93. The branch manager must be notified when daily loans fall below plan. What should be created?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Create a data alert on a dashboard tile
- C. Set the alert threshold on the pinned card tile
- D. Pin the visual to a dashboard tile

### 94. The circulation fact spanning four years must refresh within the overnight window. Which two steps are required? Select two.

Domain: Manage and secure Power BI

- A. Install an on-premises data gateway
- B. Configure incremental refresh with the range parameters
- C. Configure scheduled refresh on the semantic model
- D. Set the RangeStart and RangeEnd parameters the refresh policy expects
- E. Update the credentials used by the refresh schedule

---

## Case study — Redwood Mills

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A contractor supplies a sensor extract with no documentation, and its quality is unknown. What should be done first?

Domain: Prepare the data

- A. Correct the column data type before building the model
- B. Review column statistics and value distribution
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Profile the column with column quality, distribution, and profile views

### 96. The production table repeats machine name, line, and plant on every row, and slicers drag. What should be built?

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Build a star schema with a fact table and conformed dimensions
- C. Flatten the lookup attributes into a single dimension
- D. Set the table and column properties, including hidden keys and format strings

### 97. Unit cost must multiply quantity by rate before summing, and the yield ratio must survive a zero denominator. Which two functions fit? Select two.

Domain: Model the data

- A. Use DISTINCT COUNT for unique entities
- B. Create a measure for the aggregation
- C. Use an iterator function for row-level arithmetic
- D. Use DIVIDE instead of the division operator
- E. Use an iterator such as SUMX over the row-level expression

---

## Case study — Skyline Transit

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Rolling ridership totals skip days when no service ran, and the running figure looks wrong. What is missing?

Domain: Model the data

- A. Build the fiscal periods as columns in the date table
- B. Create one date table and role-play it through several relationships
- C. Create a dedicated date table marked as the date table
- D. Mark the table as a date table

### 99. Fare-card balance is recorded only when a top-up occurs, so month-end lands on a blank day. What should be used?

Domain: Model the data

- A. Use AVERAGEX over a rolling date window
- B. Use LASTNONBLANK or LASTDATE for a semi-additive balance
- C. Use LASTNONBLANK when the balance is only recorded on some dates
- D. Use TOTALYTD or DATESYTD for year-to-date

### 100. The operations team must state the delay below which 90 percent of trips fall. What should be used?

Domain: Model the data

- A. Use PERCENTILE.INC for a distribution boundary
- B. Create a calculation group for the time-intelligence variants
- C. Use a statistical function such as STDEV.P or MEDIAN to describe the spread
- D. Use a quick measure for the standard pattern

---

## Answer key and explanations

### Question 1 — B

Answer: Import mode. Import serves the volume from memory and spares the historian from analyst queries. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Import serves the volume from memory and spares the historian from analyst queries.
- **B:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import serves the volume from memory and spares the historian from analyst queries.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import serves the volume from memory and spares the historian from analyst queries.
- **D:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import serves the volume from memory and spares the historian from analyst queries.

### Question 2 — B

Answer: Connect to a shared semantic model instead of importing the source again. Connecting to the published model inherits its definitions, refresh, and security. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Connecting to the published model inherits its definitions, refresh, and security.
- **B:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Connecting to the published model inherits its definitions, refresh, and security.
- **C:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: Connecting to the published model inherits its definitions, refresh, and security.
- **D:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Connecting to the published model inherits its definitions, refresh, and security.

### Question 3 — A, E

Answers: DirectQuery; Import mode. Line status must query the source live, while the shift summary is best imported. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: Line status must query the source live, while the shift summary is best imported.
- **B:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: Line status must query the source live, while the shift summary is best imported.
- **C:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: Line status must query the source live, while the shift summary is best imported.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Line status must query the source live, while the shift summary is best imported.
- **E:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Line status must query the source live, while the shift summary is best imported.

### Question 4 — A

Answer: Live connection to a published semantic model. A live connection allows report authoring without editing the model. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. In this case: A live connection allows report authoring without editing the model.
- **B:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: A live connection allows report authoring without editing the model.
- **C:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: A live connection allows report authoring without editing the model.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: A live connection allows report authoring without editing the model.

### Question 5 — C

Answer: Dual mode table. A Dual table can answer some queries from memory instead of the source. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.
- **B:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.
- **C:** Correct. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. In this case: A Dual table can answer some queries from memory instead of the source.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: A Dual table can answer some queries from memory instead of the source.

### Question 6 — C

Answer: DirectQuery. DirectQuery reads the source at report time, which current status requires. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.
- **B:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.
- **C:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery reads the source at report time, which current status requires.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery reads the source at report time, which current status requires.

### Question 7 — D

Answer: Import mode. Import moves the analytical load off the source. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import moves the analytical load off the source.
- **B:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Import moves the analytical load off the source.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import moves the analytical load off the source.
- **D:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import moves the analytical load off the source.

### Question 8 — D

Answer: Create a parameter for the server, path, or filter. A parameter swaps the environment without editing the M code. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **B:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **C:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **D:** Correct. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. In this case: A parameter swaps the environment without editing the M code.

### Question 9 — B

Answer: Update the data source credentials in the semantic model settings. The stored credential in the data source settings is what refresh uses. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **B:** Correct. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. In this case: The stored credential in the data source settings is what refresh uses.
- **C:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.
- **D:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: The stored credential in the data source settings is what refresh uses.

### Question 10 — C

Answer: Set privacy levels to isolate the sources. Privacy levels stop values being combined across sources that must stay separate. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **B:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.
- **C:** Correct. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. In this case: Privacy levels stop values being combined across sources that must stay separate.
- **D:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Privacy levels stop values being combined across sources that must stay separate.

### Question 11 — C

Answer: Review column statistics and value distribution. Value distribution shows whether the measure is concentrated in a few members. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **B:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **C:** Correct. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. In this case: Value distribution shows whether the measure is concentrated in a few members.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.

### Question 12 — B

Answer: Correct the column data type before building the model. A numeric value stored as text cannot be aggregated, so the type must be fixed. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **B:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **C:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.
- **D:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: A numeric value stored as text cannot be aggregated, so the type must be fixed.

### Question 13 — C

Answer: Profile the source → fix types and nulls → shape the table → load only the needed columns. Profiling comes first, shaping follows, and loading only needed columns keeps the model small. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Discovering type errors after load means the model was built on wrong data and the work restarts. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **B:** Incorrect for this question. Deleting profiling removes the evidence of quality problems and loading every column inflates the model. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **C:** Correct. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. In this case: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **D:** Incorrect for this question. Patching visuals hides the data problem instead of fixing it at the source. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.

### Question 14 — D

Answer: Replace nulls with a defined placeholder or a filled-down value. Replacing blank with zero for this case makes the rate correct and the assumption explicit. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Replacing blank with zero for this case makes the rate correct and the assumption explicit.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Replacing blank with zero for this case makes the rate correct and the assumption explicit.
- **C:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Replacing blank with zero for this case makes the rate correct and the assumption explicit.
- **D:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: Replacing blank with zero for this case makes the rate correct and the assumption explicit.

### Question 15 — A, E

Answers: Remove duplicate rows using the natural business key; Trim, clean, and standardize the text values. De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. In this case: De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names.
- **B:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names.
- **C:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names.
- **D:** Incorrect for this question. A locale-aware conversion stops day and month being swapped and stops decimal commas being interpreted as text. Why the correct answer wins: De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names.
- **E:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: De-duplicating on the work order key removes repeats, and standardizing text collapses the duplicate names.

### Question 16 — C

Answer: Filter out the error rows and report them separately. Filtering the failing rows and reporting them keeps the load moving without hiding the gap. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Filtering the failing rows and reporting them keeps the load moving without hiding the gap.
- **B:** Incorrect for this question. Most import errors come from a value that does not match the declared type, so the fix is at the source column or an explicit conversion. Why the correct answer wins: Filtering the failing rows and reporting them keeps the load moving without hiding the gap.
- **C:** Correct. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. In this case: Filtering the failing rows and reporting them keeps the load moving without hiding the gap.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Filtering the failing rows and reporting them keeps the load moving without hiding the gap.

### Question 17 — C

Answer: Identify the bad values → standardize text → convert types → document what was replaced. Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing everything with a default destroys real values and hides the pattern behind the error. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **B:** Incorrect for this question. Converting before trimming fails on values that only differ by whitespace and leaves duplicates behind. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **C:** Correct. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. In this case: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.
- **D:** Incorrect for this question. Silently dropping rows changes the totals and the business never learns what is missing. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps it auditable.

### Question 18 — A

Answer: Group by the key and aggregate the measures. Grouping with an aggregate produces one row per machine and hour. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. In this case: Grouping with an aggregate produces one row per machine and hour.
- **B:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Grouping with an aggregate produces one row per machine and hour.
- **C:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Grouping with an aggregate produces one row per machine and hour.
- **D:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Grouping with an aggregate produces one row per machine and hour.

### Question 19 — C

Answer: Add a conditional column for rule-based bucketing. A conditional column applies the policy thresholds explicitly and is easy to review. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: A conditional column applies the policy thresholds explicitly and is easy to review.
- **B:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: A conditional column applies the policy thresholds explicitly and is easy to review.
- **C:** Correct. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. In this case: A conditional column applies the policy thresholds explicitly and is easy to review.
- **D:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A conditional column applies the policy thresholds explicitly and is easy to review.

### Question 20 — D, E

Answers: Split the combined column into separate fields; Add a custom column with an M expression. Splitting separates the three parts, and a custom column builds the display label. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Splitting separates the three parts, and a custom column builds the display label.
- **B:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Splitting separates the three parts, and a custom column builds the display label.
- **C:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Splitting separates the three parts, and a custom column builds the display label.
- **D:** Correct. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. In this case: Splitting separates the three parts, and a custom column builds the display label.
- **E:** Correct. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. In this case: Splitting separates the three parts, and a custom column builds the display label.

### Question 21 — B

Answer: Extract the needed part of the text with a delimiter or position. Extracting by position keeps the week without importing the whole identifier twice. Extraction keeps the useful part of an identifier without importing the whole string into the model. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Extracting by position keeps the week without importing the whole identifier twice.
- **B:** Correct. Extraction keeps the useful part of an identifier without importing the whole string into the model. In this case: Extracting by position keeps the week without importing the whole identifier twice.
- **C:** Incorrect for this question. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Why the correct answer wins: Extracting by position keeps the week without importing the whole identifier twice.
- **D:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Extracting by position keeps the week without importing the whole identifier twice.

### Question 22 — A

Answer: Pivot the attribute values into columns. Pivoting turns attribute rows into columns. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. In this case: Pivoting turns attribute rows into columns.
- **B:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Pivoting turns attribute rows into columns.
- **C:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Pivoting turns attribute rows into columns.
- **D:** Incorrect for this question. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Why the correct answer wins: Pivoting turns attribute rows into columns.

### Question 23 — A

Answer: Unpivot the month columns into rows. Unpivoting turns the category columns into rows. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. In this case: Unpivoting turns the category columns into rows.
- **B:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Unpivoting turns the category columns into rows.
- **C:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Unpivoting turns the category columns into rows.
- **D:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Unpivoting turns the category columns into rows.

### Question 24 — D

Answer: Transpose the table so the header becomes a column. Transposing swaps rows and columns, which repairs a report-shaped sheet. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Transposing swaps rows and columns, which repairs a report-shaped sheet.
- **B:** Incorrect for this question. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Why the correct answer wins: Transposing swaps rows and columns, which repairs a report-shaped sheet.
- **C:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Transposing swaps rows and columns, which repairs a report-shaped sheet.
- **D:** Correct. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. In this case: Transposing swaps rows and columns, which repairs a report-shaped sheet.

### Question 25 — B

Answer: Append the queries into one table. Appending stacks rows of the same shape. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. Why the correct answer wins: Appending stacks rows of the same shape.
- **B:** Correct. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. In this case: Appending stacks rows of the same shape.
- **C:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: Appending stacks rows of the same shape.
- **D:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: Appending stacks rows of the same shape.

### Question 26 — A, D

Answers: Merge the two queries on a matching key; Use a left outer join to keep every fact row. A merge adds criticality, and a left outer join keeps unmatched work orders. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. In this case: A merge adds criticality, and a left outer join keeps unmatched work orders.
- **B:** Incorrect for this question. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Why the correct answer wins: A merge adds criticality, and a left outer join keeps unmatched work orders.
- **C:** Incorrect for this question. Disabling load keeps a working query out of the model, which prevents unused tables from inflating the dataset. Why the correct answer wins: A merge adds criticality, and a left outer join keeps unmatched work orders.
- **D:** Correct. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. In this case: A merge adds criticality, and a left outer join keeps unmatched work orders.
- **E:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: A merge adds criticality, and a left outer join keeps unmatched work orders.

### Question 27 — D, E

Answers: Stage the raw query and build a separate clean query on it; Disable load on the staging query. Staging separates extraction from transformation, and disabling load keeps working tables out of the model. Staging separates extraction from transformation, which makes each layer easier to test and reuse. Disabling load keeps a working query out of the model, which prevents unused tables from inflating the dataset. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A reference reuses the earlier steps of a query while allowing a different downstream shape, which avoids loading the base table twice. Why the correct answer wins: Staging separates extraction from transformation, and disabling load keeps working tables out of the model.
- **B:** Incorrect for this question. A native query reduces what is transferred, but it can break folding for later steps and must be maintained as the schema changes. Why the correct answer wins: Staging separates extraction from transformation, and disabling load keeps working tables out of the model.
- **C:** Incorrect for this question. A duplicate copies the full step chain, so a change in one copy does not affect the other but the work is repeated. Why the correct answer wins: Staging separates extraction from transformation, and disabling load keeps working tables out of the model.
- **D:** Correct. Staging separates extraction from transformation, which makes each layer easier to test and reuse. In this case: Staging separates extraction from transformation, and disabling load keeps working tables out of the model.
- **E:** Correct. Disabling load keeps a working query out of the model, which prevents unused tables from inflating the dataset. In this case: Staging separates extraction from transformation, and disabling load keeps working tables out of the model.

### Question 28 — C, E

Answers: Set the table and column properties, including hidden keys and format strings; Hide technical columns from the report view. Hiding identifiers removes them from the field list, and format strings fix how values display. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **B:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **C:** Correct. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **D:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Hiding identifiers removes them from the field list, and format strings fix how values display.
- **E:** Correct. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. In this case: Hiding identifiers removes them from the field list, and format strings fix how values display.

### Question 29 — A

Answer: Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact. Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. In this case: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **B:** Incorrect for this question. Relationships built before the grain is agreed will be wrong and must be rebuilt. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **C:** Incorrect for this question. A single wide table cannot be filtered cleanly by dimension and pushes duplication into every row. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.
- **D:** Incorrect for this question. A dimension per column produces a hub of one-column tables and makes the model unmaintainable. Why the correct answer wins: Agreeing the grain first decides what a row means, and separating descriptive attributes makes the star work.

### Question 30 — D

Answer: Flatten the lookup attributes into a single dimension. Flattening the line attributes into the machine dimension removes the hop. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Flattening the line attributes into the machine dimension removes the hop.
- **B:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Flattening the line attributes into the machine dimension removes the hop.
- **C:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: Flattening the line attributes into the machine dimension removes the hop.
- **D:** Correct. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. In this case: Flattening the line attributes into the machine dimension removes the hop.

### Question 31 — D

Answer: Inactive relationship activated with USERELATIONSHIP. Only one relationship can be active, so the second waits until a measure activates it. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **B:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **C:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: Only one relationship can be active, so the second waits until a measure activates it.
- **D:** Correct. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. In this case: Only one relationship can be active, so the second waits until a measure activates it.

### Question 32 — C

Answer: One-to-one relationship between two tables with the same grain. One-to-one suits two tables describing the same entity at the same grain. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: One-to-one suits two tables describing the same entity at the same grain.
- **B:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: One-to-one suits two tables describing the same entity at the same grain.
- **C:** Correct. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. In this case: One-to-one suits two tables describing the same entity at the same grain.
- **D:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: One-to-one suits two tables describing the same entity at the same grain.

### Question 33 — D, E

Answers: Single-direction filter from dimension to fact; One-to-many relationship from the dimension to the fact. Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **B:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **C:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **D:** Correct. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **E:** Correct. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.

### Question 34 — A

Answer: Set the cross-filter direction on the relationship. Cross-filter direction decides whether the fact can filter the dimension. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. In this case: Cross-filter direction decides whether the fact can filter the dimension.
- **B:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **C:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **D:** Incorrect for this question. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.

### Question 35 — A

Answer: Create one date table and role-play it through several relationships. One date table related three times through role-playing dimensions avoids three near-identical tables. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. In this case: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **B:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **C:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **D:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.

### Question 36 — C

Answer: Mark the table as a date table. Marking the table as the date table removes the ambiguity. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: Marking the table as the date table removes the ambiguity.
- **B:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Marking the table as the date table removes the ambiguity.
- **C:** Correct. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. In this case: Marking the table as the date table removes the ambiguity.
- **D:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Marking the table as the date table removes the ambiguity.

### Question 37 — D

Answer: Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it. Marking and relating the date table is what makes the measures obey the date slicer. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A fact date column has gaps, so year-to-date silently skips missing days and the slicer shows no clean hierarchy. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **B:** Incorrect for this question. An unrelated date table filters nothing, so the slicer appears to work while the visuals ignore it. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **C:** Incorrect for this question. Several date tables multiply relationships and make every time measure ambiguous. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **D:** Correct. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. In this case: Marking and relating the date table is what makes the measures obey the date slicer.

### Question 38 — D

Answer: Create a measure for the aggregation. A measure is evaluated in the filter context the visual supplies. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **B:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **C:** Incorrect for this question. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies.
- **D:** Correct. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. In this case: A measure is evaluated in the filter context the visual supplies.

### Question 39 — B

Answer: Create a calculated table. A calculated table materializes at refresh, which suits a small derived table. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: A calculated table materializes at refresh, which suits a small derived table.
- **B:** Correct. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. In this case: A calculated table materializes at refresh, which suits a small derived table.
- **C:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: A calculated table materializes at refresh, which suits a small derived table.
- **D:** Incorrect for this question. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. Why the correct answer wins: A calculated table materializes at refresh, which suits a small derived table.

### Question 40 — B

Answer: Wrap the aggregation in CALCULATE to change the filter context. CALCULATE evaluates the expression under modified filters. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **B:** Correct. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. In this case: CALCULATE evaluates the expression under modified filters.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.
- **D:** Incorrect for this question. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Why the correct answer wins: CALCULATE evaluates the expression under modified filters.

### Question 41 — D

Answer: Use ALLSELECTED to respect the slicer but ignore the visual. ALLSELECTED respects the reader's selection while removing the visual's grouping. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **B:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **C:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's grouping.
- **D:** Correct. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. In this case: ALLSELECTED respects the reader's selection while removing the visual's grouping.

### Question 42 — D

Answer: Store intermediate results in VAR and RETURN. Variables compute the expression once and make the measure readable. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **B:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **D:** Correct. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. In this case: Variables compute the expression once and make the measure readable.

### Question 43 — A

Answer: Remove the filter with REMOVEFILTERS or ALL. Removing the machine filter lets the denominator cover the whole line. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. In this case: Removing the machine filter lets the denominator cover the whole line.
- **B:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Removing the machine filter lets the denominator cover the whole line.
- **C:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: Removing the machine filter lets the denominator cover the whole line.
- **D:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Removing the machine filter lets the denominator cover the whole line.

### Question 44 — C

Answer: Use TOTALYTD or DATESYTD for year-to-date. Year-to-date accumulates from the start of the year defined by the marked date table. Year-to-date functions accumulate from the start of the year defined by the marked date table. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **B:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.
- **C:** Correct. Year-to-date functions accumulate from the start of the year defined by the marked date table. In this case: Year-to-date accumulates from the start of the year defined by the marked date table.
- **D:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: Year-to-date accumulates from the start of the year defined by the marked date table.

### Question 45 — C, E

Answers: Use SAMEPERIODLASTYEAR or DATEADD for the comparable period; Use DATESINPERIOD for a windowed calculation. The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window.
- **B:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window.
- **C:** Correct. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. In this case: The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window.
- **D:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window.
- **E:** Correct. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. In this case: The comparable-period shift supplies last year, and DATESINPERIOD supplies the rolling window.

### Question 46 — B

Answer: Create a numeric range parameter for scenario analysis. A numeric range parameter drives a measure with the selected assumption. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.
- **B:** Correct. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. In this case: A numeric range parameter drives a measure with the selected assumption.
- **C:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.
- **D:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A numeric range parameter drives a measure with the selected assumption.

### Question 47 — B, C

Answers: Create a calculation group for the time-intelligence variants; Create a field parameter so the author can switch the measure or axis. A calculation group applies the variants to every measure, and a field parameter switches the measure in place. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **B:** Correct. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. In this case: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **C:** Correct. A field parameter lets one visual switch between measures or dimensions without duplicating pages. In this case: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **D:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.
- **E:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A calculation group applies the variants to every measure, and a field parameter switches the measure in place.

### Question 48 — B

Answer: Run Performance Analyzer to find the slow visual. Performance Analyzer times each visual and separates DAX, query, and rendering cost. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **B:** Correct. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. In this case: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **C:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.
- **D:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: Performance Analyzer times each visual and separates DAX, query, and rendering cost.

### Question 49 — D

Answer: Reduce the granularity loaded into the model. Loading at the grain the report needs removes rows the visuals never use. Loading to the grain the report actually needs removes rows the visuals never use. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. Why the correct answer wins: Loading at the grain the report needs removes rows the visuals never use.
- **B:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: Loading at the grain the report needs removes rows the visuals never use.
- **C:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: Loading at the grain the report needs removes rows the visuals never use.
- **D:** Correct. Loading to the grain the report actually needs removes rows the visuals never use. In this case: Loading at the grain the report needs removes rows the visuals never use.

### Question 50 — C

Answer: Reduce column cardinality and width to shrink the VertiPaq store. The in-memory store compresses repeated and narrow values well, so high-cardinality text costs the most. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so high-cardinality text costs the most.
- **B:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so high-cardinality text costs the most.
- **C:** Correct. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. In this case: The in-memory store compresses repeated and narrow values well, so high-cardinality text costs the most.
- **D:** Incorrect for this question. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so high-cardinality text costs the most.

### Question 51 — B

Answer: A line chart with a date axis. A line chart shows a trend over a continuous axis. A line chart shows a trend over a continuous axis, which is what time series need. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A line chart shows a trend over a continuous axis.
- **B:** Correct. A line chart shows a trend over a continuous axis, which is what time series need. In this case: A line chart shows a trend over a continuous axis.
- **C:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A line chart shows a trend over a continuous axis.
- **D:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A line chart shows a trend over a continuous axis.

### Question 52 — B, E

Answers: A gauge visual; A funnel chart. A gauge shows one value against a target range, and a funnel shows stage attrition. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A gauge shows one value against a target range, and a funnel shows stage attrition.
- **B:** Correct. A funnel shows sequential stage attrition, which suits a sales or process pipeline. In this case: A gauge shows one value against a target range, and a funnel shows stage attrition.
- **C:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A gauge shows one value against a target range, and a funnel shows stage attrition.
- **D:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A gauge shows one value against a target range, and a funnel shows stage attrition.
- **E:** Correct. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. In this case: A gauge shows one value against a target range, and a funnel shows stage attrition.

### Question 53 — B

Answer: A clustered bar or column chart. A bar chart compares a measure across categories. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A bar chart compares a measure across categories.
- **B:** Correct. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. In this case: A bar chart compares a measure across categories.
- **C:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A bar chart compares a measure across categories.
- **D:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A bar chart compares a measure across categories.

### Question 54 — D

Answer: A matrix visual with row and column groups. A matrix supports nested rows and columns with subtotals. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **B:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **C:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **D:** Correct. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. In this case: A matrix supports nested rows and columns with subtotals.

### Question 55 — C

Answer: A slicer on the report page. A slicer puts the control on the canvas. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: A slicer puts the control on the canvas.
- **B:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: A slicer puts the control on the canvas.
- **C:** Correct. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. In this case: A slicer puts the control on the canvas.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: A slicer puts the control on the canvas.

### Question 56 — B

Answer: Edit the interactions so the visual does not filter the others. Interaction settings decide whether a selection filters, highlights, or does nothing. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **B:** Correct. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. In this case: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **C:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.

### Question 57 — A

Answer: Set the filter pane scope by page, report, or visual. Filter scope decides whether a filter applies to a visual, a page, or the whole report. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. In this case: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **C:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.
- **D:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Filter scope decides whether a filter applies to a visual, a page, or the whole report.

### Question 58 — A

Answer: Use the Selection pane to group and layer visuals. The Selection pane controls visibility and z-order. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. In this case: The Selection pane controls visibility and z-order.
- **B:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: The Selection pane controls visibility and z-order.
- **C:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: The Selection pane controls visibility and z-order.
- **D:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: The Selection pane controls visibility and z-order.

### Question 59 — B

Answer: Capture the view in a bookmark. A bookmark stores filter and visibility state. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: A bookmark stores filter and visibility state.
- **B:** Correct. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. In this case: A bookmark stores filter and visibility state.
- **C:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A bookmark stores filter and visibility state.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A bookmark stores filter and visibility state.

### Question 60 — D

Answer: Create the views → capture each in a bookmark → add buttons → hide the visuals not in use. Bookmarks store state and buttons apply it. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A button with no action is decoration and the report still has no navigation. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **B:** Incorrect for this question. A bookmark captures the state at the moment it is created, so filters set afterwards are not stored. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **C:** Incorrect for this question. Duplicating pages multiplies maintenance and the copies drift apart. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **D:** Correct. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. In this case: Bookmarks store state and buttons apply it.

### Question 61 — C

Answer: Add a page navigator for the report. A page navigator generates navigation from the pages themselves. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **B:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **C:** Correct. A page navigator generates navigation for every page automatically, which stays correct as pages are added. In this case: A page navigator generates navigation from the pages themselves.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A page navigator generates navigation from the pages themselves.

### Question 62 — B

Answer: Configure a drillthrough page with the entity filter. Drillthrough passes the selected entity to a detail page through a filter. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **B:** Correct. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. In this case: Drillthrough passes the selected entity to a detail page through a filter.
- **C:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **D:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.

### Question 63 — A, B

Answers: Build a custom tooltip page; Set the tooltip to a report page and size it to the hover area. A tooltip page holds the extra measures, and the report-page tooltip setting displays it. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **B:** Correct. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **C:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **E:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.

### Question 64 — B

Answer: Choose the entity field → create the drillthrough page → place the entity filter → add a back button. The drillthrough filter carries the selection, and the back button keeps the reader oriented. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page without the drillthrough filter does not carry the selected entity, so the detail is not about what was clicked. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **B:** Correct. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. In this case: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **C:** Incorrect for this question. Without a back button the reader is stranded on the detail page and loses the summary context. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **D:** Incorrect for this question. Too many fields on one visual makes the click target ambiguous and the drill result unpredictable. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.

### Question 65 — A

Answer: Enable drill-down through the hierarchy. Drill-down moves through the hierarchy inside the same visual. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. In this case: Drill-down moves through the hierarchy inside the same visual.
- **B:** Incorrect for this question. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **C:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **D:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.

### Question 66 — B

Answer: Provide alt text for each meaningful visual. Alt text describes each visual for a screen reader. Alt text describes the visual for a screen reader, which is required for an accessible report. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **B:** Correct. Alt text describes the visual for a screen reader, which is required for an accessible report. In this case: Alt text describes each visual for a screen reader.
- **C:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **D:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Alt text describes each visual for a screen reader.

### Question 67 — B

Answer: Build the mobile layout in the mobile view. The mobile layout decides what appears first on a phone. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **B:** Correct. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. In this case: The mobile layout decides what appears first on a phone.
- **C:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: The mobile layout decides what appears first on a phone.
- **D:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: The mobile layout decides what appears first on a phone.

### Question 68 — B

Answer: Configure the export and download settings for the report. Export settings decide whether readers can take data out. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Export settings decide whether readers can take data out.
- **B:** Correct. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. In this case: Export settings decide whether readers can take data out.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Export settings decide whether readers can take data out.
- **D:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Export settings decide whether readers can take data out.

### Question 69 — C

Answer: Turn on and format data labels. Data labels put the value next to the mark. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: Data labels put the value next to the mark.
- **B:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: Data labels put the value next to the mark.
- **C:** Correct. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. In this case: Data labels put the value next to the mark.
- **D:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Data labels put the value next to the mark.

### Question 70 — B, E

Answers: Apply conditional formatting driven by a measure; Set the axis range and units explicitly. Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **B:** Correct. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. In this case: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **C:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **E:** Correct. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. In this case: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.

### Question 71 — C

Answer: Add a reference line for the target or average. A reference line gives the comparison without a second visual. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **B:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: A reference line gives the comparison without a second visual.
- **C:** Correct. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. In this case: A reference line gives the comparison without a second visual.
- **D:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: A reference line gives the comparison without a second visual.

### Question 72 — A

Answer: Use clustering to find segments in the data. Clustering groups rows that behave similarly. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. In this case: Clustering groups rows that behave similarly.
- **B:** Incorrect for this question. Binning turns a continuous value into ranges, which is how a distribution becomes readable. Why the correct answer wins: Clustering groups rows that behave similarly.
- **C:** Incorrect for this question. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Why the correct answer wins: Clustering groups rows that behave similarly.
- **D:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: Clustering groups rows that behave similarly.

### Question 73 — D

Answer: Use the built-in forecast on a line chart. Forecasting extends the series statistically with a confidence band. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.
- **B:** Incorrect for this question. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.
- **C:** Incorrect for this question. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. Why the correct answer wins: Forecasting extends the series statistically with a confidence band.
- **D:** Correct. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. In this case: Forecasting extends the series statistically with a confidence band.

### Question 74 — C

Answer: Use the Key Influencers visual. Key Influencers ranks the factors associated with a metric. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.
- **B:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.
- **C:** Correct. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. In this case: Key Influencers ranks the factors associated with a metric.
- **D:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: Key Influencers ranks the factors associated with a metric.

### Question 75 — A

Answer: Use Copilot to create a narrative visual. A narrative visual summarizes the page in text. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. In this case: A narrative visual summarizes the page in text.
- **B:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A narrative visual summarizes the page in text.
- **C:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A narrative visual summarizes the page in text.
- **D:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: A narrative visual summarizes the page in text.

### Question 76 — A

Answer: Create a workspace for the team that owns the content. A workspace is the collaboration and permission boundary for the team. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. In this case: A workspace is the collaboration and permission boundary for the team.
- **B:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **C:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **D:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.

### Question 77 — A, B

Answers: Workspace Admin role; Workspace Contributor role. Admin manages the workspace and members, and Contributor publishes without membership control. Admins manage the workspace, its members, and its settings, which is more than publishing content. Contributors can publish and edit content, which is the role for authors who should not manage membership. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Admins manage the workspace, its members, and its settings, which is more than publishing content. In this case: Admin manages the workspace and members, and Contributor publishes without membership control.
- **B:** Correct. Contributors can publish and edit content, which is the role for authors who should not manage membership. In this case: Admin manages the workspace and members, and Contributor publishes without membership control.
- **C:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Admin manages the workspace and members, and Contributor publishes without membership control.
- **D:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Admin manages the workspace and members, and Contributor publishes without membership control.
- **E:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Admin manages the workspace and members, and Contributor publishes without membership control.

### Question 78 — A

Answer: Choose the distribution method that matches the audience. The distribution method decides reach, control, and authentication. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. In this case: The distribution method decides reach, control, and authentication.
- **B:** Incorrect for this question. Consumers see the published app, so workspace edits stay invisible until the app is updated. Why the correct answer wins: The distribution method decides reach, control, and authentication.
- **C:** Incorrect for this question. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Why the correct answer wins: The distribution method decides reach, control, and authentication.
- **D:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: The distribution method decides reach, control, and authentication.

### Question 79 — D

Answer: Build in the workspace → curate the app pages → assign audiences → publish and update the app. Audiences control who sees what, and consumers see changes only when the app is updated. Audiences control who sees what, and consumers only see changes when the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Publishing an unfinished report sets expectations you cannot meet and consumers see the version you last shipped. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **B:** Incorrect for this question. Direct workspace access exposes everything in the workspace and cannot be curated per audience. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **C:** Incorrect for this question. An app per person is unmaintainable and defeats the point of audiences. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **D:** Correct. Audiences control who sees what, and consumers only see changes when the app is updated. In this case: Audiences control who sees what, and consumers see changes only when the app is updated.

### Question 80 — A

Answer: Update the app after changing the workspace content. Consumers see the published app, so the app must be updated. Consumers see the published app, so workspace edits stay invisible until the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Consumers see the published app, so workspace edits stay invisible until the app is updated. In this case: Consumers see the published app, so the app must be updated.
- **B:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Consumers see the published app, so the app must be updated.
- **C:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: Consumers see the published app, so the app must be updated.
- **D:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: Consumers see the published app, so the app must be updated.

### Question 81 — A

Answer: Pin the visual to a dashboard tile. Pinning copies the visual to a dashboard tile and keeps the link. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. In this case: Pinning copies the visual to a dashboard tile and keeps the link.
- **B:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link.
- **C:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link.
- **D:** Incorrect for this question. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link.

### Question 82 — C

Answer: Create a subscription for the report or dashboard. A subscription delivers a scheduled snapshot by email. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **B:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **C:** Correct. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. In this case: A subscription delivers a scheduled snapshot by email.
- **D:** Incorrect for this question. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.

### Question 83 — D

Answer: Personal mode gateway. A personal gateway serves a single author and cannot be shared, which is the only fit here. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: A personal gateway serves a single author and cannot be shared, which is the only fit here.
- **B:** Incorrect for this question. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. Why the correct answer wins: A personal gateway serves a single author and cannot be shared, which is the only fit here.
- **C:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: A personal gateway serves a single author and cannot be shared, which is the only fit here.
- **D:** Correct. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. In this case: A personal gateway serves a single author and cannot be shared, which is the only fit here.

### Question 84 — D

Answer: Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh. Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. The policy is applied when the model is published and refreshed, so assuming it worked leaves a full load in place. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **B:** Incorrect for this question. A later policy does not rewrite history that was never partitioned, so the load stays slow. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **C:** Incorrect for this question. A policy without the parameter filter has nothing to partition and falls back to loading everything. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **D:** Correct. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. In this case: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.

### Question 85 — D

Answer: Test the role with View as role in the service. View as role shows the report exactly as a role member sees it. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **B:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **C:** Incorrect for this question. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **D:** Correct. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. In this case: View as role shows the report exactly as a role member sees it.

### Question 86 — A

Answer: A static RLS role per region with fixed members. A static role per plant is simple to reason about when membership is stable. A static role is simple to reason about but must be maintained every time the org chart changes. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A static role is simple to reason about but must be maintained every time the org chart changes. In this case: A static role per plant is simple to reason about when membership is stable.
- **B:** Incorrect for this question. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. Why the correct answer wins: A static role per plant is simple to reason about when membership is stable.
- **C:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: A static role per plant is simple to reason about when membership is stable.
- **D:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: A static role per plant is simple to reason about when membership is stable.

### Question 87 — D

Answer: Review lineage view. Lineage shows which reports depend on which model and source. Lineage shows which reports depend on which model and source, which is how the impact of a change is scoped. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Impact analysis lists the downstream items that will break, which prevents an unannounced outage for report consumers. Why the correct answer wins: Lineage shows which reports depend on which model and source.
- **B:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: Lineage shows which reports depend on which model and source.
- **C:** Incorrect for this question. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. Why the correct answer wins: Lineage shows which reports depend on which model and source.
- **D:** Correct. Lineage shows which reports depend on which model and source, which is how the impact of a change is scoped. In this case: Lineage shows which reports depend on which model and source.

### Question 88 — C

Answer: Run impact analysis before changing the model. Impact analysis lists the dependent items. Impact analysis lists the downstream items that will break, which prevents an unannounced outage for report consumers. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: Impact analysis lists the dependent items.
- **B:** Incorrect for this question. Lineage shows which reports depend on which model and source, which is how the impact of a change is scoped. Why the correct answer wins: Impact analysis lists the dependent items.
- **C:** Correct. Impact analysis lists the downstream items that will break, which prevents an unannounced outage for report consumers. In this case: Impact analysis lists the dependent items.
- **D:** Incorrect for this question. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Why the correct answer wins: Impact analysis lists the dependent items.

### Question 89 — A

Answer: Sync the slicer across the pages that share the same filter. Syncing the slicer keeps one selection consistent across pages. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. In this case: Syncing the slicer keeps one selection consistent across pages.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **C:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.

### Question 90 — B, C

Answers: Use the Decomposition Tree visual; Use Q&A to answer a natural-language question. A decomposition tree supports open-ended drill paths, and Q&A answers a typed question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and Q&A answers a typed question.
- **B:** Correct. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. In this case: A decomposition tree supports open-ended drill paths, and Q&A answers a typed question.
- **C:** Correct. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. In this case: A decomposition tree supports open-ended drill paths, and Q&A answers a typed question.
- **D:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and Q&A answers a typed question.
- **E:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: A decomposition tree supports open-ended drill paths, and Q&A answers a typed question.

### Question 91 — D

Answer: Workspace Viewer role. Viewers read content without editing it. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Viewers read content without editing it.
- **B:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Viewers read content without editing it.
- **C:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Viewers read content without editing it.
- **D:** Correct. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. In this case: Viewers read content without editing it.

### Question 92 — A

Answer: Apply a report theme JSON. A theme applies a consistent palette across the report. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. In this case: A theme applies a consistent palette across the report.
- **B:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: A theme applies a consistent palette across the report.
- **C:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: A theme applies a consistent palette across the report.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A theme applies a consistent palette across the report.

### Question 93 — B

Answer: Create a data alert on a dashboard tile. A data alert notifies when a tile value crosses a threshold. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **B:** Correct. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. In this case: A data alert notifies when a tile value crosses a threshold.
- **C:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.
- **D:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: A data alert notifies when a tile value crosses a threshold.

### Question 94 — B, D

Answers: Configure incremental refresh with the range parameters; Set the RangeStart and RangeEnd parameters the refresh policy expects. An incremental refresh policy partitions the table, and the range parameters must filter the query. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **B:** Correct. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **C:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **D:** Correct. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. In this case: An incremental refresh policy partitions the table, and the range parameters must filter the query.
- **E:** Incorrect for this question. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. Why the correct answer wins: An incremental refresh policy partitions the table, and the range parameters must filter the query.

### Question 95 — D

Answer: Profile the column with column quality, distribution, and profile views. Profiling reports valid, distinct, and empty values per column before shaping. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before shaping.
- **B:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before shaping.
- **C:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before shaping.
- **D:** Correct. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. In this case: Profiling reports valid, distinct, and empty values per column before shaping.

### Question 96 — B

Answer: Build a star schema with a fact table and conformed dimensions. A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **B:** Correct. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. In this case: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **C:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **D:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.

### Question 97 — D, E

Answers: Use an iterator such as SUMX over the row-level expression; Use DIVIDE instead of the division operator. SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Distinct count answers how many unique customers or orders, which a plain count would overstate. Why the correct answer wins: SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error.
- **B:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error.
- **C:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error.
- **D:** Correct. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. In this case: SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error.
- **E:** Correct. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. In this case: SUMX evaluates the row-level arithmetic before aggregating, and DIVIDE avoids a division error.

### Question 98 — C

Answer: Create a dedicated date table marked as the date table. A contiguous date table supplies every date so accumulation does not skip gaps. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **B:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **C:** Correct. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. In this case: A contiguous date table supplies every date so accumulation does not skip gaps.
- **D:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.

### Question 99 — C

Answer: Use LASTNONBLANK when the balance is only recorded on some dates. LASTNONBLANK finds the most recent date that carries a value. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: LASTNONBLANK finds the most recent date that carries a value.
- **B:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: LASTNONBLANK finds the most recent date that carries a value.
- **C:** Correct. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. In this case: LASTNONBLANK finds the most recent date that carries a value.
- **D:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: LASTNONBLANK finds the most recent date that carries a value.

### Question 100 — A

Answer: Use PERCENTILE.INC for a distribution boundary. A percentile returns the boundary value, which describes the tail. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. In this case: A percentile returns the boundary value, which describes the tail.
- **B:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.
- **C:** Incorrect for this question. Descriptive statistics show the shape of the data, which an average alone hides. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.
- **D:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A percentile returns the boundary value, which describes the tail.

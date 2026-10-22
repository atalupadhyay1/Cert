# Microsoft PL-300 — Full-Length Mock Exam 2

Power BI Data Analyst · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. Bed management must see current occupancy as it changes through the shift, and the source can serve a steady query load. Which connection fits?

Domain: Prepare the data

- A. DirectLake over a lakehouse
- B. Live connection to a published semantic model
- C. DirectQuery
- D. Import mode

### 2. A payer needs a weekly snapshot for actuarial reporting and a live view of open claim counts. Which two storage choices fit? Select two.

Domain: Prepare the data

- A. Live connection to a published semantic model
- B. DirectQuery
- C. Import mode
- D. Connect to a shared semantic model instead of importing the source again
- E. DirectLake over a lakehouse

### 3. An analyst must build reports on a published model but is not allowed to edit the model itself. What should be used?

Domain: Prepare the data

- A. Import mode
- B. Live connection to a published semantic model
- C. DirectQuery
- D. Connect to a shared semantic model instead of importing the source again

### 4. A Fabric lakehouse stores Delta tables for patient encounters, and capacity is available. Which mode gives Import-like speed without a copy?

Domain: Prepare the data

- A. DirectLake over a lakehouse
- B. Import mode
- C. DirectQuery
- D. Dual mode table

### 5. Three million claim lines are reported on daily, and the source system cannot tolerate analyst queries. Which mode fits?

Domain: Prepare the data

- A. DirectQuery
- B. Import mode
- C. DirectLake over a lakehouse
- D. Dual mode table

### 6. A privacy rule forbids copying clinical data outside the source system. Which storage mode fits?

Domain: Prepare the data

- A. Import mode
- B. DirectQuery
- C. DirectLake over a lakehouse
- D. Dual mode table

### 7. The same query must read a test lakehouse before release and the production lakehouse afterwards. What should be created?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Create a parameter for the server, path, or filter
- C. Update the data source credentials in the semantic model settings
- D. Change the data source settings rather than rebuilding the query

### 8. A single query combines clinician records with payroll data, and the engine is folding values between them. Which setting prevents that?

Domain: Prepare the data

- A. Change the data source settings rather than rebuilding the query
- B. Set privacy levels to isolate the sources
- C. Update the data source credentials in the semantic model settings
- D. Create a parameter for the server, path, or filter

### 9. Refresh fails overnight with an authentication error after the service account password expired. Where should the fix be applied?

Domain: Prepare the data

- A. Set privacy levels to isolate the sources
- B. Update the data source credentials in the semantic model settings
- C. Create a parameter for the server, path, or filter
- D. Change the data source settings rather than rebuilding the query

### 10. A clinic sends an extract that the team has never seen, and nobody knows how complete it is. What should be done first?

Domain: Prepare the data

- A. Review column statistics and value distribution
- B. Profile the column with column quality, distribution, and profile views
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Correct the column data type before building the model

### 11. A quality team asks whether a few providers account for most of the referrals. Which evidence answers that?

Domain: Prepare the data

- A. Profile the column with column quality, distribution, and profile views
- B. Correct the column data type before building the model
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Review column statistics and value distribution

### 12. An admission date column arrives as text, and monthly grouping fails. What should be corrected before modelling?

Domain: Prepare the data

- A. Replace nulls with a defined placeholder or a filled-down value
- B. Review column statistics and value distribution
- C. Profile the column with column quality, distribution, and profile views
- D. Correct the column data type before building the model

### 13. A new clinical extract is arriving next week, and the team wants to avoid rework. Which sequence is correct?

Domain: Prepare the data

- A. Shape the table → delete the profiling steps → load every column
- B. Profile the source → fix types and nulls → shape the table → load only the needed columns
- C. Load the table → discover the type errors in the report → re-import the source
- D. Load every column → profile in the report → patch the visual

### 14. A patient list has trailing spaces and mixed casing, so one medical record number appears as several members. Which two fixes are required? Select two.

Domain: Prepare the data

- A. Filter out the error rows and report them separately
- B. Use a locale-aware conversion for dates and decimals
- C. Remove duplicate rows using the natural business key
- D. Replace nulls with a defined placeholder or a filled-down value
- E. Trim, clean, and standardize the text values

### 15. A readmission flag is blank for new patients, and the readmission rate dips whenever new patients appear. What should be done?

Domain: Prepare the data

- A. Filter out the error rows and report them separately
- B. Trim, clean, and standardize the text values
- C. Replace nulls with a defined placeholder or a filled-down value
- D. Remove duplicate rows using the natural business key

### 16. One row fails to load because a text value sits in a numeric column. What should be investigated first?

Domain: Prepare the data

- A. Trace the import error to the source type mismatch
- B. Replace nulls with a defined placeholder or a filled-down value
- C. Trim, clean, and standardize the text values
- D. Filter out the error rows and report them separately

### 17. A claims extract has stray characters, duplicated members, and mixed formats. Which sequence is defensible?

Domain: Prepare the data

- A. Identify the bad values → standardize text → convert types → document what was replaced
- B. Replace all values with a default → convert types → load
- C. Filter out the failing rows → load → ask the business later
- D. Convert types first → then look for duplicates → then trim

### 18. The report needs a single field that combines building, floor, and room for a location label. What should be added?

Domain: Prepare the data

- A. Extract the needed part of the text with a delimiter or position
- B. Add a custom column with an M expression
- C. Add a conditional column for rule-based bucketing
- D. Group by the key and aggregate the measures

### 19. A referral identifier begins with a two-letter clinic code, and the duration column arrives as text. Which two transformations are required? Select two.

Domain: Prepare the data

- A. Add an aggregate step with the correct summarization
- B. Split the combined column into separate fields
- C. Correct the column data type before building the model
- D. Extract the needed part of the text with a delimiter or position
- E. Add a custom column with an M expression

### 20. A single provider field holds surname and given name separated by a comma, and the report needs them separately. What should be used?

Domain: Prepare the data

- A. Group by the key and aggregate the measures
- B. Add a custom column with an M expression
- C. Extract the needed part of the text with a delimiter or position
- D. Split the combined column into separate fields

### 21. A pharmacy extract has one column per drug category, and the model needs one category column and one value column. What should be done?

Domain: Prepare the data

- A. Convert the XML or JSON list into a table of rows
- B. Transpose the table so the header becomes a column
- C. Unpivot the month columns into rows
- D. Pivot the attribute values into columns

### 22. A source stores one row per patient-observation pair, and the report needs observations as columns. What should be done?

Domain: Prepare the data

- A. Expand the JSON record into typed columns
- B. Unpivot the month columns into rows
- C. Pivot the attribute values into columns
- D. Transpose the table so the header becomes a column

### 23. A laboratory feed returns an XML document with repeated result elements. What should be done?

Domain: Prepare the data

- A. Convert the list value to a table and expand it
- B. Expand the JSON record into typed columns
- C. Transpose the table so the header becomes a column
- D. Convert the XML or JSON list into a table of rows

### 24. Thirteen weekly ward files share the same columns and must become one table. What should be used?

Domain: Prepare the data

- A. Use a left outer join to keep every fact row
- B. Merge the two queries on a matching key
- C. Use a fuzzy merge with a similarity threshold
- D. Append the queries into one table

### 25. A transformation is complex and slow, and the team needs to test it separately from the extraction. Which two choices fit? Select two.

Domain: Prepare the data

- A. Use a native query to select only the needed rows
- B. Stage the raw query and build a separate clean query on it
- C. Keep the steps foldable so the source does the work
- D. Disable load on the staging query
- E. Duplicate the query so the two are independent

### 26. Authors keep using the record identifier as a label, and date totals display without formatting. Which two actions fix that? Select two.

Domain: Model the data

- A. Build a star schema with a fact table and conformed dimensions
- B. Normalize the dimension into a snowflake
- C. Flatten the lookup attributes into a single dimension
- D. Set the table and column properties, including hidden keys and format strings
- E. Hide technical columns from the report view

### 27. A clinical model must be rebuilt from one wide extract. Which sequence produces a maintainable model?

Domain: Model the data

- A. Keep one wide table → relate it to itself → build measures
- B. Build the relationships first → decide the grain afterwards → load
- C. Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact
- D. Create a dimension per column → relate each one to the fact

### 28. A payer table hangs off the patient dimension, and every filter crosses two hops. What should be done?

Domain: Model the data

- A. Build a star schema with a fact table and conformed dimensions
- B. Set the table and column properties, including hidden keys and format strings
- C. Normalize the dimension into a snowflake
- D. Flatten the lookup attributes into a single dimension

### 29. Admission date and discharge date both relate to the date table, but only one filters the report. Why?

Domain: Model the data

- A. One-to-one relationship between two tables with the same grain
- B. One-to-many relationship from the dimension to the fact
- C. Inactive relationship activated with USERELATIONSHIP
- D. Single-direction filter from dimension to fact

### 30. A new claims fact must filter from its dimensions and must never let one dimension filter another. Which two choices fit? Select two.

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. Many-to-many relationship with a bridging table
- C. Bi-directional cross-filtering on the relationship
- D. Single-direction filter from dimension to fact
- E. Set the cross-filter direction on the relationship

### 31. A clinic visual does not respond when a claim visual is selected, and the model is suspected. Which setting decides that?

Domain: Model the data

- A. Inactive relationship activated with USERELATIONSHIP
- B. Bi-directional cross-filtering on the relationship
- C. Set the cross-filter direction on the relationship
- D. Single-direction filter from dimension to fact

### 32. Rolling admission counts skip days with no activity, and the running total looks wrong. What is missing?

Domain: Model the data

- A. Build the fiscal periods as columns in the date table
- B. Mark the table as a date table
- C. Create one date table and role-play it through several relationships
- D. Create a dedicated date table marked as the date table

### 33. Admission, discharge, and billing dates all need the same year-quarter-month logic. What should be used?

Domain: Model the data

- A. Create one date table and role-play it through several relationships
- B. Build the fiscal periods as columns in the date table
- C. Mark the table as a date table
- D. Create a dedicated date table marked as the date table

### 34. A date table exists, but the engine still picks a fact date column as the date source. What should be done?

Domain: Model the data

- A. Create a dedicated date table marked as the date table
- B. Build the fiscal periods as columns in the date table
- C. Create one date table and role-play it through several relationships
- D. Mark the table as a date table

### 35. A quality dashboard needs dependable year-to-date and prior-year values. Which sequence delivers that?

Domain: Model the data

- A. Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it
- B. Create one date table per date column → relate all of them to the fact
- C. Create a date table → leave it unrelated → filter with it
- D. Use the fact date column directly → write TOTALYTD → add a date slicer

### 36. A length-of-stay figure must respond to ward and period slicers without adding a stored column. What should be created?

Domain: Model the data

- A. Create a measure for the aggregation
- B. The filter context supplied by the visual, slicers, and page filters
- C. Create a calculated column
- D. Create a calculated table

### 37. A discharge category is needed as a slicer field and depends on two columns in the same row. What should be created?

Domain: Model the data

- A. Create a measure for the aggregation
- B. Create a calculated table
- C. Create a calculated column
- D. The row context inside an iterator

### 38. A report needs a readmission rate that survives a zero denominator and a count of unique patients. Which two functions fit? Select two.

Domain: Model the data

- A. Use an iterator such as SUMX over the row-level expression
- B. Use an iterator function for row-level arithmetic
- C. Create a measure for the aggregation
- D. Use DIVIDE instead of the division operator
- E. Use DISTINCT COUNT for unique entities

### 39. A measure must report the share of total admissions while the visual still shows one clinic per row. Which function changes the filter context?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Add KEEPFILTERS to intersect rather than replace the filter
- C. Wrap the aggregation in CALCULATE to change the filter context
- D. Store intermediate results in VAR and RETURN

### 40. A share measure must calculate within the period the reader picked, whatever clinic rows the matrix shows. Which modifier keeps the selection but drops the row grouping?

Domain: Model the data

- A. Use ALLSELECTED to respect the slicer but ignore the visual
- B. Use ALL on the table to clear its filters
- C. Add KEEPFILTERS to intersect rather than replace the filter
- D. Remove the filter with REMOVEFILTERS or ALL

### 41. A complex measure repeats the same denominator expression twice and reads badly. What should be used?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Add KEEPFILTERS to intersect rather than replace the filter
- C. Store intermediate results in VAR and RETURN
- D. Wrap the aggregation in CALCULATE to change the filter context

### 42. A measure that must stay within the chosen quarter is returning values for the whole year. Which modifier fixes it?

Domain: Model the data

- A. Use ALL on the table to clear its filters
- B. Use ALLSELECTED to respect the slicer but ignore the visual
- C. Remove the filter with REMOVEFILTERS or ALL
- D. Add KEEPFILTERS to intersect rather than replace the filter

### 43. Ward occupancy is recorded only on days with activity, so the month-end figure lands on a blank day. What should be used?

Domain: Model the data

- A. Use LASTNONBLANK when the balance is only recorded on some dates
- B. Use AVERAGEX over a rolling date window
- C. Use TOTALYTD or DATESYTD for year-to-date
- D. Use LASTNONBLANK or LASTDATE for a semi-additive balance

### 44. A daily admission series is too noisy to read, and the team wants a smoothing view. What should be used?

Domain: Model the data

- A. Use AVERAGEX over a rolling date window
- B. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- C. Use DATESINPERIOD for a windowed calculation
- D. Use TOTALYTD or DATESYTD for year-to-date

### 45. A measure must cover the 90 days ending on the selected date. What should be used?

Domain: Model the data

- A. Use TOTALYTD or DATESYTD for year-to-date
- B. Use SAMEPERIODLASTYEAR or DATEADD for the comparable period
- C. Use DATESINPERIOD for a windowed calculation
- D. Build the measure against the marked date table

### 46. Thirty measures each need month-to-date, quarter-to-date, and year-to-date variants. What should be used?

Domain: Model the data

- A. Create a calculation group for the time-intelligence variants
- B. Use a quick measure for the standard pattern
- C. Create a numeric range parameter for scenario analysis
- D. Create a field parameter so the author can switch the measure or axis

### 47. One page must let readers switch between cost and readmission rate, and test a staffing assumption. Which two features fit? Select two.

Domain: Model the data

- A. Create a numeric range parameter for scenario analysis
- B. Use PERCENTILE.INC for a distribution boundary
- C. Create a field parameter so the author can switch the measure or axis
- D. Create a calculation group for the time-intelligence variants
- E. Use a quick measure for the standard pattern

### 48. A service must state the wait time below which 90 percent of patients are seen. What should be used?

Domain: Model the data

- A. Use PERCENTILE.INC for a distribution boundary
- B. Use a statistical function such as STDEV.P or MEDIAN to describe the spread
- C. Use a quick measure for the standard pattern
- D. Create a calculation group for the time-intelligence variants

### 49. A model stores a free-text note field with hundreds of thousands of distinct values. Which storage behaviour makes that expensive?

Domain: Model the data

- A. Reduce column cardinality and width to shrink the VertiPaq store
- B. Run Performance Analyzer to find the slow visual
- C. Inspect the query plan in DAX query view
- D. Reduce the granularity loaded into the model

### 50. One measure is suspected of generating an expensive query, and the author needs to see the query plan. What should be used?

Domain: Model the data

- A. Remove unnecessary rows and columns before optimizing measures
- B. Run Performance Analyzer to find the slow visual
- C. Inspect the query plan in DAX query view
- D. Reduce column cardinality and width to shrink the VertiPaq store

### 51. A report must show clinic by month with subtotals in both directions. Which visual fits?

Domain: Visualize and analyze the data

- A. A scatter chart
- B. A waterfall chart
- C. A clustered bar or column chart
- D. A matrix visual with row and column groups

### 52. A quality team must see whether length of stay relates to readmission risk across patients. Which visual fits?

Domain: Visualize and analyze the data

- A. A scatter chart
- B. A line chart with a date axis
- C. A pie or donut chart
- D. A clustered bar or column chart

### 53. A page needs a monthly trend and a view of drop-off between referral stages. Which two visuals fit? Select two.

Domain: Visualize and analyze the data

- A. A treemap
- B. A matrix visual with row and column groups
- C. A funnel chart
- D. A line chart with a date axis
- E. A KPI visual with a target

### 54. Readers need a visible control for choosing a clinic on the page. What should be added?

Domain: Visualize and analyze the data

- A. A slicer on the report page
- B. Set the filter pane scope by page, report, or visual
- C. Edit the interactions so the visual does not filter the others
- D. Sync the slicer across the pages that share the same filter

### 55. Selecting a clinic in one visual is filtering a stable summary card that should not change. What should be changed?

Domain: Visualize and analyze the data

- A. Set the filter pane scope by page, report, or visual
- B. Sync the slicer across the pages that share the same filter
- C. Edit the interactions so the visual does not filter the others
- D. A slicer on the report page

### 56. A period restriction has to hold on every page of a multi-page report. Where should that filter sit?

Domain: Visualize and analyze the data

- A. Edit the interactions so the visual does not filter the others
- B. A slicer on the report page
- C. Sync the slicer across the pages that share the same filter
- D. Set the filter pane scope by page, report, or visual

### 57. A ward view and a trust view share one page, and readers must switch between saved states. What should be captured?

Domain: Visualize and analyze the data

- A. Capture the view in a bookmark
- B. Add a page navigator for the report
- C. Add buttons with actions that navigate or apply a bookmark
- D. Use the Selection pane to group and layer visuals

### 58. Two bookmarks exist, and readers must apply one with a single click from the canvas. What should be added?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Capture the view in a bookmark
- C. Add buttons with actions that navigate or apply a bookmark
- D. Use the Selection pane to group and layer visuals

### 59. A single page must serve three saved views through buttons. Which sequence works?

Domain: Visualize and analyze the data

- A. Capture a bookmark before setting the filters → expect it to restore them
- B. Create a page per view → duplicate the visuals → maintain each page
- C. Create the views → capture each in a bookmark → add buttons → hide the visuals not in use
- D. Use buttons without actions → tell readers to click twice

### 60. The report will grow to twelve pages and needs navigation that stays current automatically. What should be used?

Domain: Visualize and analyze the data

- A. Add a page navigator for the report
- B. Use the Selection pane to group and layer visuals
- C. Add buttons with actions that navigate or apply a bookmark
- D. Capture the view in a bookmark

### 61. A reader must click a ward and open a detail page about that ward's patients. What should be configured?

Domain: Visualize and analyze the data

- A. Configure a drillthrough page with the entity filter
- B. Enable drill-down through the hierarchy
- C. Edit the interactions so the visual does not filter the others
- D. Set the filter pane scope by page, report, or visual

### 62. One visual must step from year to quarter to month while the chart itself stays in place. What should be enabled?

Domain: Visualize and analyze the data

- A. Configure a drillthrough page with the entity filter
- B. Build a custom tooltip page
- C. Use the Selection pane to group and layer visuals
- D. Enable drill-down through the hierarchy

### 63. Hovering a point must reveal occupancy, staffing, and readmission rate together. Which two actions deliver that? Select two.

Domain: Visualize and analyze the data

- A. Set the tooltip to a report page and size it to the hover area
- B. Enable drill-down through the hierarchy
- C. Build a custom tooltip page
- D. Use the Selection pane to group and layer visuals
- E. Configure a drillthrough page with the entity filter

### 64. A clinical team is building its first drillthrough page. Which sequence works?

Domain: Visualize and analyze the data

- A. Choose the entity field → create the drillthrough page → place the entity filter → add a back button
- B. Set the drillthrough filter → publish → skip the back button
- C. Put every field on the summary visual → expect drillthrough to work
- D. Create the detail page → add a visual → tell readers to filter it manually

### 65. The report must be usable by screen-reader users, and visuals carry no descriptions. What must be added?

Domain: Visualize and analyze the data

- A. Set a logical tab order for the interactive elements
- B. Provide alt text for each meaningful visual
- C. Enable personalization for the visuals the reader may change
- D. Build the mobile layout in the mobile view

### 66. Keyboard users cannot reach the slicers in a sensible sequence. What should be configured?

Domain: Visualize and analyze the data

- A. Provide alt text for each meaningful visual
- B. Set a logical tab order for the interactive elements
- C. Build the mobile layout in the mobile view
- D. Configure the export and download settings for the report

### 67. Clinical data must not be downloaded from the report by readers. What should be configured?

Domain: Visualize and analyze the data

- A. Build the mobile layout in the mobile view
- B. Provide alt text for each meaningful visual
- C. Configure the export and download settings for the report
- D. Enable personalization for the visuals the reader may change

### 68. Every page must share one palette and font family without styling each visual. What should be applied?

Domain: Visualize and analyze the data

- A. Turn on and format data labels
- B. Use the Selection pane to group and layer visuals
- C. Apply conditional formatting driven by a measure
- D. Apply a report theme JSON

### 69. A six-bar chart must show exact values without the reader reading the axis. What should be enabled?

Domain: Visualize and analyze the data

- A. Apply conditional formatting driven by a measure
- B. Set the axis range and units explicitly
- C. Apply a report theme JSON
- D. Turn on and format data labels

### 70. Exceptions must stand out by colour, and a bar axis must not exaggerate small differences. Which two settings are required? Select two.

Domain: Visualize and analyze the data

- A. Apply a report theme JSON
- B. Apply conditional formatting driven by a measure
- C. Set the axis range and units explicitly
- D. Use the Selection pane to group and layer visuals
- E. Turn on and format data labels

### 71. A director asks why admissions rose last month, and the model has many dimensions. Which feature helps?

Domain: Visualize and analyze the data

- A. Use the Analyze feature to explain a change
- B. Use the outlier detection feature on the visual
- C. Use clustering to find segments in the data
- D. Use the built-in forecast on a line chart

### 72. A daily series contains a handful of points far from the pattern, and the team wants them surfaced. What should be used?

Domain: Visualize and analyze the data

- A. Add error bars to show the uncertainty range
- B. Use the outlier detection feature on the visual
- C. Create groups for the categories that matter
- D. Add a reference line for the target or average

### 73. Patients must be segmented by utilization without a predefined scheme. What should be used?

Domain: Visualize and analyze the data

- A. Use the built-in forecast on a line chart
- B. Create bins for a continuous measure
- C. Create groups for the categories that matter
- D. Use clustering to find segments in the data

### 74. A root-cause page must let analysts choose any dimension in any order. Which visual fits?

Domain: Visualize and analyze the data

- A. Use Q&A to answer a natural-language question
- B. Use Copilot to suggest a report page
- C. Use the Decomposition Tree visual
- D. Use the Key Influencers visual

### 75. An author wants a first draft of a new report page from a written prompt. Which feature fits?

Domain: Visualize and analyze the data

- A. Use Copilot to suggest a report page
- B. Use Copilot to create a narrative visual
- C. Use the Key Influencers visual
- D. Use Q&A to answer a natural-language question

### 76. A clinical analytics team needs one place where its authors collaborate on shared content. What should be created?

Domain: Manage and secure Power BI

- A. Publish an app from the workspace
- B. Create a workspace for the team that owns the content
- C. Workspace Viewer role
- D. Workspace Admin role

### 77. One person must manage membership and workspace settings after the original owner leaves. Which role fits?

Domain: Manage and secure Power BI

- A. Workspace Contributor role
- B. Workspace Member role
- C. Workspace Admin role
- D. Workspace Viewer role

### 78. Consumers should get a curated, read-only experience rather than access to every item in the workspace. What should be published?

Domain: Manage and secure Power BI

- A. Choose the distribution method that matches the audience
- B. Create a workspace for the team that owns the content
- C. Define an app audience for each group of consumers
- D. Publish an app from the workspace

### 79. A trust must decide whether to use an app, a direct link, or embedding for a board pack. What is being decided?

Domain: Manage and secure Power BI

- A. Create a workspace for the team that owns the content
- B. Update the app after changing the workspace content
- C. Choose the distribution method that matches the audience
- D. Define an app audience for each group of consumers

### 80. The team is publishing its first clinical app to two audiences. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Give every consumer the workspace Viewer role → skip the app
- B. Build in the workspace → curate the app pages → assign audiences → publish and update the app
- C. Publish the app before the report is finished → update it never
- D. Create one app per person → assign each audience manually

### 81. A single metric must be watched on a monitoring page and stay linked to its report. What should be created?

Domain: Manage and secure Power BI

- A. Create a dashboard in the service
- B. Pin the visual to a dashboard tile
- C. Create a subscription for the report or dashboard
- D. Create a data alert on a dashboard tile

### 82. A threshold notification must be configured on one specific card tile. What should be used?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Pin the visual to a dashboard tile
- C. Create a data alert on a dashboard tile
- D. Set the alert threshold on the pinned card tile

### 83. The source database sits inside an Azure virtual network that the service cannot reach directly. What should be used?

Domain: Manage and secure Power BI

- A. Configure scheduled refresh on the semantic model
- B. Virtual network data gateway
- C. Install an on-premises data gateway
- D. Personal mode gateway

### 84. A three-year claims table must load incrementally. Which sequence is correct?

Domain: Manage and secure Power BI

- A. Load all history every refresh → add a policy later → hope it rebuilds
- B. Configure the policy in Desktop → publish → assume partitions were created
- C. Filter the query by date → set the policy → skip the parameters
- D. Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh

### 85. A security role has been written, and the team wants to confirm what a member actually sees before release. What should be used?

Domain: Manage and secure Power BI

- A. Define a row-level security role with a DAX filter
- B. Test the role with View as role in the service
- C. Add the security group to the role membership
- D. Use a dynamic RLS rule based on USERPRINCIPALNAME

### 86. Role membership is maintained person by person and drifts after every transfer. What should be used instead?

Domain: Manage and secure Power BI

- A. Map the signed-in user with USERPRINCIPALNAME in the filter
- B. Add the security group to the role membership
- C. A static RLS role per region with fixed members
- D. Define a row-level security role with a DAX filter

### 87. A team wants to signal that its model is ready for reuse within the department. What should be applied?

Domain: Manage and secure Power BI

- A. Apply a sensitivity label to the semantic model and report
- B. Certify the semantic model
- C. Grant item-level access to the specific report
- D. Promote the content as endorsed

### 88. One external auditor needs a single report without joining the workspace. What should be granted?

Domain: Manage and secure Power BI

- A. Certify the semantic model
- B. Grant item-level access to the specific report
- C. Create a workspace for the team that owns the content
- D. Grant Build permission on the semantic model

---

## Case study — Cambria Insurance

Cambria Insurance reports on 1.2 million policies, and the monthly board pack must explain how opening policy counts became closing counts. The pack runs to four pages, all filtered to the same policy period, and readers keep re-applying that filter on every page. The retention team also wants to understand which factors are associated with lapses and to ask ad hoc questions without waiting for another page to be built. The model is imported and refreshes nightly from the policy administration system.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. The board pack must explain how opening policy counts became closing counts across the month. Which visual fits?

Domain: Visualize and analyze the data

- A. A funnel chart
- B. A waterfall chart
- C. A gauge visual
- D. A treemap

### 90. A chosen policy period must stay applied while readers move across four pages of the report. What should be configured?

Domain: Visualize and analyze the data

- A. Set the filter pane scope by page, report, or visual
- B. Edit the interactions so the visual does not filter the others
- C. A slicer on the report page
- D. Sync the slicer across the pages that share the same filter

### 91. The team wants the factors associated with lapses and a way for managers to ask ad hoc questions. Which two features fit? Select two.

Domain: Visualize and analyze the data

- A. Use Q&A to answer a natural-language question
- B. Use the Key Influencers visual
- C. Use the Decomposition Tree visual
- D. Use Copilot to suggest a report page
- E. Use Copilot to create a narrative visual

---

## Case study — Harborline Grocers

Harborline Grocers operates 300 stores and runs more than 400 promotions a year, several of them across many stores at once. Its visit table repeats store name, region, and district on every row, and category filters have slowed to a crawl. The sales fact holds every basket line and is slow to summarize, yet merchandisers still need to reach transaction detail when a number looks wrong. Promotion analysis needs a relationship that respects the many-to-many pattern between promotions and stores.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The visit table repeats store name, region, and district on every row, and filters are slow. What should be built?

Domain: Model the data

- A. Normalize the dimension into a snowflake
- B. Build a star schema with a fact table and conformed dimensions
- C. Flatten the lookup attributes into a single dimension
- D. Set the table and column properties, including hidden keys and format strings

### 93. Promotions run across many stores and stores run many promotions, with a promotion-store table between them. Which relationship shape is required?

Domain: Model the data

- A. One-to-many relationship from the dimension to the fact
- B. One-to-one relationship between two tables with the same grain
- C. Many-to-many relationship with a bridging table
- D. Single-direction filter from dimension to fact

### 94. The sales fact is slow to summarize but must stay available at transaction level. Which two actions fit? Select two.

Domain: Model the data

- A. Remove the high-cardinality columns the report does not use
- B. Reduce column cardinality and width to shrink the VertiPaq store
- C. Remove unnecessary rows and columns before optimizing measures
- D. Reduce the granularity loaded into the model
- E. Add an aggregation table for the large fact

---

## Case study — Pinecrest Clinics

Pinecrest Clinics is a 60-clinic network that reports admissions from a shared electronic record system. The analytics team must use the clinical model the data office certifies, because a second definition of length of stay caused a board dispute last year. Encounter rows arrive at patient level, but the operations review needs one row per clinician per month. Clinic names sit in a lookup table keyed on a composite of site and clinic code, and the relationship must handle that shape.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. The analytics team must report on admissions without creating a second definition of length of stay. Which action fits?

Domain: Prepare the data

- A. Import mode
- B. DirectQuery
- C. Connect to a shared semantic model instead of importing the source again
- D. DirectLake over a lakehouse

### 96. Encounter rows must become one row per clinician per month before loading. What should be used?

Domain: Prepare the data

- A. Add an aggregate step with the correct summarization
- B. Add a custom column with an M expression
- C. Add a conditional column for rule-based bucketing
- D. Group by the key and aggregate the measures

### 97. The fact table must gain clinic name, and the relationship will be built on a composite of site and clinic codes. Which two choices fit? Select two.

Domain: Prepare the data

- A. Append the queries into one table
- B. Merge the two queries on a matching key
- C. Use a left outer join to keep every fact row
- D. Use a fuzzy merge with a similarity threshold
- E. Create an integer surrogate key for the relationship

---

## Case study — Solstice Energy

Solstice Energy reports outage and meter data for 2.1 million supply points, refreshed from an operational system every two hours. A small team of authors publishes the reports, while field crews need to read them on a phone without changing anything. The board asks for a monthly PDF snapshot of the outage report, and the service account used for refresh has a credential that expires every 90 days. The team has been caught twice by a refresh that failed silently overnight.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Authors must publish and edit reports, and field crews must read without editing. Which two roles fit? Select two.

Domain: Manage and secure Power BI

- A. Workspace Member role
- B. Workspace Contributor role
- C. Workspace Viewer role
- D. Workspace Admin role
- E. Publish an app from the workspace

### 99. A board member wants a PDF snapshot of the outage report every month. What should be configured?

Domain: Manage and secure Power BI

- A. Create a subscription for the report or dashboard
- B. Create a dashboard in the service
- C. Set the alert threshold on the pinned card tile
- D. Create a data alert on a dashboard tile

### 100. The meter model must refresh every two hours, and the service account credential expires every 90 days. Which two settings matter? Select two.

Domain: Manage and secure Power BI

- A. Install an on-premises data gateway
- B. Configure scheduled refresh on the semantic model
- C. Update the credentials used by the refresh schedule
- D. Configure incremental refresh with the range parameters
- E. Set the RangeStart and RangeEnd parameters the refresh policy expects

---

## Answer key and explanations

### Question 1 — C

Answer: DirectQuery. DirectQuery reads the source at report time, which is what live occupancy requires. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery reads the source at report time, which is what live occupancy requires.
- **B:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: DirectQuery reads the source at report time, which is what live occupancy requires.
- **C:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery reads the source at report time, which is what live occupancy requires.
- **D:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery reads the source at report time, which is what live occupancy requires.

### Question 2 — B, C

Answers: Import mode; DirectQuery. The weekly snapshot is best imported, while the open claim count must query the source directly. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Why the correct answer wins: The weekly snapshot is best imported, while the open claim count must query the source directly.
- **B:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: The weekly snapshot is best imported, while the open claim count must query the source directly.
- **C:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: The weekly snapshot is best imported, while the open claim count must query the source directly.
- **D:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: The weekly snapshot is best imported, while the open claim count must query the source directly.
- **E:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: The weekly snapshot is best imported, while the open claim count must query the source directly.

### Question 3 — B

Answer: Live connection to a published semantic model. A live connection gives report authoring on a governed model without editing it. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: A live connection gives report authoring on a governed model without editing it.
- **B:** Correct. A live connection reuses a governed semantic model without copying it, so consistency and security are inherited and the report is not edited in Desktop. In this case: A live connection gives report authoring on a governed model without editing it.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: A live connection gives report authoring on a governed model without editing it.
- **D:** Incorrect for this question. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Why the correct answer wins: A live connection gives report authoring on a governed model without editing it.

### Question 4 — A

Answer: DirectLake over a lakehouse. DirectLake reads the Delta tables directly when the workspace has the capacity it needs. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. In this case: DirectLake reads the Delta tables directly when the workspace has the capacity it needs.
- **B:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectLake reads the Delta tables directly when the workspace has the capacity it needs.
- **C:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: DirectLake reads the Delta tables directly when the workspace has the capacity it needs.
- **D:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectLake reads the Delta tables directly when the workspace has the capacity it needs.

### Question 5 — B

Answer: Import mode. Import moves the query load off the source and serves reports from memory. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Import moves the query load off the source and serves reports from memory.
- **B:** Correct. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. In this case: Import moves the query load off the source and serves reports from memory.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Import moves the query load off the source and serves reports from memory.
- **D:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: Import moves the query load off the source and serves reports from memory.

### Question 6 — B

Answer: DirectQuery. DirectQuery leaves the data in place and reads it at query time. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Local study-map skill 1.2 (Choosing Import, DirectQuery, or DirectLake), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: DirectQuery leaves the data in place and reads it at query time.
- **B:** Correct. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. In this case: DirectQuery leaves the data in place and reads it at query time.
- **C:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: DirectQuery leaves the data in place and reads it at query time.
- **D:** Incorrect for this question. A Dual table can act as Import for some relationships and DirectQuery for others, which reduces the number of DirectQuery round trips in a composite model. Why the correct answer wins: DirectQuery leaves the data in place and reads it at query time.

### Question 7 — B

Answer: Create a parameter for the server, path, or filter. A parameter swaps the environment without editing the M code. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **B:** Correct. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. In this case: A parameter swaps the environment without editing the M code.
- **C:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: A parameter swaps the environment without editing the M code.
- **D:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: A parameter swaps the environment without editing the M code.

### Question 8 — B

Answer: Set privacy levels to isolate the sources. Privacy levels stop the engine combining values across sources that must stay separate. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: Privacy levels stop the engine combining values across sources that must stay separate.
- **B:** Correct. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. In this case: Privacy levels stop the engine combining values across sources that must stay separate.
- **C:** Incorrect for this question. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Why the correct answer wins: Privacy levels stop the engine combining values across sources that must stay separate.
- **D:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: Privacy levels stop the engine combining values across sources that must stay separate.

### Question 9 — B

Answer: Update the data source credentials in the semantic model settings. The stored credential in the data source settings is what the service authenticates with. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. Local study-map skill 1.3 (Data Source Settings, Credentials, Privacy Levels, and Parameters), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Privacy levels stop the engine from folding data across sources it should not combine, which prevents accidental exposure of confidential values. Why the correct answer wins: The stored credential in the data source settings is what the service authenticates with.
- **B:** Correct. Credentials live with the data source connection in the service, so a changed password must be updated there or refresh fails. In this case: The stored credential in the data source settings is what the service authenticates with.
- **C:** Incorrect for this question. A parameter lets one query point at different environments without editing the M code, which makes promotion between dev, test, and prod safe. Why the correct answer wins: The stored credential in the data source settings is what the service authenticates with.
- **D:** Incorrect for this question. Editing the connection keeps the applied steps and lets you repoint an existing query at a new location. Why the correct answer wins: The stored credential in the data source settings is what the service authenticates with.

### Question 10 — B

Answer: Profile the column with column quality, distribution, and profile views. Profiling reports valid, distinct, and empty values per column before any shaping begins. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before any shaping begins.
- **B:** Correct. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. In this case: Profiling reports valid, distinct, and empty values per column before any shaping begins.
- **C:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before any shaping begins.
- **D:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Profiling reports valid, distinct, and empty values per column before any shaping begins.

### Question 11 — D

Answer: Review column statistics and value distribution. Value distribution shows whether the measure is concentrated in a few members. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **B:** Incorrect for this question. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **C:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Value distribution shows whether the measure is concentrated in a few members.
- **D:** Correct. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. In this case: Value distribution shows whether the measure is concentrated in a few members.

### Question 12 — D

Answer: Correct the column data type before building the model. A text date cannot drive time intelligence, so the type must be fixed at the source of the query. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be fixed at the source of the query.
- **B:** Incorrect for this question. Value distribution reveals skew, unexpected dominant values, and long tails that a simple row count hides. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be fixed at the source of the query.
- **C:** Incorrect for this question. Profiling shows how many values are valid, distinct, and empty before any transformation is chosen. Why the correct answer wins: A text date cannot drive time intelligence, so the type must be fixed at the source of the query.
- **D:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: A text date cannot drive time intelligence, so the type must be fixed at the source of the query.

### Question 13 — B

Answer: Profile the source → fix types and nulls → shape the table → load only the needed columns. Profiling comes first, shaping follows, and loading only needed columns keeps the model small. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. Local study-map skill 1.4 (Evaluating Data with Profiling and Column Statistics), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Deleting profiling removes the evidence of quality problems and loading every column inflates the model. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **B:** Correct. Profiling first prevents wasted shaping, and typing before loading keeps the model small and time intelligence working. In this case: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **C:** Incorrect for this question. Discovering type errors after load means the model was built on wrong data and the work restarts. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.
- **D:** Incorrect for this question. Patching visuals hides the data problem instead of fixing it at the source. Why the correct answer wins: Profiling comes first, shaping follows, and loading only needed columns keeps the model small.

### Question 14 — C, E

Answers: Trim, clean, and standardize the text values; Remove duplicate rows using the natural business key. Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies.
- **B:** Incorrect for this question. A locale-aware conversion stops day and month being swapped and stops decimal commas being interpreted as text. Why the correct answer wins: Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies.
- **C:** Correct. De-duplicating on the business key prevents double counting when a source system repeats records across loads. In this case: Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies.
- **D:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies.
- **E:** Correct. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. In this case: Standardizing the text removes the invisible differences, and de-duplicating on the record number collapses the copies.

### Question 15 — C

Answer: Replace nulls with a defined placeholder or a filled-down value. Replacing blank with a defined value keeps the denominator stable and documents the assumption. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Replacing blank with a defined value keeps the denominator stable and documents the assumption.
- **B:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Replacing blank with a defined value keeps the denominator stable and documents the assumption.
- **C:** Correct. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. In this case: Replacing blank with a defined value keeps the denominator stable and documents the assumption.
- **D:** Incorrect for this question. De-duplicating on the business key prevents double counting when a source system repeats records across loads. Why the correct answer wins: Replacing blank with a defined value keeps the denominator stable and documents the assumption.

### Question 16 — A

Answer: Trace the import error to the source type mismatch. Most import errors are a value that does not match the declared type, so the source column is the place to look. Most import errors come from a value that does not match the declared type, so the fix is at the source column or an explicit conversion. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Most import errors come from a value that does not match the declared type, so the fix is at the source column or an explicit conversion. In this case: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **B:** Incorrect for this question. Replacing nulls makes aggregations reproducible; the placeholder must be documented so it is not mistaken for a measurement. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **C:** Incorrect for this question. Leading spaces, inconsistent casing, and stray characters create duplicate dimension members and break joins. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.
- **D:** Incorrect for this question. Removing errors keeps the model loadable, but the discarded rows must be reported so the business knows what is missing. Why the correct answer wins: Most import errors are a value that does not match the declared type, so the source column is the place to look.

### Question 17 — A

Answer: Identify the bad values → standardize text → convert types → document what was replaced. Standardizing before conversion fixes the cause, and documenting the replacement keeps the change auditable. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. Local study-map skill 1.5 (Resolving Inconsistencies, Nulls, and Import Errors), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Cleaning in that order fixes the cause, and documenting the replacement keeps the change auditable. In this case: Standardizing before conversion fixes the cause, and documenting the replacement keeps the change auditable.
- **B:** Incorrect for this question. Replacing everything with a default destroys real values and hides the pattern behind the error. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps the change auditable.
- **C:** Incorrect for this question. Silently dropping rows changes the totals and the business never learns what is missing. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps the change auditable.
- **D:** Incorrect for this question. Converting before trimming fails on values that only differ by whitespace and leaves duplicates behind. Why the correct answer wins: Standardizing before conversion fixes the cause, and documenting the replacement keeps the change auditable.

### Question 18 — B

Answer: Add a custom column with an M expression. A custom column concatenates the fields row by row into the label the report needs. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: A custom column concatenates the fields row by row into the label the report needs.
- **B:** Correct. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. In this case: A custom column concatenates the fields row by row into the label the report needs.
- **C:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: A custom column concatenates the fields row by row into the label the report needs.
- **D:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: A custom column concatenates the fields row by row into the label the report needs.

### Question 19 — C, D

Answers: Extract the needed part of the text with a delimiter or position; Correct the column data type before building the model. Extracting the prefix creates the clinic field, and converting the type makes duration measurable. Extraction keeps the useful part of an identifier without importing the whole string into the model. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Extracting the prefix creates the clinic field, and converting the type makes duration measurable.
- **B:** Incorrect for this question. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Why the correct answer wins: Extracting the prefix creates the clinic field, and converting the type makes duration measurable.
- **C:** Correct. A wrong data type blocks time intelligence, breaks relationships, and inflates the model through text storage of numbers and dates. In this case: Extracting the prefix creates the clinic field, and converting the type makes duration measurable.
- **D:** Correct. Extraction keeps the useful part of an identifier without importing the whole string into the model. In this case: Extracting the prefix creates the clinic field, and converting the type makes duration measurable.
- **E:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Extracting the prefix creates the clinic field, and converting the type makes duration measurable.

### Question 20 — D

Answer: Split the combined column into separate fields. Splitting on the delimiter separates the two parts cleanly. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Why the correct answer wins: Splitting on the delimiter separates the two parts cleanly.
- **B:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Splitting on the delimiter separates the two parts cleanly.
- **C:** Incorrect for this question. Extraction keeps the useful part of an identifier without importing the whole string into the model. Why the correct answer wins: Splitting on the delimiter separates the two parts cleanly.
- **D:** Correct. Splitting separates values that are packed into one field so each can be typed, filtered, and related correctly. In this case: Splitting on the delimiter separates the two parts cleanly.

### Question 21 — C

Answer: Unpivot the month columns into rows. Unpivoting turns the category columns into rows, which is the shape the model needs. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Why the correct answer wins: Unpivoting turns the category columns into rows, which is the shape the model needs.
- **B:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Unpivoting turns the category columns into rows, which is the shape the model needs.
- **C:** Correct. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. In this case: Unpivoting turns the category columns into rows, which is the shape the model needs.
- **D:** Incorrect for this question. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Why the correct answer wins: Unpivoting turns the category columns into rows, which is the shape the model needs.

### Question 22 — C

Answer: Pivot the attribute values into columns. Pivoting turns the observation rows into columns. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Pivoting turns the observation rows into columns.
- **B:** Incorrect for this question. Unpivoting turns wide period columns into a single date column and a single value column, which is what a tabular model needs. Why the correct answer wins: Pivoting turns the observation rows into columns.
- **C:** Correct. Pivoting turns row-based attribute values into columns, which suits a cross-tab source that must become a flat table. In this case: Pivoting turns the observation rows into columns.
- **D:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Pivoting turns the observation rows into columns.

### Question 23 — D

Answer: Convert the XML or JSON list into a table of rows. Converting the XML elements into a table of rows makes each result addressable. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. Local study-map skill 1.7 (Pivot, Unpivot, Transpose, and Semi-Structured Data), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Converting a list to a table preserves every element as a row instead of keeping only the first value. Why the correct answer wins: Converting the XML elements into a table of rows makes each result addressable.
- **B:** Incorrect for this question. Expanding a JSON record exposes its fields as columns that can be typed, filtered, and related. Why the correct answer wins: Converting the XML elements into a table of rows makes each result addressable.
- **C:** Incorrect for this question. Transposing swaps rows and columns, which repairs a report-shaped sheet whose headings run down the side. Why the correct answer wins: Converting the XML elements into a table of rows makes each result addressable.
- **D:** Correct. A nested list must become rows before it can be modelled, because a model cannot aggregate a cell that holds a list. In this case: Converting the XML elements into a table of rows makes each result addressable.

### Question 24 — D

Answer: Append the queries into one table. Appending stacks rows of the same shape. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: Appending stacks rows of the same shape.
- **B:** Incorrect for this question. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. Why the correct answer wins: Appending stacks rows of the same shape.
- **C:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: Appending stacks rows of the same shape.
- **D:** Correct. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. In this case: Appending stacks rows of the same shape.

### Question 25 — B, C

Answers: Keep the steps foldable so the source does the work; Stage the raw query and build a separate clean query on it. Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. Staging separates extraction from transformation, which makes each layer easier to test and reuse. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A native query reduces what is transferred, but it can break folding for later steps and must be maintained as the schema changes. Why the correct answer wins: Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work.
- **B:** Correct. Staging separates extraction from transformation, which makes each layer easier to test and reuse. In this case: Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work.
- **C:** Correct. Query folding pushes transformations back to the source, which is faster and lets incremental refresh work. In this case: Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work.
- **D:** Incorrect for this question. Disabling load keeps a working query out of the model, which prevents unused tables from inflating the dataset. Why the correct answer wins: Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work.
- **E:** Incorrect for this question. A duplicate copies the full step chain, so a change in one copy does not affect the other but the work is repeated. Why the correct answer wins: Staging separates extraction from transformation, and keeping steps foldable keeps the source doing the work.

### Question 26 — D, E

Answers: Hide technical columns from the report view; Set the table and column properties, including hidden keys and format strings. Hiding the identifier removes it from the field list, and format strings fix how dates and values display. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Hiding the identifier removes it from the field list, and format strings fix how dates and values display.
- **B:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Hiding the identifier removes it from the field list, and format strings fix how dates and values display.
- **C:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: Hiding the identifier removes it from the field list, and format strings fix how dates and values display.
- **D:** Correct. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. In this case: Hiding the identifier removes it from the field list, and format strings fix how dates and values display.
- **E:** Correct. Hiding keys and helper columns stops report authors using an ID as a label and keeps the field list readable. In this case: Hiding the identifier removes it from the field list, and format strings fix how dates and values display.

### Question 27 — C

Answer: Define the grain → separate facts from dimensions → add surrogate keys → relate dimension to fact. The grain comes first, and separating descriptive attributes is what makes the star work. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A single wide table cannot be filtered cleanly by dimension and pushes duplication into every row. Why the correct answer wins: The grain comes first, and separating descriptive attributes is what makes the star work.
- **B:** Incorrect for this question. Relationships built before the grain is agreed will be wrong and must be rebuilt. Why the correct answer wins: The grain comes first, and separating descriptive attributes is what makes the star work.
- **C:** Correct. The grain decides what a row means, and separating descriptive attributes is what makes a star schema work. In this case: The grain comes first, and separating descriptive attributes is what makes the star work.
- **D:** Incorrect for this question. A dimension per column produces a hub of one-column tables and makes the model unmaintainable. Why the correct answer wins: The grain comes first, and separating descriptive attributes is what makes the star work.

### Question 28 — D

Answer: Flatten the lookup attributes into a single dimension. Flattening the payer attributes into the patient dimension removes the hop. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Why the correct answer wins: Flattening the payer attributes into the patient dimension removes the hop.
- **B:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: Flattening the payer attributes into the patient dimension removes the hop.
- **C:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: Flattening the payer attributes into the patient dimension removes the hop.
- **D:** Correct. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. In this case: Flattening the payer attributes into the patient dimension removes the hop.

### Question 29 — C

Answer: Inactive relationship activated with USERELATIONSHIP. Only one relationship can be active, so the second stays inactive until a measure activates it. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: Only one relationship can be active, so the second stays inactive until a measure activates it.
- **B:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: Only one relationship can be active, so the second stays inactive until a measure activates it.
- **C:** Correct. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. In this case: Only one relationship can be active, so the second stays inactive until a measure activates it.
- **D:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Only one relationship can be active, so the second stays inactive until a measure activates it.

### Question 30 — A, D

Answers: Single-direction filter from dimension to fact; One-to-many relationship from the dimension to the fact. Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **B:** Incorrect for this question. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **C:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **D:** Correct. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. In this case: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.
- **E:** Incorrect for this question. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Why the correct answer wins: Dimension-to-fact one-to-many is the standard shape, and single-direction filtering keeps it predictable.

### Question 31 — C

Answer: Set the cross-filter direction on the relationship. Cross-filter direction decides whether the fact can filter the dimension. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. An inactive relationship exists but does not filter until a measure activates it, which is how one fact supports several dates. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **B:** Incorrect for this question. Bi-directional filtering lets a fact filter a dimension, which is occasionally required but can create ambiguity and slow queries. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.
- **C:** Correct. Cross-filter direction decides which table filters which, and changing it is the usual fix for a filter that does not reach the visual. In this case: Cross-filter direction decides whether the fact can filter the dimension.
- **D:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: Cross-filter direction decides whether the fact can filter the dimension.

### Question 32 — D

Answer: Create a dedicated date table marked as the date table. A contiguous date table supplies every date so accumulation does not skip gaps. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **B:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **C:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: A contiguous date table supplies every date so accumulation does not skip gaps.
- **D:** Correct. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. In this case: A contiguous date table supplies every date so accumulation does not skip gaps.

### Question 33 — A

Answer: Create one date table and role-play it through several relationships. One date table related three times through role-playing dimensions avoids three near-identical tables. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. In this case: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **B:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **C:** Incorrect for this question. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.
- **D:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: One date table related three times through role-playing dimensions avoids three near-identical tables.

### Question 34 — D

Answer: Mark the table as a date table. Marking the table as the date table removes the ambiguity. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A marked date table with contiguous dates is what time intelligence functions require and what slicers should use. Why the correct answer wins: Marking the table as the date table removes the ambiguity.
- **B:** Incorrect for this question. Fiscal columns let time intelligence follow the organization's year instead of the calendar year. Why the correct answer wins: Marking the table as the date table removes the ambiguity.
- **C:** Incorrect for this question. Role-playing reuses a single date dimension for order, ship, and due dates, which avoids three near-identical date tables. Why the correct answer wins: Marking the table as the date table removes the ambiguity.
- **D:** Correct. Marking the date table tells the engine which table supplies the date hierarchy, which removes ambiguity when several date columns exist. In this case: Marking the table as the date table removes the ambiguity.

### Question 35 — A

Answer: Create a contiguous date table → mark it as the date table → relate it to the fact dates → build time intelligence on it. Marking and relating the date table is what makes the measures obey the date slicer. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. Local study-map skill 2.3 (Date Tables and Role-Playing Dimensions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. Time intelligence needs a marked, contiguous table, and relating it properly is what makes the measures respond to slicers. In this case: Marking and relating the date table is what makes the measures obey the date slicer.
- **B:** Incorrect for this question. Several date tables multiply relationships and make every time measure ambiguous. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **C:** Incorrect for this question. An unrelated date table filters nothing, so the slicer appears to work while the visuals ignore it. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.
- **D:** Incorrect for this question. A fact date column has gaps, so year-to-date silently skips missing days and the slicer shows no clean hierarchy. Why the correct answer wins: Marking and relating the date table is what makes the measures obey the date slicer.

### Question 36 — A

Answer: Create a measure for the aggregation. A measure is evaluated in the filter context the visual supplies, so it responds to slicers and adds nothing to the stored model. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. In this case: A measure is evaluated in the filter context the visual supplies, so it responds to slicers and adds nothing to the stored model.
- **B:** Incorrect for this question. Filter context is what the visual and its slicers impose on a measure at evaluation time, and it explains most unexpected totals. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies, so it responds to slicers and adds nothing to the stored model.
- **C:** Incorrect for this question. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies, so it responds to slicers and adds nothing to the stored model.
- **D:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A measure is evaluated in the filter context the visual supplies, so it responds to slicers and adds nothing to the stored model.

### Question 37 — C

Answer: Create a calculated column. A calculated column is computed row by row and stored, which is what a slicer field needs. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: A calculated column is computed row by row and stored, which is what a slicer field needs.
- **B:** Incorrect for this question. A calculated table materializes at refresh, which suits a small derived table such as a parameter or a bridge. Why the correct answer wins: A calculated column is computed row by row and stored, which is what a slicer field needs.
- **C:** Correct. A calculated column is computed row by row at refresh and stored, which suits a value needed for slicing or a relationship. In this case: A calculated column is computed row by row and stored, which is what a slicer field needs.
- **D:** Incorrect for this question. Row context exists inside a calculated column or an iterator function and is the reason RELATED is needed to reach another table. Why the correct answer wins: A calculated column is computed row by row and stored, which is what a slicer field needs.

### Question 38 — D, E

Answers: Use DIVIDE instead of the division operator; Use DISTINCT COUNT for unique entities. DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. Distinct count answers how many unique customers or orders, which a plain count would overstate. Local study-map skill 2.4 (Measures, Calculated Columns, and Filter Context), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. An iterator evaluates the expression per row and then aggregates, which is required when the value to sum is not a stored column. Why the correct answer wins: DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question.
- **B:** Incorrect for this question. Iterators such as SUMX and AVERAGEX apply a calculation per row, which is the difference between an average of ratios and a ratio of totals. Why the correct answer wins: DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question.
- **C:** Incorrect for this question. A measure is evaluated in the filter context of the visual, so it responds to slicers automatically and does not inflate the model. Why the correct answer wins: DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question.
- **D:** Correct. DIVIDE returns blank instead of an error when the denominator is zero, which keeps ratio visuals clean. In this case: DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question.
- **E:** Correct. Distinct count answers how many unique customers or orders, which a plain count would overstate. In this case: DIVIDE avoids a division error and DISTINCT COUNT answers the unique-patient question.

### Question 39 — C

Answer: Wrap the aggregation in CALCULATE to change the filter context. CALCULATE evaluates the expression under modified filters, which is how a share is built. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: CALCULATE evaluates the expression under modified filters, which is how a share is built.
- **B:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: CALCULATE evaluates the expression under modified filters, which is how a share is built.
- **C:** Correct. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. In this case: CALCULATE evaluates the expression under modified filters, which is how a share is built.
- **D:** Incorrect for this question. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Why the correct answer wins: CALCULATE evaluates the expression under modified filters, which is how a share is built.

### Question 40 — A

Answer: Use ALLSELECTED to respect the slicer but ignore the visual. ALLSELECTED respects the reader's selection while removing the visual's own grouping. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. In this case: ALLSELECTED respects the reader's selection while removing the visual's own grouping.
- **B:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's own grouping.
- **C:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's own grouping.
- **D:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: ALLSELECTED respects the reader's selection while removing the visual's own grouping.

### Question 41 — C

Answer: Store intermediate results in VAR and RETURN. Variables compute the expression once and make the measure readable. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **B:** Incorrect for this question. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Why the correct answer wins: Variables compute the expression once and make the measure readable.
- **C:** Correct. Variables compute once, make a measure readable, and prevent a filter modifier from being applied differently in two places. In this case: Variables compute the expression once and make the measure readable.
- **D:** Incorrect for this question. CALCULATE evaluates an expression under modified filters, which is how ratios, shares, and prior-period values are built. Why the correct answer wins: Variables compute the expression once and make the measure readable.

### Question 42 — D

Answer: Add KEEPFILTERS to intersect rather than replace the filter. KEEPFILTERS intersects the new filter with the existing one. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. Local study-map skill 2.5 (CALCULATE and Filter Modifiers), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. ALL clears filters from a table, which is the basis for share-of-total and denominator calculations. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one.
- **B:** Incorrect for this question. ALLSELECTED computes a share within the user's chosen selection rather than the whole table, which is usually what a percent-of-total wants. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one.
- **C:** Incorrect for this question. Removing a filter lets a measure compute a total or share regardless of the current slicer selection. Why the correct answer wins: KEEPFILTERS intersects the new filter with the existing one.
- **D:** Correct. KEEPFILTERS keeps the existing filter and intersects it with the new one, which prevents a measure from reporting values outside the current selection. In this case: KEEPFILTERS intersects the new filter with the existing one.

### Question 43 — A

Answer: Use LASTNONBLANK when the balance is only recorded on some dates. LASTNONBLANK finds the most recent date that actually carries a value. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. LASTNONBLANK finds the most recent date that actually has a value, which handles accounts that are not updated daily. In this case: LASTNONBLANK finds the most recent date that actually carries a value.
- **B:** Incorrect for this question. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Why the correct answer wins: LASTNONBLANK finds the most recent date that actually carries a value.
- **C:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: LASTNONBLANK finds the most recent date that actually carries a value.
- **D:** Incorrect for this question. Balances such as inventory should not be summed across time, so the measure takes the value at the last date in the period. Why the correct answer wins: LASTNONBLANK finds the most recent date that actually carries a value.

### Question 44 — A

Answer: Use AVERAGEX over a rolling date window. A rolling average over a trailing window smooths the series without hiding the current value. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A rolling window averages a trailing number of periods, which smooths a noisy series without hiding the current value. In this case: A rolling average over a trailing window smooths the series without hiding the current value.
- **B:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: A rolling average over a trailing window smooths the series without hiding the current value.
- **C:** Incorrect for this question. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Why the correct answer wins: A rolling average over a trailing window smooths the series without hiding the current value.
- **D:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: A rolling average over a trailing window smooths the series without hiding the current value.

### Question 45 — C

Answer: Use DATESINPERIOD for a windowed calculation. DATESINPERIOD returns a range ending at the selected date. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. Local study-map skill 2.6 (Time Intelligence and Semi-Additive Measures), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Year-to-date functions accumulate from the start of the year defined by the marked date table. Why the correct answer wins: DATESINPERIOD returns a range ending at the selected date.
- **B:** Incorrect for this question. The comparable-period functions shift the current selection back a year, which is how year-over-year is computed correctly. Why the correct answer wins: DATESINPERIOD returns a range ending at the selected date.
- **C:** Correct. DATESINPERIOD returns a range ending at the current date, which is the basis for rolling totals. In this case: DATESINPERIOD returns a range ending at the selected date.
- **D:** Incorrect for this question. Time intelligence only works reliably when the date table is contiguous and marked, so the measure must reference it rather than a fact date column. Why the correct answer wins: DATESINPERIOD returns a range ending at the selected date.

### Question 46 — A

Answer: Create a calculation group for the time-intelligence variants. A calculation group applies the same variants to every measure instead of triplicating them. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. In this case: A calculation group applies the same variants to every measure instead of triplicating them.
- **B:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A calculation group applies the same variants to every measure instead of triplicating them.
- **C:** Incorrect for this question. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Why the correct answer wins: A calculation group applies the same variants to every measure instead of triplicating them.
- **D:** Incorrect for this question. A field parameter lets one visual switch between measures or dimensions without duplicating pages. Why the correct answer wins: A calculation group applies the same variants to every measure instead of triplicating them.

### Question 47 — A, C

Answers: Create a field parameter so the author can switch the measure or axis; Create a numeric range parameter for scenario analysis. A field parameter switches the measure in place, and a numeric range parameter drives the assumption. A field parameter lets one visual switch between measures or dimensions without duplicating pages. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A what-if parameter feeds a measure that applies the selected value, which lets users test assumptions in the report. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **B:** Incorrect for this question. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **C:** Correct. A field parameter lets one visual switch between measures or dimensions without duplicating pages. In this case: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **D:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.
- **E:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A field parameter switches the measure in place, and a numeric range parameter drives the assumption.

### Question 48 — A

Answer: Use PERCENTILE.INC for a distribution boundary. A percentile returns the boundary value, which describes the tail rather than the average. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. Local study-map skill 2.7 (Statistical Functions, Quick Measures, and Calculation Groups), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. A percentile returns the value below which a share of observations fall, which describes a distribution rather than an average. In this case: A percentile returns the boundary value, which describes the tail rather than the average.
- **B:** Incorrect for this question. Descriptive statistics show the shape of the data, which an average alone hides. Why the correct answer wins: A percentile returns the boundary value, which describes the tail rather than the average.
- **C:** Incorrect for this question. A quick measure generates the DAX for a common pattern such as a running total, which is faster and less error-prone than hand-writing it. Why the correct answer wins: A percentile returns the boundary value, which describes the tail rather than the average.
- **D:** Incorrect for this question. A calculation group applies the same set of variants to every measure, which replaces dozens of near-identical measures. Why the correct answer wins: A percentile returns the boundary value, which describes the tail rather than the average.

### Question 49 — A

Answer: Reduce column cardinality and width to shrink the VertiPaq store. The in-memory store compresses repeated and narrow values well, so a high-cardinality text column costs the most. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Correct. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. In this case: The in-memory store compresses repeated and narrow values well, so a high-cardinality text column costs the most.
- **B:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so a high-cardinality text column costs the most.
- **C:** Incorrect for this question. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so a high-cardinality text column costs the most.
- **D:** Incorrect for this question. Loading to the grain the report actually needs removes rows the visuals never use. Why the correct answer wins: The in-memory store compresses repeated and narrow values well, so a high-cardinality text column costs the most.

### Question 50 — C

Answer: Inspect the query plan in DAX query view. DAX query view shows the generated query and its timings. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: DAX query view shows the generated query and its timings.
- **B:** Incorrect for this question. Performance Analyzer times each visual and separates DAX, query, and rendering cost, which identifies where the delay actually is. Why the correct answer wins: DAX query view shows the generated query and its timings.
- **C:** Correct. DAX query view shows the generated query and its timings, which is how a slow measure is isolated from a slow visual. In this case: DAX query view shows the generated query and its timings.
- **D:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: DAX query view shows the generated query and its timings.

### Question 51 — D

Answer: A matrix visual with row and column groups. A matrix supports nested rows and columns with subtotals. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **B:** Incorrect for this question. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **C:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A matrix supports nested rows and columns with subtotals.
- **D:** Correct. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. In this case: A matrix supports nested rows and columns with subtotals.

### Question 52 — A

Answer: A scatter chart. A scatter plot shows the relationship between two numeric measures. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A scatter plot shows the relationship between two numeric measures and reveals clusters and outliers. In this case: A scatter plot shows the relationship between two numeric measures.
- **B:** Incorrect for this question. A line chart shows a trend over a continuous axis, which is what time series need. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.
- **C:** Incorrect for this question. A pie chart shows part-to-whole for a few categories; beyond about five slices the comparison becomes unreadable. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.
- **D:** Incorrect for this question. Bar and column charts compare a measure across categories, which is the right default for ranking or comparison. Why the correct answer wins: A scatter plot shows the relationship between two numeric measures.

### Question 53 — C, D

Answers: A line chart with a date axis; A funnel chart. A line chart shows the trend, and a funnel shows stage attrition. A line chart shows a trend over a continuous axis, which is what time series need. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A line chart shows the trend, and a funnel shows stage attrition.
- **B:** Incorrect for this question. A matrix supports nested rows and columns with subtotals, which is the report equivalent of a pivot table. Why the correct answer wins: A line chart shows the trend, and a funnel shows stage attrition.
- **C:** Correct. A funnel shows sequential stage attrition, which suits a sales or process pipeline. In this case: A line chart shows the trend, and a funnel shows stage attrition.
- **D:** Correct. A line chart shows a trend over a continuous axis, which is what time series need. In this case: A line chart shows the trend, and a funnel shows stage attrition.
- **E:** Incorrect for this question. A KPI visual states progress against a defined target, which a plain card cannot show. Why the correct answer wins: A line chart shows the trend, and a funnel shows stage attrition.

### Question 54 — A

Answer: A slicer on the report page. A slicer puts the control on the canvas. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. In this case: A slicer puts the control on the canvas.
- **B:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: A slicer puts the control on the canvas.
- **C:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: A slicer puts the control on the canvas.
- **D:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: A slicer puts the control on the canvas.

### Question 55 — C

Answer: Edit the interactions so the visual does not filter the others. Interaction settings decide whether a selection filters, highlights, or does nothing. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **B:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **C:** Correct. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. In this case: Interaction settings decide whether a selection filters, highlights, or does nothing.
- **D:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Interaction settings decide whether a selection filters, highlights, or does nothing.

### Question 56 — D

Answer: Set the filter pane scope by page, report, or visual. Filter scope decides whether the filter applies to a visual, a page, or the whole report. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Filter scope decides whether the filter applies to a visual, a page, or the whole report.
- **B:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Filter scope decides whether the filter applies to a visual, a page, or the whole report.
- **C:** Incorrect for this question. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Why the correct answer wins: Filter scope decides whether the filter applies to a visual, a page, or the whole report.
- **D:** Correct. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. In this case: Filter scope decides whether the filter applies to a visual, a page, or the whole report.

### Question 57 — A

Answer: Capture the view in a bookmark. A bookmark stores the filter and visibility state of each view. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. In this case: A bookmark stores the filter and visibility state of each view.
- **B:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: A bookmark stores the filter and visibility state of each view.
- **C:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A bookmark stores the filter and visibility state of each view.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A bookmark stores the filter and visibility state of each view.

### Question 58 — C

Answer: Add buttons with actions that navigate or apply a bookmark. Buttons with bookmark actions turn a stored state into one click. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Why the correct answer wins: Buttons with bookmark actions turn a stored state into one click.
- **B:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: Buttons with bookmark actions turn a stored state into one click.
- **C:** Correct. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. In this case: Buttons with bookmark actions turn a stored state into one click.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Buttons with bookmark actions turn a stored state into one click.

### Question 59 — C

Answer: Create the views → capture each in a bookmark → add buttons → hide the visuals not in use. Bookmarks store state and buttons apply it. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A bookmark captures the state at the moment it is created, so filters set afterwards are not stored. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **B:** Incorrect for this question. Duplicating pages multiplies maintenance and the copies drift apart. Why the correct answer wins: Bookmarks store state and buttons apply it.
- **C:** Correct. Bookmarks store state and buttons apply it, which is what makes a single page behave like several. In this case: Bookmarks store state and buttons apply it.
- **D:** Incorrect for this question. A button with no action is decoration and the report still has no navigation. Why the correct answer wins: Bookmarks store state and buttons apply it.

### Question 60 — A

Answer: Add a page navigator for the report. A page navigator generates navigation from the pages themselves. A page navigator generates navigation for every page automatically, which stays correct as pages are added. Local study-map skill 3.3 (Bookmarks, Buttons, and Report Navigation), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A page navigator generates navigation for every page automatically, which stays correct as pages are added. In this case: A page navigator generates navigation from the pages themselves.
- **B:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **C:** Incorrect for this question. Buttons turn a bookmark or page change into one click, which is how a report is made to feel like an application. Why the correct answer wins: A page navigator generates navigation from the pages themselves.
- **D:** Incorrect for this question. A bookmark stores the current filter, slicer, and visibility state, which is how a report offers saved views or a reset button. Why the correct answer wins: A page navigator generates navigation from the pages themselves.

### Question 61 — A

Answer: Configure a drillthrough page with the entity filter. Drillthrough passes the selected entity to a detail page through a filter. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. In this case: Drillthrough passes the selected entity to a detail page through a filter.
- **B:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **C:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.
- **D:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Drillthrough passes the selected entity to a detail page through a filter.

### Question 62 — D

Answer: Enable drill-down through the hierarchy. Drill-down moves through the hierarchy inside the same visual. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **B:** Incorrect for this question. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **C:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Drill-down moves through the hierarchy inside the same visual.
- **D:** Correct. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. In this case: Drill-down moves through the hierarchy inside the same visual.

### Question 63 — A, C

Answers: Build a custom tooltip page; Set the tooltip to a report page and size it to the hover area. A tooltip page holds the extra measures, and the report-page tooltip setting displays it. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. A report-page tooltip must be small enough to read on hover, and its filters must match the hovered data point. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **B:** Incorrect for this question. Drill-down moves from a summary level to the next level within the same visual, which keeps the context visible. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **C:** Correct. A tooltip page shows several related measures on hover, which adds context without cluttering the visual. In this case: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.
- **E:** Incorrect for this question. Drillthrough opens a detail page filtered to the selected entity, which is how a reader moves from a summary to the underlying rows. Why the correct answer wins: A tooltip page holds the extra measures, and the report-page tooltip setting displays it.

### Question 64 — A

Answer: Choose the entity field → create the drillthrough page → place the entity filter → add a back button. The drillthrough filter carries the selection, and the back button keeps the reader oriented. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. Local study-map skill 3.4 (Drillthrough, Drill-Down, and Tooltips), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. The drillthrough filter is what carries the selection, and the back button is what keeps the reader oriented. In this case: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **B:** Incorrect for this question. Without a back button the reader is stranded on the detail page and loses the summary context. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **C:** Incorrect for this question. Too many fields on one visual makes the click target ambiguous and the drill result unpredictable. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.
- **D:** Incorrect for this question. A page without the drillthrough filter does not carry the selected entity, so the detail is not about what was clicked. Why the correct answer wins: The drillthrough filter carries the selection, and the back button keeps the reader oriented.

### Question 65 — B

Answer: Provide alt text for each meaningful visual. Alt text describes each visual for a screen reader. Alt text describes the visual for a screen reader, which is required for an accessible report. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **B:** Correct. Alt text describes the visual for a screen reader, which is required for an accessible report. In this case: Alt text describes each visual for a screen reader.
- **C:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Alt text describes each visual for a screen reader.
- **D:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Alt text describes each visual for a screen reader.

### Question 66 — B

Answer: Set a logical tab order for the interactive elements. Tab order decides the keyboard sequence through the interactive elements. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Tab order decides the keyboard sequence through the interactive elements.
- **B:** Correct. Tab order decides the keyboard sequence, which is how a keyboard user reaches the controls in a sensible order. In this case: Tab order decides the keyboard sequence through the interactive elements.
- **C:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Tab order decides the keyboard sequence through the interactive elements.
- **D:** Incorrect for this question. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Why the correct answer wins: Tab order decides the keyboard sequence through the interactive elements.

### Question 67 — C

Answer: Configure the export and download settings for the report. Export settings decide whether readers can take data out, which is a governance decision. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. Local study-map skill 3.5 (Accessibility, Mobile Layout, Personalization, and Export), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. The mobile layout decides what a phone shows first, which is not the same as a squeezed desktop canvas. Why the correct answer wins: Export settings decide whether readers can take data out, which is a governance decision.
- **B:** Incorrect for this question. Alt text describes the visual for a screen reader, which is required for an accessible report. Why the correct answer wins: Export settings decide whether readers can take data out, which is a governance decision.
- **C:** Correct. Export settings decide whether readers can take data out, which is a governance decision as much as a convenience. In this case: Export settings decide whether readers can take data out, which is a governance decision.
- **D:** Incorrect for this question. Personalization lets a reader change visual type or fields without edit rights, while the author keeps the published default. Why the correct answer wins: Export settings decide whether readers can take data out, which is a governance decision.

### Question 68 — D

Answer: Apply a report theme JSON. A theme applies a consistent palette across the report. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: A theme applies a consistent palette across the report.
- **B:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: A theme applies a consistent palette across the report.
- **C:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: A theme applies a consistent palette across the report.
- **D:** Correct. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. In this case: A theme applies a consistent palette across the report.

### Question 69 — D

Answer: Turn on and format data labels. Data labels put the value next to the mark. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. Why the correct answer wins: Data labels put the value next to the mark.
- **B:** Incorrect for this question. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Why the correct answer wins: Data labels put the value next to the mark.
- **C:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Data labels put the value next to the mark.
- **D:** Correct. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. In this case: Data labels put the value next to the mark.

### Question 70 — B, C

Answers: Apply conditional formatting driven by a measure; Set the axis range and units explicitly. Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. Local study-map skill 3.6 (Sorting, Conditional Formatting, Themes, and the Selection Pane), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A theme applies a consistent palette and formatting across every visual, which is faster and more consistent than styling each visual. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **B:** Correct. Conditional formatting encodes a value as colour or an icon, which lets a reader scan exceptions instead of reading every number. In this case: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **C:** Correct. A fixed axis prevents a small change from looking dramatic, which is an integrity issue rather than a cosmetic one. In this case: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **D:** Incorrect for this question. The Selection pane controls visibility and z-order, which is how a report builds layered or swapped views. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.
- **E:** Incorrect for this question. Data labels put the value next to the mark, which removes the need to read an axis for a small number of categories. Why the correct answer wins: Conditional formatting highlights the exception, and an explicit axis range prevents exaggeration.

### Question 71 — A

Answer: Use the Analyze feature to explain a change. The Analyze feature decomposes the change across dimensions to show what contributed. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. The Analyze feature decomposes a value into the dimensions that contribute most to the change, which answers why a number moved. In this case: The Analyze feature decomposes the change across dimensions to show what contributed.
- **B:** Incorrect for this question. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Why the correct answer wins: The Analyze feature decomposes the change across dimensions to show what contributed.
- **C:** Incorrect for this question. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Why the correct answer wins: The Analyze feature decomposes the change across dimensions to show what contributed.
- **D:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: The Analyze feature decomposes the change across dimensions to show what contributed.

### Question 72 — B

Answer: Use the outlier detection feature on the visual. Outlier detection finds points that sit far from the pattern. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Error bars show the spread around a value, which stops a point estimate being read as certainty. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.
- **B:** Correct. Outlier detection finds points that sit far from the pattern, which is often the first sign of a data or process problem. In this case: Outlier detection finds points that sit far from the pattern.
- **C:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.
- **D:** Incorrect for this question. A reference line gives the reader a comparison without a second visual, which turns a trend into a performance judgement. Why the correct answer wins: Outlier detection finds points that sit far from the pattern.

### Question 73 — D

Answer: Use clustering to find segments in the data. Clustering groups rows that behave similarly, which surfaces segments nobody defined in advance. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. Local study-map skill 3.7 (Analyze Features, Grouping, Binning, and Forecasting), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Forecasting extends the series statistically and shows a confidence band, which is only meaningful on a stable, seasonally understood series. Why the correct answer wins: Clustering groups rows that behave similarly, which surfaces segments nobody defined in advance.
- **B:** Incorrect for this question. Binning turns a continuous value into ranges, which is how a distribution becomes readable. Why the correct answer wins: Clustering groups rows that behave similarly, which surfaces segments nobody defined in advance.
- **C:** Incorrect for this question. Grouping combines members into meaningful buckets, which reduces clutter and matches how the business talks. Why the correct answer wins: Clustering groups rows that behave similarly, which surfaces segments nobody defined in advance.
- **D:** Correct. Clustering groups similar rows statistically, which surfaces segments that were not defined in advance. In this case: Clustering groups rows that behave similarly, which surfaces segments nobody defined in advance.

### Question 74 — C

Answer: Use the Decomposition Tree visual. A decomposition tree supports open-ended drill paths across dimensions. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: A decomposition tree supports open-ended drill paths across dimensions.
- **B:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: A decomposition tree supports open-ended drill paths across dimensions.
- **C:** Correct. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. In this case: A decomposition tree supports open-ended drill paths across dimensions.
- **D:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: A decomposition tree supports open-ended drill paths across dimensions.

### Question 75 — A

Answer: Use Copilot to suggest a report page. Copilot can draft a page from a prompt, which the author then reviews. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. In this case: Copilot can draft a page from a prompt, which the author then reviews.
- **B:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.
- **C:** Incorrect for this question. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.
- **D:** Incorrect for this question. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Why the correct answer wins: Copilot can draft a page from a prompt, which the author then reviews.

### Question 76 — B

Answer: Create a workspace for the team that owns the content. A workspace is the collaboration and permission boundary for the team. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **B:** Correct. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. In this case: A workspace is the collaboration and permission boundary for the team.
- **C:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.
- **D:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: A workspace is the collaboration and permission boundary for the team.

### Question 77 — C

Answer: Workspace Admin role. Admins manage the workspace, its members, and its settings. Admins manage the workspace, its members, and its settings, which is more than publishing content. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Contributors can publish and edit content, which is the role for authors who should not manage membership. Why the correct answer wins: Admins manage the workspace, its members, and its settings.
- **B:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Admins manage the workspace, its members, and its settings.
- **C:** Correct. Admins manage the workspace, its members, and its settings, which is more than publishing content. In this case: Admins manage the workspace, its members, and its settings.
- **D:** Incorrect for this question. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Why the correct answer wins: Admins manage the workspace, its members, and its settings.

### Question 78 — D

Answer: Publish an app from the workspace. An app gives consumers a curated experience with its own audience list. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.
- **B:** Incorrect for this question. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.
- **C:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: An app gives consumers a curated experience with its own audience list.
- **D:** Correct. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. In this case: An app gives consumers a curated experience with its own audience list.

### Question 79 — C

Answer: Choose the distribution method that matches the audience. The distribution method decides reach, control, and how the audience authenticates. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Why the correct answer wins: The distribution method decides reach, control, and how the audience authenticates.
- **B:** Incorrect for this question. Consumers see the published app, so workspace edits stay invisible until the app is updated. Why the correct answer wins: The distribution method decides reach, control, and how the audience authenticates.
- **C:** Correct. App, shared link, Teams, or embedded all grant different levels of control, so the choice is a governance decision. In this case: The distribution method decides reach, control, and how the audience authenticates.
- **D:** Incorrect for this question. Audiences let one app show different content to different groups, which avoids maintaining several near-identical apps. Why the correct answer wins: The distribution method decides reach, control, and how the audience authenticates.

### Question 80 — B

Answer: Build in the workspace → curate the app pages → assign audiences → publish and update the app. Audiences control who sees what, and consumers see changes only when the app is updated. Audiences control who sees what, and consumers only see changes when the app is updated. Local study-map skill 4.2 (Apps and Distribution Methods), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Direct workspace access exposes everything in the workspace and cannot be curated per audience. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **B:** Correct. Audiences control who sees what, and consumers only see changes when the app is updated. In this case: Audiences control who sees what, and consumers see changes only when the app is updated.
- **C:** Incorrect for this question. Publishing an unfinished report sets expectations you cannot meet and consumers see the version you last shipped. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.
- **D:** Incorrect for this question. An app per person is unmaintainable and defeats the point of audiences. Why the correct answer wins: Audiences control who sees what, and consumers see changes only when the app is updated.

### Question 81 — B

Answer: Pin the visual to a dashboard tile. Pinning copies the visual to a dashboard tile and keeps the link to the report. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link to the report.
- **B:** Correct. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. In this case: Pinning copies the visual to a dashboard tile and keeps the link to the report.
- **C:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link to the report.
- **D:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: Pinning copies the visual to a dashboard tile and keeps the link to the report.

### Question 82 — D

Answer: Set the alert threshold on the pinned card tile. Alerts are configured per tile, so the tile must expose a single value. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.
- **B:** Incorrect for this question. Pinning copies the visual to the dashboard, and the tile stays linked to the underlying report for drill-through. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.
- **C:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: Alerts are configured per tile, so the tile must expose a single value.
- **D:** Correct. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. In this case: Alerts are configured per tile, so the tile must expose a single value.

### Question 83 — B

Answer: Virtual network data gateway. A virtual network gateway connects the service to sources inside the network without a server install. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. Why the correct answer wins: A virtual network gateway connects the service to sources inside the network without a server install.
- **B:** Correct. A VNet gateway connects the service to sources inside an Azure virtual network without installing software on a server. In this case: A virtual network gateway connects the service to sources inside the network without a server install.
- **C:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: A virtual network gateway connects the service to sources inside the network without a server install.
- **D:** Incorrect for this question. A personal gateway serves one author and cannot be shared, which makes it unsuitable for team-owned refresh. Why the correct answer wins: A virtual network gateway connects the service to sources inside the network without a server install.

### Question 84 — D

Answer: Add RangeStart and RangeEnd parameters → filter the source query → configure the refresh policy → publish and refresh. Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A later policy does not rewrite history that was never partitioned, so the load stays slow. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **B:** Incorrect for this question. The policy is applied when the model is published and refreshed, so assuming it worked leaves a full load in place. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **C:** Incorrect for this question. A policy without the parameter filter has nothing to partition and falls back to loading everything. Why the correct answer wins: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.
- **D:** Correct. Incremental refresh only partitions the query when the parameters filter it, and the policy must exist in the published model. In this case: Incremental refresh only partitions the query when the parameters filter it, and the policy must reach the published model.

### Question 85 — B

Answer: Test the role with View as role in the service. View as role shows the report exactly as a role member sees it. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **B:** Correct. View as role shows the report exactly as a member of the role sees it, which is how a security mistake is caught before release. In this case: View as role shows the report exactly as a role member sees it.
- **C:** Incorrect for this question. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Why the correct answer wins: View as role shows the report exactly as a role member sees it.
- **D:** Incorrect for this question. A dynamic rule matches the signed-in user to a mapping table, which avoids maintaining one role per person. Why the correct answer wins: View as role shows the report exactly as a role member sees it.

### Question 86 — B

Answer: Add the security group to the role membership. Adding a security group aligns membership with the directory and reduces drift. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. Local study-map skill 4.5 (Row-Level Security), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. The filter compares the model column to the identity the service passes, which is the basis of dynamic security. Why the correct answer wins: Adding a security group aligns membership with the directory and reduces drift.
- **B:** Correct. Adding a group instead of individuals keeps role membership aligned with the directory and reduces drift. In this case: Adding a security group aligns membership with the directory and reduces drift.
- **C:** Incorrect for this question. A static role is simple to reason about but must be maintained every time the org chart changes. Why the correct answer wins: Adding a security group aligns membership with the directory and reduces drift.
- **D:** Incorrect for this question. An RLS role filters the model per user at query time, which is how one report serves many regions without duplication. Why the correct answer wins: Adding a security group aligns membership with the directory and reduces drift.

### Question 87 — D

Answer: Promote the content as endorsed. Promotion signals the content is ready for reuse by the team. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A sensitivity label travels with the exported file, which is how protection survives beyond the workspace. Why the correct answer wins: Promotion signals the content is ready for reuse by the team.
- **B:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: Promotion signals the content is ready for reuse by the team.
- **C:** Incorrect for this question. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Why the correct answer wins: Promotion signals the content is ready for reuse by the team.
- **D:** Correct. Promotion signals the content is ready for reuse by the team, while certification asserts organization-wide trust. In this case: Promotion signals the content is ready for reuse by the team.

### Question 88 — B

Answer: Grant item-level access to the specific report. Item-level sharing grants one item without workspace membership. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. Local study-map skill 4.6 (Sensitivity Labels, Endorsement, and Item Access), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Certification requires a designated reviewer, which is how a single trusted model becomes the organization standard. Why the correct answer wins: Item-level sharing grants one item without workspace membership.
- **B:** Correct. Item-level sharing grants one item without workspace membership, which limits what the recipient can discover. In this case: Item-level sharing grants one item without workspace membership.
- **C:** Incorrect for this question. A workspace is the collaboration and permission boundary, so content shared by one team belongs in one workspace. Why the correct answer wins: Item-level sharing grants one item without workspace membership.
- **D:** Incorrect for this question. Build lets another author create reports on the model without editing it, which is how reuse is enabled safely. Why the correct answer wins: Item-level sharing grants one item without workspace membership.

### Question 89 — B

Answer: A waterfall chart. A waterfall explains movement from a starting value to an ending value. A waterfall explains how a starting value moves to an ending value through additions and subtractions. Local study-map skill 3.1 (Selecting and Formatting Visuals), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. A funnel shows sequential stage attrition, which suits a sales or process pipeline. Why the correct answer wins: A waterfall explains movement from a starting value to an ending value.
- **B:** Correct. A waterfall explains how a starting value moves to an ending value through additions and subtractions. In this case: A waterfall explains movement from a starting value to an ending value.
- **C:** Incorrect for this question. A gauge shows one value against a target range, which is compact but wastes space relative to a KPI or card. Why the correct answer wins: A waterfall explains movement from a starting value to an ending value.
- **D:** Incorrect for this question. A treemap shows hierarchical part-to-whole through area, which suits many categories when exact comparison is secondary. Why the correct answer wins: A waterfall explains movement from a starting value to an ending value.

### Question 90 — D

Answer: Sync the slicer across the pages that share the same filter. Syncing the slicer keeps one selection consistent across pages. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. Local study-map skill 3.2 (Slicers, Filters, and Visual Interactions), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Incorrect for this question. Filter scope decides who the filter affects, and putting it at the wrong level is a common cause of a filter that seems to be ignored. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **B:** Incorrect for this question. Interaction settings decide whether a selection filters, highlights, or does nothing, which is how an executive summary stays stable. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **C:** Incorrect for this question. A slicer gives the reader an obvious control over the filter, which is clearer than expecting them to use the filter pane. Why the correct answer wins: Syncing the slicer keeps one selection consistent across pages.
- **D:** Correct. Syncing keeps a selection consistent as the reader moves between pages, which prevents contradictory views. In this case: Syncing the slicer keeps one selection consistent across pages.

### Question 91 — A, B

Answers: Use the Key Influencers visual; Use Q&A to answer a natural-language question. Key Influencers ranks associated factors, and Q&A answers a typed question with a visual. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. Local study-map skill 3.8 (AI Visuals, Anomaly Detection, Q&A, and Copilot), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI report visuals and analytics documentation: https://learn.microsoft.com/en-us/power-bi/visuals/

- **A:** Correct. Q&A maps a typed question to the model and returns a visual, which is fast for ad hoc questions if the model is well named. In this case: Key Influencers ranks associated factors, and Q&A answers a typed question with a visual.
- **B:** Correct. Key Influencers ranks the factors associated with a metric, which is explanatory rather than causal. In this case: Key Influencers ranks associated factors, and Q&A answers a typed question with a visual.
- **C:** Incorrect for this question. A decomposition tree lets the reader drill into any dimension in any order, which suits open-ended root-cause work. Why the correct answer wins: Key Influencers ranks associated factors, and Q&A answers a typed question with a visual.
- **D:** Incorrect for this question. Copilot can draft a page from a prompt, which is a starting point that still needs an author to check the fields and layout. Why the correct answer wins: Key Influencers ranks associated factors, and Q&A answers a typed question with a visual.
- **E:** Incorrect for this question. A narrative visual summarizes the page in text, which helps a reader who wants the story rather than the chart. Why the correct answer wins: Key Influencers ranks associated factors, and Q&A answers a typed question with a visual.

### Question 92 — B

Answer: Build a star schema with a fact table and conformed dimensions. A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. Local study-map skill 2.1 (Designing a Star Schema and Table Properties), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Snowflaking splits a dimension into related tables, which reduces duplication but adds hops and slows filters. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **B:** Correct. A star schema puts measurable events in one fact table surrounded by descriptive dimensions, which is the shape the engine and DAX are optimized for. In this case: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **C:** Incorrect for this question. Flattening keeps one hop between fact and filter, which is simpler for report authors and faster for the engine. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.
- **D:** Incorrect for this question. Properties control how a field behaves in the report: hidden keys disappear from the field list and format strings fix how values display. Why the correct answer wins: A star schema moves descriptive attributes into dimensions and keeps keys and measures in the fact.

### Question 93 — C

Answer: Many-to-many relationship with a bridging table. The assignment bridge resolves the many-to-many and keeps the filter path explicit. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. Local study-map skill 2.2 (Relationship Cardinality and Cross-Filter Direction), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A one-to-many relationship from the unique dimension key to the repeated fact key is the standard star relationship. Why the correct answer wins: The assignment bridge resolves the many-to-many and keeps the filter path explicit.
- **B:** Incorrect for this question. One-to-one suits two tables that describe the same entity, and it is usually a sign the tables could be merged. Why the correct answer wins: The assignment bridge resolves the many-to-many and keeps the filter path explicit.
- **C:** Correct. Many-to-many is needed when neither side is unique, and a bridge table keeps the filter path explicit rather than ambiguous. In this case: The assignment bridge resolves the many-to-many and keeps the filter path explicit.
- **D:** Incorrect for this question. Single direction keeps filter flow predictable and avoids ambiguous paths that the engine has to resolve. Why the correct answer wins: The assignment bridge resolves the many-to-many and keeps the filter path explicit.

### Question 94 — D, E

Answers: Add an aggregation table for the large fact; Reduce the granularity loaded into the model. An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. Loading to the grain the report actually needs removes rows the visuals never use. Local study-map skill 2.8 (Model Performance and Granularity), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI semantic model and DAX documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. A column with almost unique values compresses badly and can dominate model size for no analytical benefit. Why the correct answer wins: An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows.
- **B:** Incorrect for this question. The in-memory store compresses repeated and narrow values well, so trimming high-cardinality text and unused columns is the main size lever. Why the correct answer wins: An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows.
- **C:** Incorrect for this question. Size work starts with what is loaded, because no DAX rewrite compensates for a model that stores data it never queries. Why the correct answer wins: An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows.
- **D:** Correct. Loading to the grain the report actually needs removes rows the visuals never use. In this case: An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows.
- **E:** Correct. A pre-aggregated table answers common summaries quickly while the detail stays available for drillthrough. In this case: An aggregation table answers common summaries quickly, and loading only the needed grain removes unused rows.

### Question 95 — C

Answer: Connect to a shared semantic model instead of importing the source again. Reusing the certified clinical model inherits one definition, its refresh, and its row-level security. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. Local study-map skill 1.1 (Connecting to Data Sources and Shared Semantic Models), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Import copies the data into the semantic model at refresh, which gives the fastest queries and the most DAX flexibility but stores the data twice and needs a refresh schedule. Why the correct answer wins: Reusing the certified clinical model inherits one definition, its refresh, and its row-level security.
- **B:** Incorrect for this question. DirectQuery sends queries to the source at report time, so the report never shows stale data but the source bears the query load and some DAX is restricted. Why the correct answer wins: Reusing the certified clinical model inherits one definition, its refresh, and its row-level security.
- **C:** Correct. Reusing the certified model keeps one definition of the metric and inherits its refresh and row-level security. In this case: Reusing the certified clinical model inherits one definition, its refresh, and its row-level security.
- **D:** Incorrect for this question. DirectLake reads Delta tables directly, which gives Import-like speed without a copy, but it requires Fabric capacity and supported Delta tables. Why the correct answer wins: Reusing the certified clinical model inherits one definition, its refresh, and its row-level security.

### Question 96 — D

Answer: Group by the key and aggregate the measures. Grouping with an aggregate produces one row per provider and month. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. Local study-map skill 1.6 (Column Data Types, Custom Columns, and Grouping), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. The summarization choice decides whether the result is a sum, count, or distinct count, and a wrong one silently changes the number. Why the correct answer wins: Grouping with an aggregate produces one row per provider and month.
- **B:** Incorrect for this question. A custom column derives a new value row by row, which suits logic that built-in transformations cannot express. Why the correct answer wins: Grouping with an aggregate produces one row per provider and month.
- **C:** Incorrect for this question. A conditional column applies explicit if-then rules, which is easier to review than a hand-written expression. Why the correct answer wins: Grouping with an aggregate produces one row per provider and month.
- **D:** Correct. Grouping reduces a transactional table to one row per key, which is the usual shape for a summary or a dimension. In this case: Grouping with an aggregate produces one row per provider and month.

### Question 97 — B, E

Answers: Merge the two queries on a matching key; Create an integer surrogate key for the relationship. A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. A single integer key is compact, stable, and avoids relationships built on text or composite columns. Local study-map skill 1.8 (Merge and Append, Reference and Duplicate, Relationship Keys), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI data preparation documentation: https://learn.microsoft.com/en-us/power-bi/transform-model/

- **A:** Incorrect for this question. Appending stacks rows with the same shape, which combines monthly extracts or regions into one table. Why the correct answer wins: A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field.
- **B:** Correct. A merge joins columns from two queries side by side using a key, which is how a lookup is added to a fact query. In this case: A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field.
- **C:** Incorrect for this question. A left outer join keeps unmatched fact rows with null lookups, which exposes missing dimension members instead of silently dropping sales. Why the correct answer wins: A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field.
- **D:** Incorrect for this question. A fuzzy merge matches near-spellings when keys differ, but the matches must be reviewed because a threshold can join the wrong records. Why the correct answer wins: A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field.
- **E:** Correct. A single integer key is compact, stable, and avoids relationships built on text or composite columns. In this case: A merge brings in the descriptive column, and a surrogate key gives the relationship one compact field.

### Question 98 — B, C

Answers: Workspace Contributor role; Workspace Viewer role. Contributors publish and edit, and viewers read without editing. Contributors can publish and edit content, which is the role for authors who should not manage membership. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. Local study-map skill 4.1 (Workspaces and Workspace Roles), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. Members can publish and edit all content and add lower-privileged users, but cannot delete the workspace. Why the correct answer wins: Contributors publish and edit, and viewers read without editing.
- **B:** Correct. Contributors can publish and edit content, which is the role for authors who should not manage membership. In this case: Contributors publish and edit, and viewers read without editing.
- **C:** Correct. Viewers can read the content but not edit it, which is the safest role for consumers who work inside the workspace. In this case: Contributors publish and edit, and viewers read without editing.
- **D:** Incorrect for this question. Admins manage the workspace, its members, and its settings, which is more than publishing content. Why the correct answer wins: Contributors publish and edit, and viewers read without editing.
- **E:** Incorrect for this question. An app gives consumers a curated, read-only experience with its own audience list, instead of direct workspace access. Why the correct answer wins: Contributors publish and edit, and viewers read without editing.

### Question 99 — A

Answer: Create a subscription for the report or dashboard. A subscription delivers a scheduled snapshot by email. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. Local study-map skill 4.3 (Dashboards, Subscriptions, and Data Alerts), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Correct. A subscription delivers a snapshot on a schedule by email, which suits readers who will not open the report themselves. In this case: A subscription delivers a scheduled snapshot by email.
- **B:** Incorrect for this question. A dashboard is a single-page canvas of pinned tiles from one or more reports, which suits monitoring rather than analysis. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **C:** Incorrect for this question. Alerts are configured per tile value with a threshold and frequency, so the tile must expose the metric as a single number. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.
- **D:** Incorrect for this question. A data alert notifies when a single value crosses a threshold, and it only works on tiles, not on report visuals. Why the correct answer wins: A subscription delivers a scheduled snapshot by email.

### Question 100 — B, C

Answers: Configure scheduled refresh on the semantic model; Update the credentials used by the refresh schedule. The schedule controls freshness, and the stored credential must be current or the refresh fails. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. Local study-map skill 4.4 (Gateways and Scheduled Refresh), mapped to the official guide: Microsoft PL-300 study guide, skills measured as of April 20, 2026 Primary reference: Power BI service administration and security documentation: https://learn.microsoft.com/en-us/power-bi/admin/

- **A:** Incorrect for this question. A gateway provides the outbound connection from the service to an on-premises source, which cloud refresh requires. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or the refresh fails.
- **B:** Correct. Scheduled refresh controls how often the imported data is updated, which is the freshness guarantee the report can make. In this case: The schedule controls freshness, and the stored credential must be current or the refresh fails.
- **C:** Correct. A scheduled refresh fails silently from the reader's point of view when the stored credential has expired. In this case: The schedule controls freshness, and the stored credential must be current or the refresh fails.
- **D:** Incorrect for this question. Incremental refresh loads only new or changed partitions, which keeps refresh time and load predictable for a large fact table. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or the refresh fails.
- **E:** Incorrect for this question. Incremental refresh requires the date parameters to filter the source query, or the policy has nothing to partition. Why the correct answer wins: The schedule controls freshness, and the stored credential must be current or the refresh fails.

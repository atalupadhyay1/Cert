# Microsoft AB-410 — Full-Length Mock Exam 4

Intelligent Applications Builder Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the maker portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A winery requirement spans a distributor portal, an allocation approval, and a forecast view. What should be decided first?

Domain: Create a foundation for intelligent applications

- A. Map each requirement to the Power Platform component that fits it
- B. Deliver every requirement as a single model-driven app
- C. Start with a custom connector and a plug-in for the first version
- D. Build a working prototype in a week and let the business react to it

### 2. A maker proposes one model-driven app for sales, warehouse, and finance. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Build a working prototype in a week and let the business react to it
- B. Start with a custom connector and a plug-in for the first version
- C. Map each requirement to the Power Platform component that fits it
- D. Deliver every requirement as a single model-driven app

### 3. An allocation approval must run the same way every time. What should be used?

Domain: Create a foundation for intelligent applications

- A. Build a custom Copilot Studio agent for every requirement
- B. Adopt the built-in agent that already covers the task
- C. Build a working prototype in a week and let the business react to it
- D. Model the process as a cloud flow with no agent at all

### 4. Sales wants a helper that answers questions about allocations. What should be evaluated first?

Domain: Create a foundation for intelligent applications

- A. Build a Power Apps component framework control
- B. Adopt the built-in agent that already covers the task
- C. Build a custom Copilot Studio agent for every requirement
- D. Model the process as a cloud flow with no agent at all

### 5. The built-in agent cannot reach the allocation data. What justifies a custom agent?

Domain: Create a foundation for intelligent applications

- A. Model the process as a cloud flow with no agent at all
- B. Write a Dataverse plug-in in C#
- C. Adopt the built-in agent that already covers the task
- D. Build a custom Copilot Studio agent for every requirement

### 6. The tasting-room team needs a custom floor-plan control. What should be built?

Domain: Create a foundation for intelligent applications

- A. Write a Dataverse plug-in in C#
- B. Ship a code-first component now and replace it with low-code later
- C. Build a Power Apps component framework control
- D. Add a JavaScript web resource to the form

### 7. A distributor portal must sit in its own governed boundary. What decides the environment?

Domain: Create a foundation for intelligent applications

- A. Build in the default environment because everyone already has access
- B. Share a single environment between development and production
- C. Use the trial environment for production after the pilot
- D. Choose the environment type that matches the data boundary and the licence

### 8. The only environment is production and the maker plans to build there. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Share a single environment between development and production
- B. Run production workloads in a sandbox environment
- C. Choose the environment type that matches the data boundary and the licence
- D. Do all building in the production environment to avoid deployment

### 9. A solution must carry a stable prefix and move as a package. Which two practices apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Import unmanaged customizations directly into production
- B. Define the solution publisher and prefix once, before the first table
- C. Package the customizations in a solution before moving them
- D. Automate export and import with an Azure DevOps pipeline
- E. Clone the environment each time instead of using a pipeline

### 10. An allocation entity has no standard equivalent. Where should it be modelled?

Domain: Create a foundation for intelligent applications

- A. Keep the records in a SharePoint list and skip Dataverse
- B. Add a choice column for the fixed set of options
- C. Extend the standard table instead of creating a duplicate
- D. Create the table in the Dataverse data workspace

### 11. A distributor list is proposed in SharePoint to avoid modelling. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Store the interactions in the Activity table
- B. Keep the records in a SharePoint list and skip Dataverse
- C. Extend the standard table instead of creating a duplicate
- D. Create the table in the Dataverse data workspace

### 12. Winery contacts must reuse the fields users already know. What should be used?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Create a custom table for the new business entity
- C. Store the account name as text so the form stays simple
- D. Store the interactions in the Activity table

### 13. An allocation must be owned by a team and keep its history. What decides that?

Domain: Create a foundation for intelligent applications

- A. Configure a row summary to summarize the record text
- B. Configure table properties such as ownership and auditing
- C. Extend the standard table instead of creating a duplicate
- D. Enable auditing on the tables that hold regulated data

### 14. Grape varieties must be identical in two tables. What should be used?

Domain: Create a foundation for intelligent applications

- A. Use a lookup column instead of storing the name as text
- B. Use a global choice so several tables share one option list
- C. Store the account name as text so the form stays simple
- D. Add a choice column for the fixed set of options

### 15. A yield ratio must stay exact across recalculation. Which column type fits?

Domain: Create a foundation for intelligent applications

- A. Store the account name as text so the form stays simple
- B. Use a decimal column for an exact rate
- C. Use a currency column with the record currency
- D. Use an auto-number column for the case identifier

### 16. A field must accept approved values and point at the distributor record. Which two column types apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Use a currency column with the record currency
- B. Add a choice column for the fixed set of options
- C. Store the account name as text so the form stays simple
- D. Use a lookup column instead of storing the name as text
- E. Use a calculated column for the value that must never change

### 17. An allocation belongs to one distributor and a distributor has many allocations. How should that be modelled?

Domain: Create a foundation for intelligent applications

- A. Model the many-to-many link with a native N:N relationship
- B. Keep the relationship referential so child records survive the parent delete
- C. Configure a one-to-many relationship with a lookup on the child table
- D. Set the relationship behaviour to parental so child records are removed with the parent

### 18. A distributor must survive the deletion of an old allocation. What behaviour fits?

Domain: Create a foundation for intelligent applications

- A. Keep the relationship referential so child records survive the parent delete
- B. Set the relationship behaviour to parental so child records are removed with the parent
- C. Configure a one-to-many relationship with a lookup on the child table
- D. Model the many-to-many link with a native N:N relationship

### 19. Every sales rep must see the same list of open allocations. What should be created?

Domain: Create a foundation for intelligent applications

- A. Change the system view so the list order suits the team
- B. Create a public view for the shared filtered list
- C. Rely on each user's personal view of the table
- D. Design the main form around the record the user opens

### 20. A sales team needs one shared list and one working form. Which two components apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Add a quick-create form for entry from a lookup
- B. Design the main form around the record the user opens
- C. Change the system view so the list order suits the team
- D. Rely on each user's personal view of the table
- E. Create a public view for the shared filtered list

### 21. A regional rep may read only their region's distributors. What grants that?

Domain: Create a foundation for intelligent applications

- A. Move the user to another business unit to fix access
- B. Assign a security role that grants only the privileges the role needs
- C. Use a field security profile for the sensitive column
- D. Assign the record to a team that the group owns

### 22. A cost column must stay hidden from sales while the account stays visible. What should be used?

Domain: Create a foundation for intelligent applications

- A. Assign the record to a team that the group owns
- B. Use a field security profile for the sensitive column
- C. Assign a security role that grants only the privileges the role needs
- D. Move the user to another business unit to fix access

### 23. Access must be granted per table and one column hidden. Which two controls apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Create a public view for the shared filtered list
- B. Assign the record to a team that the group owns
- C. Use a field security profile for the sensitive column
- D. Move the user to another business unit to fix access
- E. Assign a security role that grants only the privileges the role needs

### 24. A winery must decide whether an agent is worth building. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Measure the outcome → pilot the agent in development → build a custom agent → map the requirement to a component → check built-in coverage
- B. Build a custom agent → map the requirement to a component → pilot in development → measure the outcome → check built-in coverage
- C. Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it
- D. Check whether a built-in agent covers it → build a custom agent → adopt it in production → map the requirement to a component → pilot in development

### 25. A distributor portal must reach the right boundary under control. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline
- B. Create the solution with its publisher → deploy through the pipeline → identify the data boundary → choose the environment type
- C. Choose the environment type → deploy through the pipeline → identify the data boundary → create the solution with its publisher
- D. Deploy through the pipeline → create the solution with its publisher → choose the environment type → identify the data boundary

### 26. An allocation form carries forty columns and reps use ten. What should change?

Domain: Create intelligent applications

- A. Add the columns the role uses to the main form
- B. Hide the field with a JavaScript web resource
- C. Choose the view columns before setting the filter
- D. Organize the long form into tabs and sections

### 27. A long form must stay reachable without a wall of inputs. What should be done?

Domain: Create intelligent applications

- A. Add the column to a card form on the main form
- B. Choose the view columns before setting the filter
- C. Add the columns the role uses to the main form
- D. Organize the long form into tabs and sections

### 28. A queue must be readable at a glance without opening each allocation. What must be chosen first?

Domain: Create intelligent applications

- A. Choose the view columns before setting the filter
- B. Filter the view on the columns the team actually searches
- C. Write FetchXML for the view to get the exact rows
- D. Create a public view for the shared filtered list

### 29. A queue must show only allocations awaiting approval in this region. What decides that?

Domain: Create intelligent applications

- A. Filter the view on the columns the team actually searches
- B. Write FetchXML for the view to get the exact rows
- C. Create a public view for the shared filtered list
- D. Choose the view columns before setting the filter

### 30. A vintage summary page does not exist and a draft is needed this week. What should be done?

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Generate the page from a natural-language description, then refine it
- C. Replace the main form with the generated page
- D. Publish the generated page without reviewing its data bindings

### 31. A maker replaces the allocation main form with a generated page. What is lost?

Domain: Create intelligent applications

- A. Replace the main form with the generated page
- B. Hide the field with a JavaScript web resource
- C. Publish the generated page without reviewing its data bindings
- D. Generate the page from a natural-language description, then refine it

### 32. The sales app must expose three forms and two views. What decides that?

Domain: Create intelligent applications

- A. Configure the navigation in the sitemap designer
- B. Add the forms, views, and pages to the app in the app designer
- C. Share the app only and rely on the app for access
- D. Share the app and assign the security role that backs it

### 33. Users cannot find the allocation area anywhere in the app. What should be configured?

Domain: Create intelligent applications

- A. Add the forms, views, and pages to the app in the app designer
- B. Configure the navigation in the sitemap designer
- C. Share the app and assign the security role that backs it
- D. Share the app only and rely on the app for access

### 34. A manager wants the allocation trend without a second query definition. What should be created?

Domain: Create intelligent applications

- A. Add the chart and the views to a dashboard
- B. Filter the view on the columns the team actually searches
- C. Create the chart on the view for the trend
- D. Build the chart in Power BI and embed it

### 35. A manager needs a bound trend and one page holding it with the queue. Which two components apply? Select two.

Domain: Create intelligent applications

- A. Add the forms, views, and pages to the app in the app designer
- B. Filter the view on the columns the team actually searches
- C. Build the chart in Power BI and embed it
- D. Add the chart and the views to a dashboard
- E. Create the chart on the view for the trend

### 36. A tasting-room app must exist over two tables by Friday. What should the maker do first?

Domain: Create intelligent applications

- A. Use the tablet layout for desk-based users
- B. Generate a canvas app from the data source
- C. Use the phone layout for field staff
- D. Write the filter so the data source performs the delegation

### 37. Tasting-room staff capture visits on a handset. Which layout fits?

Domain: Create intelligent applications

- A. Fix the layout to one pixel width so it always looks the same
- B. Use the phone layout for field staff
- C. Use responsive containers so the layout adapts to the device
- D. Use the tablet layout for desk-based users

### 38. One app must serve a phone in the field and a desktop in the office. What should be used?

Domain: Create intelligent applications

- A. Use responsive containers so the layout adapts to the device
- B. Fix the layout to one pixel width so it always looks the same
- C. Use the phone layout for field staff
- D. Use the tablet layout for desk-based users

### 39. A distributor-facing app must work with a screen reader. What must be added?

Domain: Create intelligent applications

- A. Add accessible labels and screen-reader text to the controls
- B. Fix the layout to one pixel width so it always looks the same
- C. Filter in Power Fx after loading the rows into the app
- D. Convey status with colour alone

### 40. Three apps must share one winery header. What should be used?

Domain: Create intelligent applications

- A. Publish a component library for the shared header and controls
- B. Create a user-defined function for the reused expression
- C. Copy the screen into every app that needs it
- D. Define a named formula for the shared calculation

### 41. A shared allocation calculation takes two inputs. What should be used?

Domain: Create intelligent applications

- A. Copy the screen into every app that needs it
- B. Define a named formula for the shared calculation
- C. Publish a component library for the shared header and controls
- D. Create a user-defined function for the reused expression

### 42. A selection must not leak from the allocation screen to the forecast screen. What should be used?

Domain: Create intelligent applications

- A. Use a context variable scoped to the screen
- B. Clear the collection when the screen changes
- C. Use a global variable for the value that the whole app needs
- D. Collect the rows into a collection for in-memory work

### 43. A change to the rep screen must not break the existing flow. What should be run first?

Domain: Create intelligent applications

- A. Use Monitor to inspect the network call and the formula that fired
- B. Wrap the call in IfError and surface the message to the user
- C. Run the app in Test Studio before publishing
- D. Write a Trace message for the support team

### 44. A rep wants to ask about a distributor inside the app. What should be added?

Domain: Create intelligent applications

- A. Build a second canvas app just to host the agent
- B. Build a custom Copilot Studio agent for every requirement
- C. Add the Copilot Studio agent to the canvas app as a component
- D. Call the agent's endpoint directly from Power Fx

### 45. A screen must be proven before release and a slow call explained. Which two tools apply? Select two.

Domain: Create intelligent applications

- A. Call the agent's endpoint directly from Power Fx
- B. Write a Trace message for the support team
- C. Use Monitor to inspect the network call and the formula that fired
- D. Wrap the call in IfError and surface the message to the user
- E. Run the app in Test Studio before publishing

### 46. A sales app must be composed and released to reps. Which sequence is correct?

Domain: Create intelligent applications

- A. Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role
- B. Share the app → assign the backing security role → configure the forms and views → compose the app → set the navigation
- C. Set the navigation in the sitemap → share the app → configure the forms and views → compose the app → assign the role
- D. Assign the backing security role → configure the forms and views → set the navigation → compose the app → share the app

### 47. A tasting-room app must reach staff without a broken save. Which sequence is correct?

Domain: Create intelligent applications

- A. Build the screens → test with Monitor → connect the data source → publish the app → add error handling
- B. Publish the app → connect the data source → build the screens → add error handling → test with Monitor and Test Studio
- C. Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app
- D. Add error handling → connect the data source → test with Monitor → build the screens → publish the app

### 48. A rep decides when to request an allocation increase. What should be used?

Domain: Build business application logic and automation

- A. Use an automated trigger on record creation
- B. Use a manually triggered flow from the app
- C. Expose an HTTP request trigger with a signed URL
- D. Use a scheduled trigger for the nightly batch

### 49. A weekly allocation forecast must be emailed every Monday. What should be used?

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Use a manually triggered flow from the app
- C. Expose an HTTP request trigger with a signed URL
- D. Use an automated trigger on record creation

### 50. A flow must run only when an allocation status becomes approved. What should be used?

Domain: Build business application logic and automation

- A. Expose an HTTP request trigger with a signed URL
- B. Use an automated trigger on record creation
- C. Trigger when a chosen column changes, with a filter condition
- D. Trigger on every update so nothing is missed

### 51. The source is a premium-only service. What is justified?

Domain: Build business application logic and automation

- A. Copy the data into Excel to avoid a premium connector
- B. Build a custom connector for the internal API
- C. Use the premium connector the source requires
- D. Use the standard Dataverse connector

### 52. A group works around a premium licence by moving order data through a spreadsheet. Which connector does that pattern rely on?

Domain: Build business application logic and automation

- A. Build a custom connector for the internal API
- B. Use the standard Dataverse connector
- C. Copy the data into Excel to avoid a premium connector
- D. Use the premium connector the source requires

### 53. One named sales director must approve an over-allocation. Which approval type fits?

Domain: Build business application logic and automation

- A. Choose the approval type that matches the sign-off the process requires
- B. Send parallel approvals and require every response
- C. Send an email and treat silence as approval
- D. Start and wait for an approval

### 54. The sales director and the winemaker must both approve. What should be configured?

Domain: Build business application logic and automation

- A. Send parallel approvals and require every response
- B. Choose the approval type that matches the sign-off the process requires
- C. Start and wait for an approval
- D. Send an email and treat silence as approval

### 55. A manager wants to approve by simply replying to a notification. What does that rely on?

Domain: Build business application logic and automation

- A. Chain two approvals in sequence for the second-level sign-off
- B. Send an email and treat silence as approval
- C. Choose the approval type that matches the sign-off the process requires
- D. Start and wait for an approval

### 56. A downstream action expects one object built from three allocation fields. What should be used?

Domain: Build business application logic and automation

- A. Add a condition to branch on the status
- B. Parse JSON so later steps can use the fields
- C. Apply to each over the returned rows
- D. Use Compose to shape the payload the next step consumes

### 57. A response contains twenty allocation rows that must each be updated. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Add a condition to branch on the status
- C. Apply to each over the returned rows
- D. Use a switch for the multi-way branch

### 58. A call to a slow distributor service may need three attempts. What should be used?

Domain: Build business application logic and automation

- A. Add a condition to branch on the status
- B. Wrap the steps in a Scope so one error path handles the failures
- C. Use Do until with a bounded count for the retry loop
- D. Use a switch for the multi-way branch

### 59. A retry loop only ends when a record appears, and it carries no count limit. What is the defect?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Add a condition to branch on the status
- C. Use a switch for the multi-way branch
- D. Loop until the record is found with no exit limit

### 60. A nightly import fails and the designer output looks empty. Where can the failing input be read?

Domain: Build business application logic and automation

- A. Turn on static result to test the rest of the flow
- B. Resubmit the failed run after the fix
- C. Read the run history to find the failed action and its inputs
- D. Test the flow with the real trigger payload

### 61. The corrected flow is live but yesterday's failed run is still open. Which action completes it safely?

Domain: Build business application logic and automation

- A. Turn on static result to test the rest of the flow
- B. Test the flow with the real trigger payload
- C. Read the run history to find the failed action and its inputs
- D. Resubmit the failed run after the fix

### 62. A novel allocation task has no template and the instruction must be written. What should be done?

Domain: Build business application logic and automation

- A. Start from a prompt template in AI Hub
- B. Copy the prompt text into each app so it can be tuned per app
- C. Add typed inputs so the prompt takes values
- D. Build the prompt from blank

### 63. A prompt must take the distributor name as a value each run. What should be added?

Domain: Build business application logic and automation

- A. Add the knowledge source so the prompt grounds on approved content
- B. Add typed inputs so the prompt takes values
- C. Copy the prompt text into each app so it can be tuned per app
- D. Choose the model that fits the task instead of the largest available

### 64. A recap must cite the approved allocation policy. What should be attached?

Domain: Build business application logic and automation

- A. Add the knowledge source so the prompt grounds on approved content
- B. Choose the model that fits the task instead of the largest available
- C. Copy the prompt text into each app so it can be tuned per app
- D. Add typed inputs so the prompt takes values

### 65. A recap must cite the policy and accept values. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Start from a prompt template in AI Hub
- C. Choose the model that fits the task instead of the largest available
- D. Copy the prompt text into each app so it can be tuned per app
- E. Add the knowledge source so the prompt grounds on approved content

### 66. Recaps are good enough on a small model and the bill is high. What should change?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Choose the model that fits the task instead of the largest available
- C. Add typed inputs so the prompt takes values
- D. Add the knowledge source so the prompt grounds on approved content

### 67. The recap instruction is pasted into each app to tune it separately. What is the objection?

Domain: Build business application logic and automation

- A. Call the prompt from the canvas app through its connector
- B. Call the prompt from the cloud flow action
- C. Copy the prompt text into each app so it can be tuned per app
- D. Start from a prompt template in AI Hub

### 68. A rep must generate the recap while looking at the allocation. What should be used?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Choose the model that fits the task instead of the largest available
- C. Call the prompt from the canvas app through its connector
- D. Call the prompt from the cloud flow action

### 69. A custom AI Hub model must be called from the app with authentication in one place. What should be used?

Domain: Build business application logic and automation

- A. Call the model from the flow and store the result on the record
- B. Call the prompt from the canvas app through its connector
- C. Copy the prompt text into each app so it can be tuned per app
- D. Consume the AI Hub model through the same connector pattern as a prompt

### 70. An allocation must require a justification whenever it exceeds the band. What should be used?

Domain: Build business application logic and automation

- A. Add a JavaScript web resource to the form
- B. Set the business rule scope to the table so it applies in every form
- C. Hide the field with a JavaScript web resource
- D. Configure a business rule on the table

### 71. A rule behaves on the form but is skipped when records arrive by integration. What should change?

Domain: Build business application logic and automation

- A. Write a Dataverse plug-in in C#
- B. Hide the field with a JavaScript web resource
- C. Configure a business rule on the table
- D. Set the business rule scope to the table so it applies in every form

### 72. An allocation must move through four ordered stages with required information. What should be built?

Domain: Build business application logic and automation

- A. Model the stages in a business process flow
- B. Configure a business rule on the table
- C. Use a rollup column to aggregate the child records
- D. Branch the business process flow on the case type

### 73. An allocation value must recalculate from two columns. What should be used?

Domain: Build business application logic and automation

- A. Use a calculated column for the value that must never change
- B. Write a plug-in to set the value on every update
- C. Use a formula column where the rule needs Power Fx
- D. Use a rollup column to aggregate the child records

### 74. A value must be set on every write including imports. What should be used?

Domain: Build business application logic and automation

- A. Use a rollup column to aggregate the child records
- B. Use a formula column where the rule needs Power Fx
- C. Write a plug-in to set the value on every update
- D. Use a calculated column for the value that must never change

### 75. A rule must run inside every allocation save with no way to bypass it. What should be used?

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Enforce the rule in a synchronous plug-in when it must run on every write
- C. Add a JavaScript web resource to the form
- D. Use a formula column where the rule needs Power Fx

### 76. A flow must start on a new allocation and only for approved ones. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Trigger on every update so nothing is missed
- B. Expose an HTTP request trigger with a signed URL
- C. Use a scheduled trigger for the nightly batch
- D. Trigger when a chosen column changes, with a filter condition
- E. Use an automated trigger on record creation

### 77. An over-allocation must pause for a recorded decision. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Chain two approvals in sequence for the second-level sign-off
- C. Choose the approval type that matches the sign-off the process requires
- D. Start and wait for an approval
- E. Send an email and treat silence as approval

### 78. A multi-step block must report one failure and hand control to a handler. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Configure run after so the failure path actually executes
- B. Wrap the steps in a Scope so one error path handles the failures
- C. Turn on concurrency control for the loop
- D. Use a switch for the multi-way branch
- E. Add a condition to branch on the status

### 79. A failing flow must be diagnosed and proven. Which two practices apply? Select two.

Domain: Build business application logic and automation

- A. Read the run history to find the failed action and its inputs
- B. Turn on static result to test the rest of the flow
- C. Resubmit the failed run after the fix
- D. Parse JSON so later steps can use the fields
- E. Test the flow with the real trigger payload

### 80. A recap prompt must start tested and use a model matched to the task. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Add typed inputs so the prompt takes values
- C. Choose the model that fits the task instead of the largest available
- D. Start from a prompt template in AI Hub
- E. Build the prompt from blank

### 81. Validation must cover records imported in bulk and records saved from code. Which two mechanisms apply? Select two.

Domain: Build business application logic and automation

- A. Use a calculated column for the value that must never change
- B. Hide the field with a JavaScript web resource
- C. Add a JavaScript web resource to the form
- D. Configure a business rule on the table
- E. Enforce the rule in a synchronous plug-in when it must run on every write

### 82. A value must recalculate and a distributor must show its allocation count. Which two column types apply? Select two.

Domain: Build business application logic and automation

- A. Write a plug-in to set the value on every update
- B. Use a calculated column for the value that must never change
- C. Configure a business rule on the table
- D. Use a rollup column to aggregate the child records
- E. Use a formula column where the rule needs Power Fx

### 83. An allocation workflow must reach production without wrong expressions. Which sequence is correct?

Domain: Build business application logic and automation

- A. Read the run history → add the trigger → decide which event starts the process → add the actions → test with a real payload
- B. Test with a real payload → decide which event starts the process → read the run history → add the trigger → add the actions
- C. Add the actions and branches → add the trigger → test with a real payload → decide which event starts the process → read the run history
- D. Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run

### 84. An over-allocation must be decided and the decision recorded. Which sequence is correct?

Domain: Build business application logic and automation

- A. Branch on the outcome → trigger on the submitted request → notify the requester → start and wait for the approval → update the record
- B. Notify the requester → update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome
- C. Update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome → notify the requester
- D. Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester

### 85. A failing allocation notification must be fixed with confidence. Which sequence is correct?

Domain: Build business application logic and automation

- A. Open the run history → resubmit the run → reproduce the failure → inspect the failing action → fix the expression
- B. Fix the expression → reproduce the failure → resubmit the run → inspect the failing action → open the run history
- C. Resubmit the run → open the run history → reproduce the failure → fix the expression → inspect the failing action
- D. Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run

### 86. An allocation value must be derived and shown on the form. Which sequence is correct?

Domain: Build business application logic and automation

- A. Configure the formula or rollup → decide whether the value is derived or aggregated → surface the column → add the column → verify the recalculation
- B. Surface the column on the form → add the column of the matching type → decide whether the value is derived or aggregated → verify the recalculation → configure the formula or rollup
- C. Decide whether the value is derived at read time or aggregated from children → add the column of the matching type → configure the formula or the rollup → verify the recalculation on a test record → surface the column on the form and view
- D. Verify the recalculation on a test record → surface the column on the form → configure the formula or rollup → add the column → decide whether the value is derived or aggregated

### 87. Several apps must share one header and one tasting-room calculation. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Copy the screen into every app that needs it
- B. Fix the layout to one pixel width so it always looks the same
- C. Publish a component library for the shared header and controls
- D. Define a named formula for the shared calculation
- E. Create a user-defined function for the reused expression

### 88. A chosen distributor must persist across screens and failures must be recoverable. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Collect the rows into a collection for in-memory work
- B. Use a context variable scoped to the screen
- C. Write a Trace message for the support team
- D. Wrap the call in IfError and surface the message to the user
- E. Use a global variable for the value that the whole app needs

---

## Case study — Coho Winery

Coho Winery sells to 900 restaurants and distributors across four states. Orders arrive by email and phone, and the sales team rebuilds a forecast every Monday from a spreadsheet. Distributor allocations are contested, and the winery promises volumes before bottling confirms them. The sales director wants a distributor portal, an allocation approval when a distributor requests more than its committed volume, and a weekly forecast view. The winery has Dataverse, a premium connector budget, and a two-person IT team that must support whatever is built. Nothing may be deployed without a test environment sign-off.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. A schema name must be right the first time. What must be decided before the first table?

Domain: Create a foundation for intelligent applications

- A. Import unmanaged customizations directly into production
- B. Define the solution publisher and prefix once, before the first table
- C. Clone the environment each time instead of using a pipeline
- D. Package the customizations in a solution before moving them

### 90. Sales reps check allocations on a phone in the field. Which layout fits?

Domain: Create intelligent applications

- A. Use the phone layout for field staff
- B. Fix the layout to one pixel width so it always looks the same
- C. Use responsive containers so the layout adapts to the device
- D. Use the tablet layout for desk-based users

### 91. Order data lives in a premium-only service. What is justified?

Domain: Build business application logic and automation

- A. Copy the data into Excel to avoid a premium connector
- B. Use the standard Dataverse connector
- C. Build a custom connector for the internal API
- D. Use the premium connector the source requires

---

## Case study — Fourth Coffee

Fourth Coffee operates 140 cafés and a wholesale bean business. Store managers order supplies by phone to a central buyer, who keys the orders into a spreadsheet. Stockouts of the best-selling blend happen two or three times a month. The operations director wants a store ordering app, an approval when an order exceeds a store's monthly budget, a replenishment suggestion from recent sales, and a daily exception list of stores with an unfilled order. The company has one maker, Dataverse, and a policy that no store manager may see another store's financial data.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The store manager's store must be available on every screen. What should be used?

Domain: Create intelligent applications

- A. Clear the collection when the screen changes
- B. Use a global variable for the value that the whole app needs
- C. Use a context variable scoped to the screen
- D. Collect the rows into a collection for in-memory work

### 93. An order above the store budget needs a recorded decision. What action fits?

Domain: Build business application logic and automation

- A. Start and wait for an approval
- B. Chain two approvals in sequence for the second-level sign-off
- C. Choose the approval type that matches the sign-off the process requires
- D. Send an email and treat silence as approval

### 94. The replenishment flow must run only for unfilled orders. What should be added?

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Trigger when a chosen column changes, with a filter condition
- C. Use an automated trigger on record creation
- D. Trigger on every update so nothing is missed

---

## Case study — Nod Publishers

Nod Publishers produces 1,500 titles a year and licenses content to libraries and retailers. Rights are tracked in contracts that live in three shared drives, and a title is occasionally sold in a territory where the rights have lapsed. The rights director wants a single rights record per title and territory, a warning when a deal would breach a lapsed right, an approval for exceptions, and a searchable view for the sales team. Contracts arrive as PDFs, and the team wants AI to extract the key terms into the rights record.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Each rights record needs an AI summary of its contract terms. What should be configured?

Domain: Create a foundation for intelligent applications

- A. Use a calculated column for the value that must never change
- B. Add a JavaScript web resource to the form
- C. Configure a prompt column to generate text per row
- D. Configure a row summary to summarize the record text

### 96. The rights form carries fields nobody uses. What should change?

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Hide the field with a JavaScript web resource
- C. Add the columns the role uses to the main form
- D. Choose the view columns before setting the filter

### 97. Extracted terms must be checked against the contract text. What should be attached?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Add typed inputs so the prompt takes values
- C. Choose the model that fits the task instead of the largest available
- D. Add the knowledge source so the prompt grounds on approved content

---

## Case study — Trey Research

Trey Research is a 400-person contract research organisation running 60 concurrent clinical studies. Study coordinators record participant visits on paper, and the quality team reconciles them monthly. A missed visit is a protocol deviation, so the sponsor requires evidence of every scheduled and completed visit. The organisation wants a coordinator app, an automated reminder, and a deviation record with an approval. Participant identifiers are sensitive, and the sponsor's auditors need read-only access to a study without seeing any other study.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Two coordinators share one queue of visits. What should own the records?

Domain: Create a foundation for intelligent applications

- A. Assign the record to a team that the group owns
- B. Move the user to another business unit to fix access
- C. Assign a security role that grants only the privileges the role needs
- D. Use a field security profile for the sensitive column

### 99. A coordinator list must show only today's scheduled visits. What decides that?

Domain: Create intelligent applications

- A. Create a public view for the shared filtered list
- B. Write FetchXML for the view to get the exact rows
- C. Choose the view columns before setting the filter
- D. Filter the view on the columns the team actually searches

### 100. A deviation must require a reason before it can be saved. What should be configured?

Domain: Build business application logic and automation

- A. Use a calculated column for the value that must never change
- B. Set the business rule scope to the table so it applies in every form
- C. Configure a business rule on the table
- D. Add a JavaScript web resource to the form

---

## Answer key and explanations

### Question 1 — A

Answer: Map each requirement to the Power Platform component that fits it. Mapping requirements to components keeps the solution minimal. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. In this case: Mapping requirements to components keeps the solution minimal.
- **B:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.
- **C:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.
- **D:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.

### Question 2 — D

Answer: Deliver every requirement as a single model-driven app. One app widens access to every table it contains. One app for everything widens access and makes the smallest change a release of the whole solution. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: One app widens access to every table it contains.
- **B:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: One app widens access to every table it contains.
- **C:** Incorrect for this question. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Why the correct answer wins: One app widens access to every table it contains.
- **D:** Correct. One app for everything widens access and makes the smallest change a release of the whole solution. In this case: One app widens access to every table it contains.

### Question 3 — D

Answer: Model the process as a cloud flow with no agent at all. A deterministic process belongs in a flow. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A deterministic process belongs in a flow.
- **B:** Incorrect for this question. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Why the correct answer wins: A deterministic process belongs in a flow.
- **C:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: A deterministic process belongs in a flow.
- **D:** Correct. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. In this case: A deterministic process belongs in a flow.

### Question 4 — B

Answer: Adopt the built-in agent that already covers the task. A built-in agent is maintained by the platform and carries less build cost. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **B:** Correct. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. In this case: A built-in agent is maintained by the platform and carries less build cost.
- **C:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **D:** Incorrect for this question. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.

### Question 5 — D

Answer: Build a custom Copilot Studio agent for every requirement. A custom agent earns its cost when the built-in one cannot reach the data. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.
- **B:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.
- **C:** Incorrect for this question. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.
- **D:** Correct. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. In this case: A custom agent earns its cost when the built-in one cannot reach the data.

### Question 6 — C

Answer: Build a Power Apps component framework control. A PCF control covers a visual the standard control cannot express. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **B:** Incorrect for this question. A deliberate later replacement rarely happens, and meanwhile two implementations must be maintained. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **C:** Correct. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. In this case: A PCF control covers a visual the standard control cannot express.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.

### Question 7 — D

Answer: Choose the environment type that matches the data boundary and the licence. Environment type sets the boundary and licensing. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The default environment has the widest membership and the least governance, which is where a regulated solution should not start. Why the correct answer wins: Environment type sets the boundary and licensing.
- **B:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: Environment type sets the boundary and licensing.
- **C:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: Environment type sets the boundary and licensing.
- **D:** Correct. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. In this case: Environment type sets the boundary and licensing.

### Question 8 — D

Answer: Do all building in the production environment to avoid deployment. Building in production removes the test step and exposes unfinished work. Building in production removes the test step and puts every unfinished change in front of users. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: Building in production removes the test step and exposes unfinished work.
- **B:** Incorrect for this question. A sandbox is for build, test, and acceptance; it is not a production target. Why the correct answer wins: Building in production removes the test step and exposes unfinished work.
- **C:** Incorrect for this question. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Why the correct answer wins: Building in production removes the test step and exposes unfinished work.
- **D:** Correct. Building in production removes the test step and puts every unfinished change in front of users. In this case: Building in production removes the test step and exposes unfinished work.

### Question 9 — B, C

Answers: Define the solution publisher and prefix once, before the first table; Package the customizations in a solution before moving them. The publisher fixes the prefix, and the solution is the unit of movement. The prefix is baked into every schema name and is expensive to change after data exists. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.
- **B:** Correct. The prefix is baked into every schema name and is expensive to change after data exists. In this case: The publisher fixes the prefix, and the solution is the unit of movement.
- **C:** Correct. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. In this case: The publisher fixes the prefix, and the solution is the unit of movement.
- **D:** Incorrect for this question. The automation is not the hard part; the solution boundary and the deployment order are. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.
- **E:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.

### Question 10 — D

Answer: Create the table in the Dataverse data workspace. The data workspace is where a new table is created. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Why the correct answer wins: The data workspace is where a new table is created.
- **B:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: The data workspace is where a new table is created.
- **C:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: The data workspace is where a new table is created.
- **D:** Correct. The data workspace lets a maker model tables and relationships without leaving the app-building flow. In this case: The data workspace is where a new table is created.

### Question 11 — B

Answer: Keep the records in a SharePoint list and skip Dataverse. A list has no relationships, security roles, or rollup columns. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **B:** Correct. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. In this case: A list has no relationships, security roles, or rollup columns.
- **C:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **D:** Incorrect for this question. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.

### Question 12 — A

Answer: Extend the standard table instead of creating a duplicate. Extending the standard table keeps the built-in relationships. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. In this case: Extending the standard table keeps the built-in relationships.
- **B:** Incorrect for this question. A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **D:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: Extending the standard table keeps the built-in relationships.

### Question 13 — B

Answer: Configure table properties such as ownership and auditing. Ownership and auditing are table properties. Ownership decides who can see a row and auditing decides whether its history survives an investigation. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: Ownership and auditing are table properties.
- **B:** Correct. Ownership decides who can see a row and auditing decides whether its history survives an investigation. In this case: Ownership and auditing are table properties.
- **C:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Ownership and auditing are table properties.
- **D:** Incorrect for this question. Auditing records who changed which column and when, which is what an audit asks for. Why the correct answer wins: Ownership and auditing are table properties.

### Question 14 — B

Answer: Use a global choice so several tables share one option list. A global choice keeps one approved list across tables. One global choice keeps the list consistent instead of drifting across tables. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Why the correct answer wins: A global choice keeps one approved list across tables.
- **B:** Correct. One global choice keeps the list consistent instead of drifting across tables. In this case: A global choice keeps one approved list across tables.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A global choice keeps one approved list across tables.
- **D:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A global choice keeps one approved list across tables.

### Question 15 — B

Answer: Use a decimal column for an exact rate. A decimal type avoids the rounding drift that currency arithmetic would introduce. A decimal avoids the rounding drift that a floating-point column introduces in a rate. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A decimal type avoids the rounding drift that currency arithmetic would introduce.
- **B:** Correct. A decimal avoids the rounding drift that a floating-point column introduces in a rate. In this case: A decimal type avoids the rounding drift that currency arithmetic would introduce.
- **C:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A decimal type avoids the rounding drift that currency arithmetic would introduce.
- **D:** Incorrect for this question. An auto-number gives every record a readable, unique reference that users can quote. Why the correct answer wins: A decimal type avoids the rounding drift that currency arithmetic would introduce.

### Question 16 — B, D

Answers: Add a choice column for the fixed set of options; Use a lookup column instead of storing the name as text. A choice constrains the value, and a lookup carries the relationship. A choice constrains input to the approved list and renders as a dropdown on every form. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **B:** Correct. A choice constrains input to the approved list and renders as a dropdown on every form. In this case: A choice constrains the value, and a lookup carries the relationship.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **D:** Correct. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. In this case: A choice constrains the value, and a lookup carries the relationship.
- **E:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.

### Question 17 — C

Answer: Configure a one-to-many relationship with a lookup on the child table. A one-to-many relationship with the lookup on the child is the standard shape. The lookup on the child is what makes the parent select a record rather than a typed string. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **B:** Incorrect for this question. Referential behaviour leaves the children in place, which is what a shared dimension needs. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **C:** Correct. The lookup on the child is what makes the parent select a record rather than a typed string. In this case: A one-to-many relationship with the lookup on the child is the standard shape.
- **D:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.

### Question 18 — A

Answer: Keep the relationship referential so child records survive the parent delete. Referential behaviour leaves the parent in place. Referential behaviour leaves the children in place, which is what a shared dimension needs. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Referential behaviour leaves the children in place, which is what a shared dimension needs. In this case: Referential behaviour leaves the parent in place.
- **B:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: Referential behaviour leaves the parent in place.
- **C:** Incorrect for this question. The lookup on the child is what makes the parent select a record rather than a typed string. Why the correct answer wins: Referential behaviour leaves the parent in place.
- **D:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: Referential behaviour leaves the parent in place.

### Question 19 — B

Answer: Create a public view for the shared filtered list. A public view is shared with everyone who has access to the table. A public view is available to everyone with access to the table, so the team sees the same list. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **B:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: A public view is shared with everyone who has access to the table.
- **C:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **D:** Incorrect for this question. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Why the correct answer wins: A public view is shared with everyone who has access to the table.

### Question 20 — B, E

Answers: Create a public view for the shared filtered list; Design the main form around the record the user opens. The public view is the shared list, and the main form is the working surface. A public view is available to everyone with access to the table, so the team sees the same list. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **B:** Correct. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. In this case: The public view is the shared list, and the main form is the working surface.
- **C:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **D:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **E:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: The public view is the shared list, and the main form is the working surface.

### Question 21 — B

Answer: Assign a security role that grants only the privileges the role needs. A security role grants privileges at a scope. A security role is how Dataverse decides create, read, write, and delete per table. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A security role grants privileges at a scope.
- **B:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: A security role grants privileges at a scope.
- **C:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: A security role grants privileges at a scope.
- **D:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A security role grants privileges at a scope.

### Question 22 — B

Answer: Use a field security profile for the sensitive column. A field security profile hides a column without hiding the record. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **B:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: A field security profile hides a column without hiding the record.
- **C:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **D:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A field security profile hides a column without hiding the record.

### Question 23 — C, E

Answers: Assign a security role that grants only the privileges the role needs; Use a field security profile for the sensitive column. The role grants table privileges, and the profile hides the column. A security role is how Dataverse decides create, read, write, and delete per table. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **B:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **C:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: The role grants table privileges, and the profile hides the column.
- **D:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **E:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: The role grants table privileges, and the profile hides the column.

### Question 24 — C

Answer: Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it. Coverage is tested with a pilot before committing to a custom build. Coverage is tested with a pilot before anyone commits to a custom build. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. There is nothing to measure before a pilot exists. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **B:** Incorrect for this question. Building first pays the custom-agent cost before coverage is even known. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **C:** Correct. Coverage is tested with a pilot before anyone commits to a custom build. In this case: Coverage is tested with a pilot before committing to a custom build.
- **D:** Incorrect for this question. Adopting before a pilot skips the step that would have caught the gap. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.

### Question 25 — A

Answer: Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline. The boundary and licence decide the environment type, and the pipeline carries the result. The boundary and licence decide the environment type, and the pipeline carries the packaged result. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The boundary and licence decide the environment type, and the pipeline carries the packaged result. In this case: The boundary and licence decide the environment type, and the pipeline carries the result.
- **B:** Incorrect for this question. Choosing an environment after deploying is how a solution ends up in the wrong data boundary. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.
- **C:** Incorrect for this question. Deployment before packaging has nothing to deploy. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.
- **D:** Incorrect for this question. Every step here runs ahead of the decision it depends on. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.

### Question 26 — A

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A form carries the working set of fields for the role.
- **C:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 27 — D

Answer: Organize the long form into tabs and sections. Tabs keep a long form scannable. Tabs keep a forty-column form scannable without hiding the fields behind a click. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A card form gives a compact editing surface for a handful of fields. Why the correct answer wins: Tabs keep a long form scannable.
- **B:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: Tabs keep a long form scannable.
- **C:** Incorrect for this question. A form carries the working set of fields; everything else belongs in a tab or a view. Why the correct answer wins: Tabs keep a long form scannable.
- **D:** Correct. Tabs keep a forty-column form scannable without hiding the fields behind a click. In this case: Tabs keep a long form scannable.

### Question 28 — A

Answer: Choose the view columns before setting the filter. The columns decide what is readable at a glance. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The columns decide what is readable at a glance.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: The columns decide what is readable at a glance.
- **C:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The columns decide what is readable at a glance.
- **D:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The columns decide what is readable at a glance.

### Question 29 — A

Answer: Filter the view on the columns the team actually searches. The filter decides which records are in the list. The filter decides which records appear, so it must match the question the list answers. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides which records are in the list.
- **B:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides which records are in the list.
- **C:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides which records are in the list.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The filter decides which records are in the list.

### Question 30 — B

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close, and the maker owns the bindings. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **B:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close, and the maker owns the bindings.
- **C:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **D:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.

### Question 31 — A

Answer: Replace the main form with the generated page. Replacing the form drops the scripts and business rules attached to it. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A generative page complements the form; replacing it drops the scripting and business rules attached to it. In this case: Replacing the form drops the scripts and business rules attached to it.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: Replacing the form drops the scripts and business rules attached to it.
- **C:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: Replacing the form drops the scripts and business rules attached to it.
- **D:** Incorrect for this question. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Why the correct answer wins: Replacing the form drops the scripts and business rules attached to it.

### Question 32 — B

Answer: Add the forms, views, and pages to the app in the app designer. The app designer decides which components the app exposes. The app designer decides which components the app exposes, so composition is a security-relevant choice. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: The app designer decides which components the app exposes.
- **B:** Correct. The app designer decides which components the app exposes, so composition is a security-relevant choice. In this case: The app designer decides which components the app exposes.
- **C:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The app designer decides which components the app exposes.
- **D:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The app designer decides which components the app exposes.

### Question 33 — B

Answer: Configure the navigation in the sitemap designer. The sitemap is the app's menu. The sitemap is the app's menu, so it decides what a user can reach at all. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: The sitemap is the app's menu.
- **B:** Correct. The sitemap is the app's menu, so it decides what a user can reach at all. In this case: The sitemap is the app's menu.
- **C:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The sitemap is the app's menu.
- **D:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The sitemap is the app's menu.

### Question 34 — C

Answer: Create the chart on the view for the trend. A chart bound to a view reuses that view's filter. A chart bound to a view reuses that view's filter instead of duplicating it. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A dashboard composes several components so a manager sees the whole picture on one page. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **C:** Correct. A chart bound to a view reuses that view's filter instead of duplicating it. In this case: A chart bound to a view reuses that view's filter.
- **D:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: A chart bound to a view reuses that view's filter.

### Question 35 — D, E

Answers: Create the chart on the view for the trend; Add the chart and the views to a dashboard. The chart reuses the view filter, and the dashboard composes the page. A chart bound to a view reuses that view's filter instead of duplicating it. A dashboard composes several components so a manager sees the whole picture on one page. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: The chart reuses the view filter, and the dashboard composes the page.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: The chart reuses the view filter, and the dashboard composes the page.
- **C:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: The chart reuses the view filter, and the dashboard composes the page.
- **D:** Correct. A dashboard composes several components so a manager sees the whole picture on one page. In this case: The chart reuses the view filter, and the dashboard composes the page.
- **E:** Correct. A chart bound to a view reuses that view's filter instead of duplicating it. In this case: The chart reuses the view filter, and the dashboard composes the page.

### Question 36 — B

Answer: Generate a canvas app from the data source. Generating from data gives working screens immediately. Generating from data gives working screens over the chosen tables immediately. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Generating from data gives working screens immediately.
- **B:** Correct. Generating from data gives working screens over the chosen tables immediately. In this case: Generating from data gives working screens immediately.
- **C:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Generating from data gives working screens immediately.
- **D:** Incorrect for this question. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Why the correct answer wins: Generating from data gives working screens immediately.

### Question 37 — B

Answer: Use the phone layout for field staff. The phone layout controls size and reach on a handheld. The phone layout controls the size and reach of controls on a handheld device. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **B:** Correct. The phone layout controls the size and reach of controls on a handheld device. In this case: The phone layout controls size and reach on a handheld.
- **C:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **D:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: The phone layout controls size and reach on a handheld.

### Question 38 — A

Answer: Use responsive containers so the layout adapts to the device. Responsive containers reflow so one app fits both. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. In this case: Responsive containers reflow so one app fits both.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **C:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **D:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Responsive containers reflow so one app fits both.

### Question 39 — A

Answer: Add accessible labels and screen-reader text to the controls. A control without a label is unusable with a screen reader. A control without a label is unusable with a screen reader, however clear it looks. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A control without a label is unusable with a screen reader, however clear it looks. In this case: A control without a label is unusable with a screen reader.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **C:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **D:** Incorrect for this question. Colour alone fails for a colour-blind user and for anyone reading the app in high contrast. Why the correct answer wins: A control without a label is unusable with a screen reader.

### Question 40 — A

Answer: Publish a component library for the shared header and controls. A component library is the reusable, versioned home for a shared control. A component library is the reusable, versioned home for a control that several apps must share. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: A component library is the reusable, versioned home for a shared control.
- **B:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **C:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **D:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.

### Question 41 — D

Answer: Create a user-defined function for the reused expression. A user-defined function accepts parameters and returns a value for reuse. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **B:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **C:** Incorrect for this question. A component library is the reusable, versioned home for a control that several apps must share. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **D:** Correct. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. In this case: A user-defined function accepts parameters and returns a value for reuse.

### Question 42 — A

Answer: Use a context variable scoped to the screen. A context variable lives with the screen. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. In this case: A context variable lives with the screen.
- **B:** Incorrect for this question. An un-cleared collection keeps the previous user's rows in memory. Why the correct answer wins: A context variable lives with the screen.
- **C:** Incorrect for this question. A global variable persists across screens, which is what a signed-in user's selection needs. Why the correct answer wins: A context variable lives with the screen.
- **D:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A context variable lives with the screen.

### Question 43 — C

Answer: Run the app in Test Studio before publishing. Test Studio captures the screens and formulas a regression would break. Test Studio captures the screens and formulas that a regression would break. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **B:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **C:** Correct. Test Studio captures the screens and formulas that a regression would break. In this case: Test Studio captures the screens and formulas a regression would break.
- **D:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.

### Question 44 — C

Answer: Add the Copilot Studio agent to the canvas app as a component. The agent component adds a conversational surface to the app. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A second app multiplies the maintenance without adding capability. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **B:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **C:** Correct. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. In this case: The agent component adds a conversational surface to the app.
- **D:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: The agent component adds a conversational surface to the app.

### Question 45 — C, E

Answers: Use Monitor to inspect the network call and the formula that fired; Run the app in Test Studio before publishing. Test Studio proves the screens, and Monitor explains the timing. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Test Studio captures the screens and formulas that a regression would break. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.
- **B:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.
- **C:** Correct. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. In this case: Test Studio proves the screens, and Monitor explains the timing.
- **D:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.
- **E:** Correct. Test Studio captures the screens and formulas that a regression would break. In this case: Test Studio proves the screens, and Monitor explains the timing.

### Question 46 — A

Answer: Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role. The app is composed from finished components, and access is granted last. The app is composed from finished components, and access is granted last. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The app is composed from finished components, and access is granted last. In this case: The app is composed from finished components, and access is granted last.
- **B:** Incorrect for this question. Sharing an app that has no components shows users an empty shell. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **C:** Incorrect for this question. Navigation is meaningless until the components exist. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **D:** Incorrect for this question. Granting data access before the app exists gives access with nothing to use it in. Why the correct answer wins: The app is composed from finished components, and access is granted last.

### Question 47 — C

Answer: Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app. The data source comes first, and testing precedes publishing. The data source comes first, and testing precedes publishing. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Screens need a data source, and publishing needs a tested app. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **B:** Incorrect for this question. Publishing before testing is how a broken save reaches users. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **C:** Correct. The data source comes first, and testing precedes publishing. In this case: The data source comes first, and testing precedes publishing.
- **D:** Incorrect for this question. Error handling has nothing to wrap before the calls exist. Why the correct answer wins: The data source comes first, and testing precedes publishing.

### Question 48 — B

Answer: Use a manually triggered flow from the app. A manual trigger gives the user the decision about when the process runs. A manual trigger gives the user the decision about when the process runs. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A manual trigger gives the user the decision about when the process runs.
- **B:** Correct. A manual trigger gives the user the decision about when the process runs. In this case: A manual trigger gives the user the decision about when the process runs.
- **C:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A manual trigger gives the user the decision about when the process runs.
- **D:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: A manual trigger gives the user the decision about when the process runs.

### Question 49 — A

Answer: Use a scheduled trigger for the nightly batch. A schedule matches work that must run at a time. A schedule matches work that must run at a time rather than on an event. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A schedule matches work that must run at a time rather than on an event. In this case: A schedule matches work that must run at a time.
- **B:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: A schedule matches work that must run at a time.
- **C:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A schedule matches work that must run at a time.
- **D:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A schedule matches work that must run at a time.

### Question 50 — C

Answer: Trigger when a chosen column changes, with a filter condition. A column filter stops irrelevant updates. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A column filter stops irrelevant updates.
- **B:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A column filter stops irrelevant updates.
- **C:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: A column filter stops irrelevant updates.
- **D:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: A column filter stops irrelevant updates.

### Question 51 — C

Answer: Use the premium connector the source requires. A premium connector is justified when no standard connector reaches the data. A premium connector is justified when the data lives where no standard connector reaches. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.
- **B:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.
- **C:** Correct. A premium connector is justified when the data lives where no standard connector reaches. In this case: A premium connector is justified when no standard connector reaches the data.
- **D:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.

### Question 52 — C

Answer: Copy the data into Excel to avoid a premium connector. A manual copy becomes stale and moves the cost to a person. A manual copy becomes stale and moves the integration cost to a person. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: A manual copy becomes stale and moves the cost to a person.
- **B:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A manual copy becomes stale and moves the cost to a person.
- **C:** Correct. A manual copy becomes stale and moves the integration cost to a person. In this case: A manual copy becomes stale and moves the cost to a person.
- **D:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: A manual copy becomes stale and moves the cost to a person.

### Question 53 — A

Answer: Choose the approval type that matches the sign-off the process requires. Approve or reject is the type for one named approver. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: Approve or reject is the type for one named approver.
- **B:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: Approve or reject is the type for one named approver.
- **C:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Approve or reject is the type for one named approver.
- **D:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Approve or reject is the type for one named approver.

### Question 54 — A

Answer: Send parallel approvals and require every response. Parallel approvals requiring every response match that rule. Everyone must approve is the right type when each stakeholder holds a veto. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Everyone must approve is the right type when each stakeholder holds a veto. In this case: Parallel approvals requiring every response match that rule.
- **B:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: Parallel approvals requiring every response match that rule.
- **C:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Parallel approvals requiring every response match that rule.
- **D:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Parallel approvals requiring every response match that rule.

### Question 55 — B

Answer: Send an email and treat silence as approval. Silence is not a decision and leaves no auditable response. Silence is not a decision, and it leaves no auditable response. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: Silence is not a decision and leaves no auditable response.
- **B:** Correct. Silence is not a decision, and it leaves no auditable response. In this case: Silence is not a decision and leaves no auditable response.
- **C:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: Silence is not a decision and leaves no auditable response.
- **D:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Silence is not a decision and leaves no auditable response.

### Question 56 — D

Answer: Use Compose to shape the payload the next step consumes. Compose builds the exact object the next action expects. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Compose builds the exact object the next action expects.
- **B:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: Compose builds the exact object the next action expects.
- **C:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Compose builds the exact object the next action expects.
- **D:** Correct. Compose builds the exact object the next action expects, which avoids mapping errors downstream. In this case: Compose builds the exact object the next action expects.

### Question 57 — C

Answer: Apply to each over the returned rows. Apply to each iterates the array. Apply to each iterates the array, which is how one run processes many records. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: Apply to each iterates the array.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Apply to each iterates the array.
- **C:** Correct. Apply to each iterates the array, which is how one run processes many records. In this case: Apply to each iterates the array.
- **D:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Apply to each iterates the array.

### Question 58 — C

Answer: Use Do until with a bounded count for the retry loop. Do until repeats until the condition holds, with a count limit to stop a loop. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.
- **B:** Incorrect for this question. A scope groups steps so a single run-after configuration can catch any failure inside it. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.
- **C:** Correct. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. In this case: Do until repeats until the condition holds, with a count limit to stop a loop.
- **D:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.

### Question 59 — D

Answer: Loop until the record is found with no exit limit. A loop with no bound can consume the flow's quota. A loop with no bound can run until the run timeout, consuming the flow's quota. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **D:** Correct. A loop with no bound can run until the run timeout, consuming the flow's quota. In this case: A loop with no bound can consume the flow's quota.

### Question 60 — C

Answer: Read the run history to find the failed action and its inputs. The run history shows each action's inputs and outputs. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **B:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **C:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows each action's inputs and outputs.
- **D:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: The run history shows each action's inputs and outputs.

### Question 61 — D

Answer: Resubmit the failed run after the fix. Resubmit replays the same inputs, so it is safe only when the actions are idempotent. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: Resubmit replays the same inputs, so it is safe only when the actions are idempotent.
- **B:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: Resubmit replays the same inputs, so it is safe only when the actions are idempotent.
- **C:** Incorrect for this question. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Why the correct answer wins: Resubmit replays the same inputs, so it is safe only when the actions are idempotent.
- **D:** Correct. Resubmit replays the same inputs, which is safe only when the actions are idempotent. In this case: Resubmit replays the same inputs, so it is safe only when the actions are idempotent.

### Question 62 — D

Answer: Build the prompt from blank. A blank prompt is right when no template covers the task. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **D:** Correct. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. In this case: A blank prompt is right when no template covers the task.

### Question 63 — B

Answer: Add typed inputs so the prompt takes values. Typed inputs become the parameters an app or flow supplies. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **B:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Typed inputs become the parameters an app or flow supplies.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **D:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.

### Question 64 — A

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in approved documents. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in approved documents.
- **B:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **D:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.

### Question 65 — A, E

Answers: Add the knowledge source so the prompt grounds on approved content; Add typed inputs so the prompt takes values. Knowledge grounds the answer, and inputs are the parameters. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Knowledge grounds the answer, and inputs are the parameters.
- **B:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Knowledge grounds the answer, and inputs are the parameters.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge grounds the answer, and inputs are the parameters.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge grounds the answer, and inputs are the parameters.
- **E:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge grounds the answer, and inputs are the parameters.

### Question 66 — B

Answer: Choose the model that fits the task instead of the largest available. Matching the model to the task controls cost. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Matching the model to the task controls cost.
- **B:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Matching the model to the task controls cost.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Matching the model to the task controls cost.
- **D:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Matching the model to the task controls cost.

### Question 67 — C

Answer: Copy the prompt text into each app so it can be tuned per app. Copied prompt text drifts, so the same question gets different answers. Copied prompt text drifts, so the same question gets different answers in different apps. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.
- **B:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.
- **C:** Correct. Copied prompt text drifts, so the same question gets different answers in different apps. In this case: Copied prompt text drifts, so the same question gets different answers.
- **D:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.

### Question 68 — C

Answer: Call the prompt from the canvas app through its connector. Consuming the published prompt keeps one instruction behind the app. Consuming the published prompt keeps one instruction and one model choice behind every app. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **B:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **C:** Correct. Consuming the published prompt keeps one instruction and one model choice behind every app. In this case: Consuming the published prompt keeps one instruction behind the app.
- **D:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.

### Question 69 — D

Answer: Consume the AI Hub model through the same connector pattern as a prompt. Consuming the model through the connector keeps authentication governed. A model consumed this way keeps authentication and throttling in one governed place. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Storing the result on the record is what makes the model output visible to the process and the audit. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.
- **B:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.
- **D:** Correct. A model consumed this way keeps authentication and throttling in one governed place. In this case: Consuming the model through the connector keeps authentication governed.

### Question 70 — D

Answer: Configure a business rule on the table. A business rule enforces a condition or required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **B:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **C:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **D:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a condition or required field without code.

### Question 71 — D

Answer: Set the business rule scope to the table so it applies in every form. Table scope makes the rule apply to imports and flows. Table scope is what makes the rule hold for imports and flows as well as the main form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: Table scope makes the rule apply to imports and flows.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: Table scope makes the rule apply to imports and flows.
- **C:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: Table scope makes the rule apply to imports and flows.
- **D:** Correct. Table scope is what makes the rule hold for imports and flows as well as the main form. In this case: Table scope makes the rule apply to imports and flows.

### Question 72 — A

Answer: Model the stages in a business process flow. A business process flow guides a record through stages. A business process flow guides a record through stages and pins the fields each stage needs. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A business process flow guides a record through stages and pins the fields each stage needs. In this case: A business process flow guides a record through stages.
- **B:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A business process flow guides a record through stages.
- **C:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A business process flow guides a record through stages.
- **D:** Incorrect for this question. A branch lets one process cover two variants without a second process and a duplicate set of stages. Why the correct answer wins: A business process flow guides a record through stages.

### Question 73 — C

Answer: Use a formula column where the rule needs Power Fx. A formula column evaluates a Power Fx expression. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **B:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **C:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column evaluates a Power Fx expression.
- **D:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A formula column evaluates a Power Fx expression.

### Question 74 — C

Answer: Write a plug-in to set the value on every update. A plug-in runs inside the save, so no caller can bypass it. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A plug-in runs inside the save, so no caller can bypass it.
- **B:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A plug-in runs inside the save, so no caller can bypass it.
- **C:** Correct. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. In this case: A plug-in runs inside the save, so no caller can bypass it.
- **D:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A plug-in runs inside the save, so no caller can bypass it.

### Question 75 — B

Answer: Enforce the rule in a synchronous plug-in when it must run on every write. A synchronous plug-in runs inside the save. A synchronous plug-in runs inside the save, so no caller can bypass it. Local study-map skill 3.14 (Choosing the Right Business Logic), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A synchronous plug-in runs inside the save.
- **B:** Correct. A synchronous plug-in runs inside the save, so no caller can bypass it. In this case: A synchronous plug-in runs inside the save.
- **C:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A synchronous plug-in runs inside the save.
- **D:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A synchronous plug-in runs inside the save.

### Question 76 — D, E

Answers: Use an automated trigger on record creation; Trigger when a chosen column changes, with a filter condition. The automated trigger starts the run, and the filter stops irrelevant updates. An automated trigger runs without a user, which is what a background rule needs. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **B:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **C:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **D:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.
- **E:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.

### Question 77 — C, D

Answers: Start and wait for an approval; Choose the approval type that matches the sign-off the process requires. The approval action pauses the run, and the type encodes who must respond. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **B:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **C:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: The approval action pauses the run, and the type encodes who must respond.
- **D:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run, and the type encodes who must respond.
- **E:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.

### Question 78 — A, B

Answers: Wrap the steps in a Scope so one error path handles the failures; Configure run after so the failure path actually executes. A scope groups the steps, and run after makes the failure branch execute. A scope groups steps so a single run-after configuration can catch any failure inside it. By default a step runs only on success, so the failure branch never fires without this setting. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. By default a step runs only on success, so the failure branch never fires without this setting. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **B:** Correct. A scope groups steps so a single run-after configuration can catch any failure inside it. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **C:** Incorrect for this question. Concurrency runs iterations in parallel, which is faster but reorders side effects. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **D:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **E:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.

### Question 79 — A, E

Answers: Read the run history to find the failed action and its inputs; Test the flow with the real trigger payload. The run history shows the wrong value, and a real payload proves the fix. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows the wrong value, and a real payload proves the fix.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **C:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **D:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **E:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: The run history shows the wrong value, and a real payload proves the fix.

### Question 80 — C, D

Answers: Start from a prompt template in AI Hub; Choose the model that fits the task instead of the largest available. The template supplies the instruction, and the model choice controls cost. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: The template supplies the instruction, and the model choice controls cost.
- **B:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: The template supplies the instruction, and the model choice controls cost.
- **C:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: The template supplies the instruction, and the model choice controls cost.
- **D:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: The template supplies the instruction, and the model choice controls cost.
- **E:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: The template supplies the instruction, and the model choice controls cost.

### Question 81 — D, E

Answers: Configure a business rule on the table; Enforce the rule in a synchronous plug-in when it must run on every write. A table-scope business rule covers imports, and a synchronous plug-in runs inside the save. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. A synchronous plug-in runs inside the save, so no caller can bypass it. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **C:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **D:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **E:** Correct. A synchronous plug-in runs inside the save, so no caller can bypass it. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.

### Question 82 — D, E

Answers: Use a formula column where the rule needs Power Fx; Use a rollup column to aggregate the child records. A formula column recalculates, and a rollup aggregates children. A formula column evaluates a Power Fx expression, which is the current way to express derived values. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **B:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **C:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **D:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A formula column recalculates, and a rollup aggregates children.
- **E:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column recalculates, and a rollup aggregates children.

### Question 83 — D

Answer: Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run. The event decides the trigger, and the real payload decides whether the expressions resolve. The event decides the trigger, and the payload decides whether the expressions actually resolve. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A run history only exists after a run has happened. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **B:** Incorrect for this question. There is no payload to test until a trigger and actions exist. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **C:** Incorrect for this question. Actions placed before the trigger cannot know what data they receive. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **D:** Correct. The event decides the trigger, and the payload decides whether the expressions actually resolve. In this case: The event decides the trigger, and the real payload decides whether the expressions resolve.

### Question 84 — D

Answer: Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester. The branch reads the approval outcome, and the record update carries the decision. The branch reads the approval outcome, and the record update carries the decision. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A branch with no outcome yet has nothing to evaluate. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **B:** Incorrect for this question. Notifying first tells the requester about a decision that does not exist. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **C:** Incorrect for this question. The record cannot be updated with a decision that has not been taken. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **D:** Correct. The branch reads the approval outcome, and the record update carries the decision. In this case: The branch reads the approval outcome, and the record update carries the decision.

### Question 85 — D

Answer: Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run. The run history turns a symptom into a specific wrong value. The run history is what turns a symptom into a specific wrong value. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. There is no run to inspect until the failure is reproduced. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **B:** Incorrect for this question. A fix applied before diagnosis is a guess. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **C:** Incorrect for this question. Resubmitting an unfixed flow repeats the same failure. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **D:** Correct. The run history is what turns a symptom into a specific wrong value. In this case: The run history turns a symptom into a specific wrong value.

### Question 86 — C

Answer: Decide whether the value is derived at read time or aggregated from children → add the column of the matching type → configure the formula or the rollup → verify the recalculation on a test record → surface the column on the form and view. The read-time versus aggregate decision chooses the column type before anything is configured. The read-time versus aggregate decision is what chooses between a formula column and a rollup. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A formula cannot be configured before the column exists. Why the correct answer wins: The read-time versus aggregate decision chooses the column type before anything is configured.
- **B:** Incorrect for this question. The form is the last step, not the first. Why the correct answer wins: The read-time versus aggregate decision chooses the column type before anything is configured.
- **C:** Correct. The read-time versus aggregate decision is what chooses between a formula column and a rollup. In this case: The read-time versus aggregate decision chooses the column type before anything is configured.
- **D:** Incorrect for this question. Verification is the check on a configured column, not a step before it. Why the correct answer wins: The read-time versus aggregate decision chooses the column type before anything is configured.

### Question 87 — C, D

Answers: Publish a component library for the shared header and controls; Define a named formula for the shared calculation. The library shares the control, and the named formula shares the calculation. A component library is the reusable, versioned home for a control that several apps must share. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **C:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: The library shares the control, and the named formula shares the calculation.
- **D:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: The library shares the control, and the named formula shares the calculation.
- **E:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.

### Question 88 — D, E

Answers: Use a global variable for the value that the whole app needs; Wrap the call in IfError and surface the message to the user. A global variable persists, and IfError handles the failure. A global variable persists across screens, which is what a signed-in user's selection needs. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **B:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **C:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **D:** Correct. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. In this case: A global variable persists, and IfError handles the failure.
- **E:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists, and IfError handles the failure.

### Question 89 — B

Answer: Define the solution publisher and prefix once, before the first table. The prefix is baked into every schema name. The prefix is baked into every schema name and is expensive to change after data exists. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: The prefix is baked into every schema name.
- **B:** Correct. The prefix is baked into every schema name and is expensive to change after data exists. In this case: The prefix is baked into every schema name.
- **C:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: The prefix is baked into every schema name.
- **D:** Incorrect for this question. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. Why the correct answer wins: The prefix is baked into every schema name.

### Question 90 — A

Answer: Use the phone layout for field staff. The phone layout controls size and reach on a handheld. The phone layout controls the size and reach of controls on a handheld device. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The phone layout controls the size and reach of controls on a handheld device. In this case: The phone layout controls size and reach on a handheld.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **C:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **D:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: The phone layout controls size and reach on a handheld.

### Question 91 — D

Answer: Use the premium connector the source requires. A premium connector is justified when no standard connector reaches the data. A premium connector is justified when the data lives where no standard connector reaches. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.
- **B:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.
- **C:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: A premium connector is justified when no standard connector reaches the data.
- **D:** Correct. A premium connector is justified when the data lives where no standard connector reaches. In this case: A premium connector is justified when no standard connector reaches the data.

### Question 92 — B

Answer: Use a global variable for the value that the whole app needs. A global variable persists across screens. A global variable persists across screens, which is what a signed-in user's selection needs. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An un-cleared collection keeps the previous user's rows in memory. Why the correct answer wins: A global variable persists across screens.
- **B:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists across screens.
- **C:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists across screens.
- **D:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists across screens.

### Question 93 — A

Answer: Start and wait for an approval. The approval action pauses the run and resumes with the outcome. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run and resumes with the outcome.
- **B:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **C:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **D:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.

### Question 94 — B

Answer: Trigger when a chosen column changes, with a filter condition. A column filter stops irrelevant updates from starting the flow. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: A column filter stops irrelevant updates from starting the flow.
- **B:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: A column filter stops irrelevant updates from starting the flow.
- **C:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A column filter stops irrelevant updates from starting the flow.
- **D:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: A column filter stops irrelevant updates from starting the flow.

### Question 95 — C

Answer: Configure a prompt column to generate text per row. A prompt column generates a value per row. A prompt column produces a value for each record from a prompt, without a separate flow. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A prompt column generates a value per row.
- **B:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A prompt column generates a value per row.
- **C:** Correct. A prompt column produces a value for each record from a prompt, without a separate flow. In this case: A prompt column generates a value per row.
- **D:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: A prompt column generates a value per row.

### Question 96 — C

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A form carries the working set of fields for the role.
- **C:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 97 — D

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in the source document. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in the source document.
- **B:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in the source document.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in the source document.
- **D:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in the source document.

### Question 98 — A

Answer: Assign the record to a team that the group owns. Team ownership shares one queue without granting each owner-level access. Team ownership shares one queue of records without granting each member the owner role. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Team ownership shares one queue of records without granting each member the owner role. In this case: Team ownership shares one queue without granting each owner-level access.
- **B:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: Team ownership shares one queue without granting each owner-level access.
- **C:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: Team ownership shares one queue without granting each owner-level access.
- **D:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: Team ownership shares one queue without granting each owner-level access.

### Question 99 — D

Answer: Filter the view on the columns the team actually searches. The filter decides which records are in the list. The filter decides which records appear, so it must match the question the list answers. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides which records are in the list.
- **B:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides which records are in the list.
- **C:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The filter decides which records are in the list.
- **D:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides which records are in the list.

### Question 100 — C

Answer: Configure a business rule on the table. A business rule enforces a required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A business rule enforces a required field without code.
- **B:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a required field without code.
- **C:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a required field without code.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a required field without code.

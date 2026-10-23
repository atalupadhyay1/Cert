# Microsoft AB-410 — Full-Length Mock Exam 6

Intelligent Applications Builder Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the maker portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A group requirement spans an order app, an approval chain, a quote document, and a dashboard. What should be decided first?

Domain: Create a foundation for intelligent applications

- A. Build a working prototype in a week and let the business react to it
- B. Start with a custom connector and a plug-in for the first version
- C. Map each requirement to the Power Platform component that fits it
- D. Deliver every requirement as a single model-driven app

### 2. A discount approval must follow the same path every time. What should be used?

Domain: Create a foundation for intelligent applications

- A. Build a custom Copilot Studio agent for every requirement
- B. Build a working prototype in a week and let the business react to it
- C. Model the process as a cloud flow with no agent at all
- D. Adopt the built-in agent that already covers the task

### 3. Sales wants a helper that answers questions about orders. What should be evaluated first?

Domain: Create a foundation for intelligent applications

- A. Model the process as a cloud flow with no agent at all
- B. Build a Power Apps component framework control
- C. Build a custom Copilot Studio agent for every requirement
- D. Adopt the built-in agent that already covers the task

### 4. The built-in agent cannot reach the order data. What justifies a custom agent?

Domain: Create a foundation for intelligent applications

- A. Model the process as a cloud flow with no agent at all
- B. Build a custom Copilot Studio agent for every requirement
- C. Write a Dataverse plug-in in C#
- D. Adopt the built-in agent that already covers the task

### 5. A group solution must sit in its own governed boundary. What decides the environment?

Domain: Create a foundation for intelligent applications

- A. Build in the default environment because everyone already has access
- B. Choose the environment type that matches the data boundary and the licence
- C. Share a single environment between development and production
- D. Use the trial environment for production after the pilot

### 6. A release must be removable if a subsidiary rejects it. What should be imported into production?

Domain: Create a foundation for intelligent applications

- A. Clone the environment each time instead of using a pipeline
- B. Promote a managed solution to test and production
- C. Import unmanaged customizations directly into production
- D. Do all building in the production environment to avoid deployment

### 7. A component behaves unexpectedly after an import. What should be reviewed first?

Domain: Create a foundation for intelligent applications

- A. Review the solution layers before overwriting a component
- B. Clone the environment each time instead of using a pipeline
- C. Import unmanaged customizations directly into production
- D. Delete the managed solution to clear a component conflict

### 8. A group solution must carry a stable prefix and move as one package. Which two practices apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Automate export and import with an Azure DevOps pipeline
- B. Define the solution publisher and prefix once, before the first table
- C. Clone the environment each time instead of using a pipeline
- D. Package the customizations in a solution before moving them
- E. Import unmanaged customizations directly into production

### 9. A group order entity has no standard equivalent. Where should it be modelled?

Domain: Create a foundation for intelligent applications

- A. Store the interactions in the Activity table
- B. Extend the standard table instead of creating a duplicate
- C. Keep the records in a SharePoint list and skip Dataverse
- D. Create the table in the Dataverse data workspace

### 10. Calls, emails, and visits must appear on one timeline per order. Which table fits?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Create a custom table for the new business entity
- C. Store the account name as text so the form stays simple
- D. Store the interactions in the Activity table

### 11. An order must be owned by a team and keep its history. What decides that?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Configure a row summary to summarize the record text
- C. Enable auditing on the tables that hold regulated data
- D. Configure table properties such as ownership and auditing

### 12. Order types must be identical in the order and quote tables. What should be used?

Domain: Create a foundation for intelligent applications

- A. Store the account name as text so the form stays simple
- B. Use a global choice so several tables share one option list
- C. Use a lookup column instead of storing the name as text
- D. Add a choice column for the fixed set of options

### 13. Every order needs a reference the customer can quote. What should be used?

Domain: Create a foundation for intelligent applications

- A. Use a currency column with the record currency
- B. Store the account name as text so the form stays simple
- C. Use a calculated column for the value that must never change
- D. Use an auto-number column for the case identifier

### 14. A field must accept approved values and point at the account record. Which two column types apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Add a choice column for the fixed set of options
- B. Use a calculated column for the value that must never change
- C. Store the account name as text so the form stays simple
- D. Use a currency column with the record currency
- E. Use a lookup column instead of storing the name as text

### 15. An order has many lines and each line belongs to one order. How should that be modelled?

Domain: Create a foundation for intelligent applications

- A. Model the many-to-many link with a native N:N relationship
- B. Keep the relationship referential so child records survive the parent delete
- C. Configure a one-to-many relationship with a lookup on the child table
- D. Set the relationship behaviour to parental so child records are removed with the parent

### 16. Each order needs an AI summary of its change history. What should be configured?

Domain: Create a foundation for intelligent applications

- A. Use a calculated column for the value that must never change
- B. Configure a prompt column to generate text per row
- C. Configure a row summary to summarize the record text
- D. Add a JavaScript web resource to the form

### 17. A supervisor recap must condense the record's own notes. What should be configured?

Domain: Create a foundation for intelligent applications

- A. Use a calculated column for the value that must never change
- B. Configure a row summary to summarize the record text
- C. Configure a prompt column to generate text per row
- D. Configure a business rule on the table

### 18. An order needs an AI summary per row and a condensed recap. Which two features apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Use a formula column where the rule needs Power Fx
- B. Configure a prompt column to generate text per row
- C. Use a calculated column for the value that must never change
- D. Configure a row summary to summarize the record text
- E. Add a JavaScript web resource to the form

### 19. Every unit must see the same list of orders awaiting approval. What should be created?

Domain: Create a foundation for intelligent applications

- A. Rely on each user's personal view of the table
- B. Create a public view for the shared filtered list
- C. Change the system view so the list order suits the team
- D. Design the main form around the record the user opens

### 20. A maker edits the system view to reorder columns for one unit. What is the risk?

Domain: Create a foundation for intelligent applications

- A. Create a public view for the shared filtered list
- B. Change the system view so the list order suits the team
- C. Rely on each user's personal view of the table
- D. Design the main form around the record the user opens

### 21. A unit manager may see only their unit's orders. What grants that?

Domain: Create a foundation for intelligent applications

- A. Assign the record to a team that the group owns
- B. Use a field security profile for the sensitive column
- C. Move the user to another business unit to fix access
- D. Assign a security role that grants only the privileges the role needs

### 22. A cost column must stay hidden from sales while the order stays visible. What should be used?

Domain: Create a foundation for intelligent applications

- A. Use a field security profile for the sensitive column
- B. Assign the record to a team that the group owns
- C. Assign a security role that grants only the privileges the role needs
- D. Move the user to another business unit to fix access

### 23. A vendor may read orders but must never read the margin column. Which two controls apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Use a field security profile for the sensitive column
- B. Assign a security role that grants only the privileges the role needs
- C. Move the user to another business unit to fix access
- D. Create a public view for the shared filtered list
- E. Assign the record to a team that the group owns

### 24. A group must decide whether an agent is worth building. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it
- B. Build a custom agent → map the requirement to a component → pilot in development → measure the outcome → check built-in coverage
- C. Check whether a built-in agent covers it → build a custom agent → adopt it in production → map the requirement to a component → pilot in development
- D. Measure the outcome → pilot the agent in development → build a custom agent → map the requirement to a component → check built-in coverage

### 25. A group solution must reach the right boundary under control. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Choose the environment type → deploy through the pipeline → identify the data boundary → create the solution with its publisher
- B. Deploy through the pipeline → create the solution with its publisher → choose the environment type → identify the data boundary
- C. Create the solution with its publisher → deploy through the pipeline → identify the data boundary → choose the environment type
- D. Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline

### 26. An order form carries fifty columns and the team uses ten. What should change?

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Add the columns the role uses to the main form
- C. Choose the view columns before setting the filter
- D. Hide the field with a JavaScript web resource

### 27. A field must be hidden only on the sales form. What should be used?

Domain: Create intelligent applications

- A. Write a Dataverse plug-in in C#
- B. Configure a business rule on the table
- C. Hide the field with a JavaScript web resource
- D. Organize the long form into tabs and sections

### 28. A queue must show only orders awaiting approval this week. What decides that?

Domain: Create intelligent applications

- A. Filter the view on the columns the team actually searches
- B. Choose the view columns before setting the filter
- C. Create a public view for the shared filtered list
- D. Write FetchXML for the view to get the exact rows

### 29. A queue must be readable at a glance. What must be chosen first?

Domain: Create intelligent applications

- A. Write FetchXML for the view to get the exact rows
- B. Filter the view on the columns the team actually searches
- C. Create a public view for the shared filtered list
- D. Choose the view columns before setting the filter

### 30. A queue must show the right orders and be readable at a glance. Which two choices apply? Select two.

Domain: Create intelligent applications

- A. Filter the view on the columns the team actually searches
- B. Write FetchXML for the view to get the exact rows
- C. Choose the view columns before setting the filter
- D. Create a public view for the shared filtered list
- E. Rely on each user's personal view of the table

### 31. A unit wants a first draft of a page for a brand-new product line. What should be created?

Domain: Create intelligent applications

- A. Publish the generated page without reviewing its data bindings
- B. Organize the long form into tabs and sections
- C. Generate the page from a natural-language description, then refine it
- D. Replace the main form with the generated page

### 32. A generated page shows a cost column the audience should not read. What was missed?

Domain: Create intelligent applications

- A. Publish the generated page without reviewing its data bindings
- B. Hide the field with a JavaScript web resource
- C. Generate the page from a natural-language description, then refine it
- D. Replace the main form with the generated page

### 33. The order app must expose four forms and three views. What decides that?

Domain: Create intelligent applications

- A. Configure the navigation in the sitemap designer
- B. Share the app only and rely on the app for access
- C. Share the app and assign the security role that backs it
- D. Add the forms, views, and pages to the app in the app designer

### 34. Users cannot find the approval area anywhere in the app. What should be configured?

Domain: Create intelligent applications

- A. Add the forms, views, and pages to the app in the app designer
- B. Share the app and assign the security role that backs it
- C. Configure the navigation in the sitemap designer
- D. Share the app only and rely on the app for access

### 35. A director wants the trend, the queue, and the count on one page. What should be assembled?

Domain: Create intelligent applications

- A. Build the chart in Power BI and embed it
- B. Create the chart on the view for the trend
- C. Add the chart and the views to a dashboard
- D. Filter the view on the columns the team actually searches

### 36. A field app must exist over two tables by Friday. What should the maker do first?

Domain: Create intelligent applications

- A. Write the filter so the data source performs the delegation
- B. Generate a canvas app from the data source
- C. Use the tablet layout for desk-based users
- D. Use the phone layout for field staff

### 37. A field app must handle a large table and fit a phone and a tablet. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Write the filter so the data source performs the delegation
- B. Use responsive containers so the layout adapts to the device
- C. Fix the layout to one pixel width so it always looks the same
- D. Collect the rows into a collection for in-memory work
- E. Filter in Power Fx after loading the rows into the app

### 38. Field staff use phones while the office uses laptops, with one app for both. What should be used?

Domain: Create intelligent applications

- A. Use the phone layout for field staff
- B. Fix the layout to one pixel width so it always looks the same
- C. Use responsive containers so the layout adapts to the device
- D. Use the tablet layout for desk-based users

### 39. The same order-value calculation appears on four screens. What should be used?

Domain: Create intelligent applications

- A. Define a named formula for the shared calculation
- B. Create a user-defined function for the reused expression
- C. Publish a component library for the shared header and controls
- D. Copy the screen into every app that needs it

### 40. Three apps must share one group header. What should be used?

Domain: Create intelligent applications

- A. Create a user-defined function for the reused expression
- B. Copy the screen into every app that needs it
- C. Define a named formula for the shared calculation
- D. Publish a component library for the shared header and controls

### 41. Two apps must share a header control and one pricing formula. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Define a named formula for the shared calculation
- B. Copy the screen into every app that needs it
- C. Create a user-defined function for the reused expression
- D. Publish a component library for the shared header and controls
- E. Fix the layout to one pixel width so it always looks the same

### 42. An order save can fail on a timeout and the user sees nothing. What should be added?

Domain: Create intelligent applications

- A. Wrap the call in IfError and surface the message to the user
- B. Write a Trace message for the support team
- C. Run the app in Test Studio before publishing
- D. Use Monitor to inspect the network call and the formula that fired

### 43. A previous user's orders remain visible after a handover. What must be added?

Domain: Create intelligent applications

- A. Collect the rows into a collection for in-memory work
- B. Use a context variable scoped to the screen
- C. Clear the collection when the screen changes
- D. Use a global variable for the value that the whole app needs

### 44. A chosen unit must persist across screens and failures must be recoverable. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Use a global variable for the value that the whole app needs
- B. Write a Trace message for the support team
- C. Wrap the call in IfError and surface the message to the user
- D. Use a context variable scoped to the screen
- E. Collect the rows into a collection for in-memory work

### 45. A change to the order screen must not break the existing flow. What should be run first?

Domain: Create intelligent applications

- A. Write a Trace message for the support team
- B. Run the app in Test Studio before publishing
- C. Use Monitor to inspect the network call and the formula that fired
- D. Wrap the call in IfError and surface the message to the user

### 46. An account manager wants to ask about an order inside the app. What should be added?

Domain: Create intelligent applications

- A. Build a second canvas app just to host the agent
- B. Add the Copilot Studio agent to the canvas app as a component
- C. Build a custom Copilot Studio agent for every requirement
- D. Call the agent's endpoint directly from Power Fx

### 47. An order app must be composed and released to the units. Which sequence is correct?

Domain: Create intelligent applications

- A. Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role
- B. Assign the backing security role → configure the forms and views → set the navigation → compose the app → share the app
- C. Share the app → assign the backing security role → configure the forms and views → compose the app → set the navigation
- D. Set the navigation in the sitemap → share the app → configure the forms and views → compose the app → assign the role

### 48. A group wants an agent answering order questions inside its app. Which sequence is correct?

Domain: Create intelligent applications

- A. Configure the agent topics → publish → build the canvas app → add the agent as a component → test the conversation
- B. Add the agent as a component → build the canvas app → publish → configure the agent topics → test the conversation
- C. Build the canvas app → add the Copilot Studio agent as a component → configure the agent topics and knowledge → test the conversation in the app → publish
- D. Test the conversation in the app → add the agent as a component → build the canvas app → configure the agent topics → publish

### 49. A new order must start the approval chain the moment it is submitted. What should be used?

Domain: Build business application logic and automation

- A. Expose an HTTP request trigger with a signed URL
- B. Use a manually triggered flow from the app
- C. Use an automated trigger on record creation
- D. Use a scheduled trigger for the nightly batch

### 50. A manager decides when to escalate a stuck order. What should be used?

Domain: Build business application logic and automation

- A. Expose an HTTP request trigger with a signed URL
- B. Use a manually triggered flow from the app
- C. Use a scheduled trigger for the nightly batch
- D. Use an automated trigger on record creation

### 51. A flow must run only when the order status becomes approved. What should be used?

Domain: Build business application logic and automation

- A. Use an automated trigger on record creation
- B. Trigger when a chosen column changes, with a filter condition
- C. Trigger on every update so nothing is missed
- D. Expose an HTTP request trigger with a signed URL

### 52. The flow reads and writes Dataverse orders. Which connector fits?

Domain: Build business application logic and automation

- A. Build a custom connector for the internal API
- B. Use the premium connector the source requires
- C. Copy the data into Excel to avoid a premium connector
- D. Use the standard Dataverse connector

### 53. A subsidiary exposes an API with its own authentication. What should be built?

Domain: Build business application logic and automation

- A. Copy the data into Excel to avoid a premium connector
- B. Use the premium connector the source requires
- C. Use the standard Dataverse connector
- D. Build a custom connector for the internal API

### 54. An order above 50,000 needs the unit lead and then the group director. What should be built?

Domain: Build business application logic and automation

- A. Choose the approval type that matches the sign-off the process requires
- B. Chain two approvals in sequence for the second-level sign-off
- C. Send parallel approvals and require every response
- D. Send an email and treat silence as approval

### 55. The finance lead and the operations lead must both approve. What should be configured?

Domain: Build business application logic and automation

- A. Send an email and treat silence as approval
- B. Send parallel approvals and require every response
- C. Choose the approval type that matches the sign-off the process requires
- D. Start and wait for an approval

### 56. A returned body is opaque and the designer offers no properties. What should be added?

Domain: Build business application logic and automation

- A. Parse JSON so later steps can use the fields
- B. Use Compose to shape the payload the next step consumes
- C. Add a condition to branch on the status
- D. Apply to each over the returned rows

### 57. A response contains sixty order lines that must each be updated. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Apply to each over the returned rows
- C. Use a switch for the multi-way branch
- D. Add a condition to branch on the status

### 58. A flow takes one of two paths based on the order value. What should be used?

Domain: Build business application logic and automation

- A. Apply to each over the returned rows
- B. Use Do until with a bounded count for the retry loop
- C. Use a switch for the multi-way branch
- D. Add a condition to branch on the status

### 59. A call to a slow subsidiary service may need three attempts. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Use a switch for the multi-way branch
- C. Loop until the record is found with no exit limit
- D. Add a condition to branch on the status

### 60. The flow's error text is generic and no field is named. What exposes the input that failed?

Domain: Build business application logic and automation

- A. Test the flow with the real trigger payload
- B. Turn on static result to test the rest of the flow
- C. Resubmit the failed run after the fix
- D. Read the run history to find the failed action and its inputs

### 61. A new approval flow must be proven with the real trigger payload. What should be done?

Domain: Build business application logic and automation

- A. Read the run history to find the failed action and its inputs
- B. Turn on static result to test the rest of the flow
- C. Resubmit the failed run after the fix
- D. Test the flow with the real trigger payload

### 62. An order summary prompt must start from a tested instruction. What should be used?

Domain: Build business application logic and automation

- A. Build the prompt from blank
- B. Copy the prompt text into each app so it can be tuned per app
- C. Start from a prompt template in AI Hub
- D. Add typed inputs so the prompt takes values

### 63. A novel task has no template and the instruction must be written. What should be done?

Domain: Build business application logic and automation

- A. Start from a prompt template in AI Hub
- B. Add typed inputs so the prompt takes values
- C. Build the prompt from blank
- D. Copy the prompt text into each app so it can be tuned per app

### 64. A prompt must be filled with the current order total on every call. What should be added?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Add the knowledge source so the prompt grounds on approved content
- C. Copy the prompt text into each app so it can be tuned per app
- D. Choose the model that fits the task instead of the largest available

### 65. A summary must cite the approved order policy. What should be attached?

Domain: Build business application logic and automation

- A. Add the knowledge source so the prompt grounds on approved content
- B. Add typed inputs so the prompt takes values
- C. Choose the model that fits the task instead of the largest available
- D. Copy the prompt text into each app so it can be tuned per app

### 66. A summarisation prompt is overspecified for its task and costly to run. What should change?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Choose the model that fits the task instead of the largest available
- C. Add the knowledge source so the prompt grounds on approved content
- D. Copy the prompt text into each app so it can be tuned per app

### 67. The summary instruction is pasted into each app to tune it separately. What is the objection?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Call the prompt from the cloud flow action
- C. Start from a prompt template in AI Hub
- D. Call the prompt from the canvas app through its connector

### 68. An account manager must generate the summary while looking at the order. What should be used?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Choose the model that fits the task instead of the largest available
- C. Call the prompt from the canvas app through its connector
- D. Call the prompt from the cloud flow action

### 69. A recap must be produced inside a scheduled flow and stored on the record. What should be used?

Domain: Build business application logic and automation

- A. Call the prompt from the cloud flow action
- B. Add typed inputs so the prompt takes values
- C. Copy the prompt text into each app so it can be tuned per app
- D. Call the prompt from the canvas app through its connector

### 70. A reason must be captured whenever a line discount is applied. What should be configured?

Domain: Build business application logic and automation

- A. Set the business rule scope to the table so it applies in every form
- B. Hide the field with a JavaScript web resource
- C. Add a JavaScript web resource to the form
- D. Configure a business rule on the table

### 71. A validation rule is bypassed when records are loaded by a data migration. What should change?

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Write a Dataverse plug-in in C#
- C. Set the business rule scope to the table so it applies in every form
- D. Hide the field with a JavaScript web resource

### 72. An order must move through five ordered stages with required information. What should be built?

Domain: Build business application logic and automation

- A. Branch the business process flow on the case type
- B. Model the stages in a business process flow
- C. Use a rollup column to aggregate the child records
- D. Configure a business rule on the table

### 73. Two order types need different stages after the first. What should be used?

Domain: Build business application logic and automation

- A. Use a formula column where the rule needs Power Fx
- B. Model the stages in a business process flow
- C. Branch the business process flow on the case type
- D. Keep every case type in one linear process to stay simple

### 74. An order margin must recalculate from two columns. What should be used?

Domain: Build business application logic and automation

- A. Write a plug-in to set the value on every update
- B. Use a formula column where the rule needs Power Fx
- C. Use a calculated column for the value that must never change
- D. Use a rollup column to aggregate the child records

### 75. An account needs a running total of open order value. What should be used?

Domain: Build business application logic and automation

- A. Write a plug-in to set the value on every update
- B. Use a formula column where the rule needs Power Fx
- C. Use a rollup column to aggregate the child records
- D. Use a calculated column for the value that must never change

### 76. Some logic must run only on a form, some on every write, and some at read time. What settles the choice?

Domain: Build business application logic and automation

- A. Enforce the rule in a synchronous plug-in when it must run on every write
- B. Use a formula column where the rule needs Power Fx
- C. Pick the logic mechanism that matches where the rule must hold
- D. Configure a business rule on the table

### 77. A flow must start on a new order but only for orders above the threshold. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Use an automated trigger on record creation
- C. Trigger on every update so nothing is missed
- D. Expose an HTTP request trigger with a signed URL
- E. Trigger when a chosen column changes, with a filter condition

### 78. A release sign-off must pause the process and match the approval rule. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Start and wait for an approval
- B. Choose the approval type that matches the sign-off the process requires
- C. Chain two approvals in sequence for the second-level sign-off
- D. Use a scheduled trigger for the nightly batch
- E. Send an email and treat silence as approval

### 79. Three dependent actions must share one failure path. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Add a condition to branch on the status
- B. Wrap the steps in a Scope so one error path handles the failures
- C. Turn on concurrency control for the loop
- D. Configure run after so the failure path actually executes
- E. Use a switch for the multi-way branch

### 80. A rejected order notification fails, and the corrected version must be proved. Which two practices apply? Select two.

Domain: Build business application logic and automation

- A. Test the flow with the real trigger payload
- B. Turn on static result to test the rest of the flow
- C. Read the run history to find the failed action and its inputs
- D. Resubmit the failed run after the fix
- E. Parse JSON so later steps can use the fields

### 81. A customer reply draft must follow a tested instruction and reference the policy. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Choose the model that fits the task instead of the largest available
- B. Start from a prompt template in AI Hub
- C. Add the knowledge source so the prompt grounds on approved content
- D. Copy the prompt text into each app so it can be tuned per app
- E. Build the prompt from blank

### 82. A prompt must accept the account name at run time and use a model chosen for cost. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Choose the model that fits the task instead of the largest available
- C. Start from a prompt template in AI Hub
- D. Add the knowledge source so the prompt grounds on approved content
- E. Add typed inputs so the prompt takes values

### 83. A guard must catch bad data entered on forms and data sent by the nightly integration. Which two mechanisms apply? Select two.

Domain: Build business application logic and automation

- A. Use a calculated column for the value that must never change
- B. Add a JavaScript web resource to the form
- C. Configure a business rule on the table
- D. Hide the field with a JavaScript web resource
- E. Enforce the rule in a synchronous plug-in when it must run on every write

### 84. A margin must recalculate and an account must show open order value. Which two column types apply? Select two.

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Use a formula column where the rule needs Power Fx
- C. Use a calculated column for the value that must never change
- D. Use a rollup column to aggregate the child records
- E. Write a plug-in to set the value on every update

### 85. An order approval workflow must reach production without wrong expressions. Which sequence is correct?

Domain: Build business application logic and automation

- A. Test with a real payload → decide which event starts the process → read the run history → add the trigger → add the actions
- B. Add the actions and branches → add the trigger → test with a real payload → decide which event starts the process → read the run history
- C. Read the run history → add the trigger → decide which event starts the process → add the actions → test with a real payload
- D. Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run

### 86. An order must be decided and the decision recorded. Which sequence is correct?

Domain: Build business application logic and automation

- A. Update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome → notify the requester
- B. Notify the requester → update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome
- C. Branch on the outcome → trigger on the submitted request → notify the requester → start and wait for the approval → update the record
- D. Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester

### 87. A failing order notification must be fixed with confidence. Which sequence is correct?

Domain: Build business application logic and automation

- A. Open the run history → resubmit the run → reproduce the failure → inspect the failing action → fix the expression
- B. Resubmit the run → open the run history → reproduce the failure → fix the expression → inspect the failing action
- C. Fix the expression → reproduce the failure → resubmit the run → inspect the failing action → open the run history
- D. Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run

### 88. An order process must guide users through five stages. Which sequence is correct?

Domain: Build business application logic and automation

- A. Branch the process → define the stages → hand the process to the users → test a record through every stage → choose the columns each stage requires
- B. Test a record through every stage → branch the process → define the stages → hand the process to the users → choose the columns
- C. Define the stages the record moves through → choose the columns each stage requires → branch the process where the case types diverge → test a record through every stage → hand the process to the users
- D. Choose the columns each stage requires → hand the process to the users → test a record → define the stages → branch the process

---

## Case study — Bellows College

Bellows College manages admissions for 18,000 applications a year across five faculties. Applications arrive through a portal as documents, and each faculty assesses with its own rubric. The registrar cannot produce a timely count of applications awaiting a decision. The college wants a reviewer app, a rubric per faculty, an approval when an offer is made below the published threshold, and a dashboard for the registrar. Applicant data is personal and must be visible only to the reviewing faculty. The college has Dataverse and Copilot Studio, and a policy that no AI may make an admission decision.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Applicant contacts must reuse the fields staff already know. What should be used?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Create a custom table for the new business entity
- C. Store the account name as text so the form stays simple
- D. Store the interactions in the Activity table

### 90. A rubric score calculation takes three inputs. What should be used?

Domain: Create intelligent applications

- A. Create a user-defined function for the reused expression
- B. Copy the screen into every app that needs it
- C. Define a named formula for the shared calculation
- D. Publish a component library for the shared header and controls

### 91. A rejection reason must be required before the decision saves. What should be configured?

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Use a calculated column for the value that must never change
- C. Add a JavaScript web resource to the form
- D. Set the business rule scope to the table so it applies in every form

---

## Case study — Munson Sporting Goods

Munson Sporting Goods sells team equipment to schools and clubs. Orders peak in August and January, and the current process is a shared mailbox monitored by four people. Quotes are built in a spreadsheet, and approvals happen in email threads that nobody can audit after the season. The company wants an order app, an approval chain that varies by order value, a quote document, and a seasonal dashboard. The finance director requires that every discount be attributable and that no order be fulfilled without an approved quote. The company has Dataverse and Power Apps per-app licences.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. A school district must not see another district's orders. What partitions the data?

Domain: Create a foundation for intelligent applications

- A. Move the user to another business unit to fix access
- B. Assign a security role that grants only the privileges the role needs
- C. Use a field security profile for the sensitive column
- D. Assign the record to a team that the group owns

### 93. A seasonal trend must reuse the existing view filter. What should be created?

Domain: Create intelligent applications

- A. Filter the view on the columns the team actually searches
- B. Add the chart and the views to a dashboard
- C. Build the chart in Power BI and embed it
- D. Create the chart on the view for the trend

### 94. A forecast model must be called from the flow and stored on the order. What should be used?

Domain: Build business application logic and automation

- A. Call the model from the flow and store the result on the record
- B. Consume the AI Hub model through the same connector pattern as a prompt
- C. Call the prompt from the canvas app through its connector
- D. Call the prompt from the cloud flow action

---

## Case study — Relecloud Telecom

Relecloud Telecom handles 30,000 service tickets a month. Field engineers record work on paper and call the dispatch desk when they finish, which delays the next job assignment. The company wants a field app that works offline, automatic dispatch of the next job, and a customer notification when an engineer is en route. Engineers must not see billing information. The company has premium connectors and a security team that reviews any connector that leaves the tenant.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A field app must search a large job table. What must the filter do?

Domain: Create intelligent applications

- A. Write the filter so the data source performs the delegation
- B. Filter in Power Fx after loading the rows into the app
- C. Collect the rows into a collection for in-memory work
- D. Generate a canvas app from the data source

### 96. Dispatchers want a daily board drafted from a description. What should be used?

Domain: Create intelligent applications

- A. Generate the page from a natural-language description, then refine it
- B. Organize the long form into tabs and sections
- C. Replace the main form with the generated page
- D. Publish the generated page without reviewing its data bindings

### 97. A response contains forty job rows to update individually. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Use a switch for the multi-way branch
- C. Add a condition to branch on the status
- D. Apply to each over the returned rows

---

## Case study — Tahoma Winery Group

Tahoma Winery Group owns four wineries and a distribution arm. Each winery tracks cellar operations in its own workbook, and the group cannot compare production across sites. The group wants a shared cellar-operations model, a winery app for cellar hands on tablets, an approval for any wine movement between sites, and a group dashboard. The wineries must not see each other's cost data. The group has Dataverse, a Power BI estate, and a governance policy that requires solutions to move through development, test, and production with an audited deployment.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Four wineries must deploy the same solution repeatably. What should be used?

Domain: Create a foundation for intelligent applications

- A. Use the trial environment for production after the pilot
- B. Automate export and import with an Azure DevOps pipeline
- C. Use Power Platform pipelines to deploy between environments
- D. Clone the environment each time instead of using a pipeline

### 99. Every cellar hand must see the same movement list. What should be created?

Domain: Create intelligent applications

- A. Change the system view so the list order suits the team
- B. Rely on each user's personal view of the table
- C. Create a public view for the shared filtered list
- D. Add a quick-create form for entry from a lookup

### 100. Moving wine between sites needs a recorded decision. What action fits?

Domain: Build business application logic and automation

- A. Chain two approvals in sequence for the second-level sign-off
- B. Start and wait for an approval
- C. Send an email and treat silence as approval
- D. Choose the approval type that matches the sign-off the process requires

---

## Answer key and explanations

### Question 1 — C

Answer: Map each requirement to the Power Platform component that fits it. Mapping requirements to components keeps the whole solution minimal. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: Mapping requirements to components keeps the whole solution minimal.
- **B:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: Mapping requirements to components keeps the whole solution minimal.
- **C:** Correct. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. In this case: Mapping requirements to components keeps the whole solution minimal.
- **D:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: Mapping requirements to components keeps the whole solution minimal.

### Question 2 — C

Answer: Model the process as a cloud flow with no agent at all. A deterministic process belongs in a flow. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A deterministic process belongs in a flow.
- **B:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: A deterministic process belongs in a flow.
- **C:** Correct. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. In this case: A deterministic process belongs in a flow.
- **D:** Incorrect for this question. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Why the correct answer wins: A deterministic process belongs in a flow.

### Question 3 — D

Answer: Adopt the built-in agent that already covers the task. A built-in agent is maintained by the platform and carries less build cost. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **B:** Incorrect for this question. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **C:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **D:** Correct. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. In this case: A built-in agent is maintained by the platform and carries less build cost.

### Question 4 — B

Answer: Build a custom Copilot Studio agent for every requirement. A custom agent earns its cost when the built-in one cannot reach the data. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.
- **B:** Correct. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. In this case: A custom agent earns its cost when the built-in one cannot reach the data.
- **C:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.
- **D:** Incorrect for this question. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Why the correct answer wins: A custom agent earns its cost when the built-in one cannot reach the data.

### Question 5 — B

Answer: Choose the environment type that matches the data boundary and the licence. Environment type sets the boundary and licensing. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The default environment has the widest membership and the least governance, which is where a regulated solution should not start. Why the correct answer wins: Environment type sets the boundary and licensing.
- **B:** Correct. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. In this case: Environment type sets the boundary and licensing.
- **C:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: Environment type sets the boundary and licensing.
- **D:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: Environment type sets the boundary and licensing.

### Question 6 — B

Answer: Promote a managed solution to test and production. A managed solution is locked, so it can be upgraded or removed predictably. A managed solution is locked, so it can be upgraded and removed predictably. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: A managed solution is locked, so it can be upgraded or removed predictably.
- **B:** Correct. A managed solution is locked, so it can be upgraded and removed predictably. In this case: A managed solution is locked, so it can be upgraded or removed predictably.
- **C:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: A managed solution is locked, so it can be upgraded or removed predictably.
- **D:** Incorrect for this question. Building in production removes the test step and puts every unfinished change in front of users. Why the correct answer wins: A managed solution is locked, so it can be upgraded or removed predictably.

### Question 7 — A

Answer: Review the solution layers before overwriting a component. Layers show which solution last changed a component. Layers show which solution last changed a component, which is how an unexplained behaviour is traced. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Layers show which solution last changed a component, which is how an unexplained behaviour is traced. In this case: Layers show which solution last changed a component.
- **B:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: Layers show which solution last changed a component.
- **C:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: Layers show which solution last changed a component.
- **D:** Incorrect for this question. Deleting the carrying solution removes the component and everything that depends on it. Why the correct answer wins: Layers show which solution last changed a component.

### Question 8 — B, D

Answers: Define the solution publisher and prefix once, before the first table; Package the customizations in a solution before moving them. The publisher fixes the prefix, and the solution is the unit of movement. The prefix is baked into every schema name and is expensive to change after data exists. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The automation is not the hard part; the solution boundary and the deployment order are. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.
- **B:** Correct. The prefix is baked into every schema name and is expensive to change after data exists. In this case: The publisher fixes the prefix, and the solution is the unit of movement.
- **C:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.
- **D:** Correct. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. In this case: The publisher fixes the prefix, and the solution is the unit of movement.
- **E:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: The publisher fixes the prefix, and the solution is the unit of movement.

### Question 9 — D

Answer: Create the table in the Dataverse data workspace. The data workspace is where a new table is created. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: The data workspace is where a new table is created.
- **B:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: The data workspace is where a new table is created.
- **C:** Incorrect for this question. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Why the correct answer wins: The data workspace is where a new table is created.
- **D:** Correct. The data workspace lets a maker model tables and relationships without leaving the app-building flow. In this case: The data workspace is where a new table is created.

### Question 10 — D

Answer: Store the interactions in the Activity table. Activities inherit the timeline and the regarding relationship. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.
- **B:** Incorrect for this question. A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.
- **D:** Correct. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. In this case: Activities inherit the timeline and the regarding relationship.

### Question 11 — D

Answer: Configure table properties such as ownership and auditing. Ownership and auditing are table properties. Ownership decides who can see a row and auditing decides whether its history survives an investigation. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Ownership and auditing are table properties.
- **B:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: Ownership and auditing are table properties.
- **C:** Incorrect for this question. Auditing records who changed which column and when, which is what an audit asks for. Why the correct answer wins: Ownership and auditing are table properties.
- **D:** Correct. Ownership decides who can see a row and auditing decides whether its history survives an investigation. In this case: Ownership and auditing are table properties.

### Question 12 — B

Answer: Use a global choice so several tables share one option list. A global choice keeps one approved list across tables. One global choice keeps the list consistent instead of drifting across tables. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A global choice keeps one approved list across tables.
- **B:** Correct. One global choice keeps the list consistent instead of drifting across tables. In this case: A global choice keeps one approved list across tables.
- **C:** Incorrect for this question. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Why the correct answer wins: A global choice keeps one approved list across tables.
- **D:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A global choice keeps one approved list across tables.

### Question 13 — D

Answer: Use an auto-number column for the case identifier. An auto-number gives a readable, unique reference. An auto-number gives every record a readable, unique reference that users can quote. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: An auto-number gives a readable, unique reference.
- **B:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: An auto-number gives a readable, unique reference.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: An auto-number gives a readable, unique reference.
- **D:** Correct. An auto-number gives every record a readable, unique reference that users can quote. In this case: An auto-number gives a readable, unique reference.

### Question 14 — A, E

Answers: Add a choice column for the fixed set of options; Use a lookup column instead of storing the name as text. A choice constrains the value, and a lookup carries the relationship. A choice constrains input to the approved list and renders as a dropdown on every form. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A choice constrains input to the approved list and renders as a dropdown on every form. In this case: A choice constrains the value, and a lookup carries the relationship.
- **B:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **D:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **E:** Correct. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. In this case: A choice constrains the value, and a lookup carries the relationship.

### Question 15 — C

Answer: Configure a one-to-many relationship with a lookup on the child table. A one-to-many relationship with the lookup on the child is the standard shape. The lookup on the child is what makes the parent select a record rather than a typed string. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **B:** Incorrect for this question. Referential behaviour leaves the children in place, which is what a shared dimension needs. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **C:** Correct. The lookup on the child is what makes the parent select a record rather than a typed string. In this case: A one-to-many relationship with the lookup on the child is the standard shape.
- **D:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.

### Question 16 — B

Answer: Configure a prompt column to generate text per row. A prompt column generates a value per row. A prompt column produces a value for each record from a prompt, without a separate flow. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A prompt column generates a value per row.
- **B:** Correct. A prompt column produces a value for each record from a prompt, without a separate flow. In this case: A prompt column generates a value per row.
- **C:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: A prompt column generates a value per row.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A prompt column generates a value per row.

### Question 17 — B

Answer: Configure a row summary to summarize the record text. A row summary condenses the record's own text. A row summary condenses the record's own text, which is what a case recap needs. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A row summary condenses the record's own text.
- **B:** Correct. A row summary condenses the record's own text, which is what a case recap needs. In this case: A row summary condenses the record's own text.
- **C:** Incorrect for this question. A prompt column produces a value for each record from a prompt, without a separate flow. Why the correct answer wins: A row summary condenses the record's own text.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A row summary condenses the record's own text.

### Question 18 — B, D

Answers: Configure a prompt column to generate text per row; Configure a row summary to summarize the record text. The prompt column generates per row, and the row summary condenses the text. A prompt column produces a value for each record from a prompt, without a separate flow. A row summary condenses the record's own text, which is what a case recap needs. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: The prompt column generates per row, and the row summary condenses the text.
- **B:** Correct. A prompt column produces a value for each record from a prompt, without a separate flow. In this case: The prompt column generates per row, and the row summary condenses the text.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: The prompt column generates per row, and the row summary condenses the text.
- **D:** Correct. A row summary condenses the record's own text, which is what a case recap needs. In this case: The prompt column generates per row, and the row summary condenses the text.
- **E:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: The prompt column generates per row, and the row summary condenses the text.

### Question 19 — B

Answer: Create a public view for the shared filtered list. A public view is shared with everyone who has access to the table. A public view is available to everyone with access to the table, so the team sees the same list. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **B:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: A public view is shared with everyone who has access to the table.
- **C:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **D:** Incorrect for this question. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Why the correct answer wins: A public view is shared with everyone who has access to the table.

### Question 20 — B

Answer: Change the system view so the list order suits the team. The system view is the fallback for every view and every app. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The system view is the fallback for every view and every app.
- **B:** Correct. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. In this case: The system view is the fallback for every view and every app.
- **C:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The system view is the fallback for every view and every app.
- **D:** Incorrect for this question. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Why the correct answer wins: The system view is the fallback for every view and every app.

### Question 21 — D

Answer: Assign a security role that grants only the privileges the role needs. A security role grants privileges at a scope. A security role is how Dataverse decides create, read, write, and delete per table. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A security role grants privileges at a scope.
- **B:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: A security role grants privileges at a scope.
- **C:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A security role grants privileges at a scope.
- **D:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: A security role grants privileges at a scope.

### Question 22 — A

Answer: Use a field security profile for the sensitive column. A field security profile hides a column without hiding the record. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: A field security profile hides a column without hiding the record.
- **B:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **C:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **D:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A field security profile hides a column without hiding the record.

### Question 23 — A, B

Answers: Assign a security role that grants only the privileges the role needs; Use a field security profile for the sensitive column. The role grants table privileges, and the profile hides the column. A security role is how Dataverse decides create, read, write, and delete per table. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: The role grants table privileges, and the profile hides the column.
- **B:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: The role grants table privileges, and the profile hides the column.
- **C:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **D:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **E:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: The role grants table privileges, and the profile hides the column.

### Question 24 — A

Answer: Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it. Coverage is tested with a pilot before committing to a custom build. Coverage is tested with a pilot before anyone commits to a custom build. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Coverage is tested with a pilot before anyone commits to a custom build. In this case: Coverage is tested with a pilot before committing to a custom build.
- **B:** Incorrect for this question. Building first pays the custom-agent cost before coverage is even known. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **C:** Incorrect for this question. Adopting before a pilot skips the step that would have caught the gap. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **D:** Incorrect for this question. There is nothing to measure before a pilot exists. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.

### Question 25 — D

Answer: Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline. The boundary and licence decide the environment type, and the pipeline carries the result. The boundary and licence decide the environment type, and the pipeline carries the packaged result. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Deployment before packaging has nothing to deploy. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.
- **B:** Incorrect for this question. Every step here runs ahead of the decision it depends on. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.
- **C:** Incorrect for this question. Choosing an environment after deploying is how a solution ends up in the wrong data boundary. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the result.
- **D:** Correct. The boundary and licence decide the environment type, and the pipeline carries the packaged result. In this case: The boundary and licence decide the environment type, and the pipeline carries the result.

### Question 26 — B

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.
- **B:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **C:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 27 — C

Answer: Hide the field with a JavaScript web resource. A form script affects that form only. A form script only affects that form, so the field is still editable everywhere else. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A form script affects that form only.
- **B:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A form script affects that form only.
- **C:** Correct. A form script only affects that form, so the field is still editable everywhere else. In this case: A form script affects that form only.
- **D:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form script affects that form only.

### Question 28 — A

Answer: Filter the view on the columns the team actually searches. The filter decides which records are in the list. The filter decides which records appear, so it must match the question the list answers. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides which records are in the list.
- **B:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The filter decides which records are in the list.
- **C:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides which records are in the list.
- **D:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides which records are in the list.

### Question 29 — D

Answer: Choose the view columns before setting the filter. The columns decide what is readable without opening the record. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The columns decide what is readable without opening the record.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: The columns decide what is readable without opening the record.
- **C:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The columns decide what is readable without opening the record.
- **D:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The columns decide what is readable without opening the record.

### Question 30 — A, C

Answers: Filter the view on the columns the team actually searches; Choose the view columns before setting the filter. The filter decides the rows, and the columns make them readable. The filter decides which records appear, so it must match the question the list answers. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides the rows, and the columns make them readable.
- **B:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **C:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The filter decides the rows, and the columns make them readable.
- **D:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **E:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The filter decides the rows, and the columns make them readable.

### Question 31 — C

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close, and the maker owns the bindings. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **B:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **C:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close, and the maker owns the bindings.
- **D:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.

### Question 32 — A

Answer: Publish the generated page without reviewing its data bindings. An unreviewed generated page can bind to data the audience is not entitled to. An unreviewed page can bind to a table the audience should not read. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. An unreviewed page can bind to a table the audience should not read. In this case: An unreviewed generated page can bind to data the audience is not entitled to.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.
- **C:** Incorrect for this question. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.
- **D:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.

### Question 33 — D

Answer: Add the forms, views, and pages to the app in the app designer. The app designer decides which components the app exposes. The app designer decides which components the app exposes, so composition is a security-relevant choice. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: The app designer decides which components the app exposes.
- **B:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The app designer decides which components the app exposes.
- **C:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The app designer decides which components the app exposes.
- **D:** Correct. The app designer decides which components the app exposes, so composition is a security-relevant choice. In this case: The app designer decides which components the app exposes.

### Question 34 — C

Answer: Configure the navigation in the sitemap designer. The sitemap is the app's menu. The sitemap is the app's menu, so it decides what a user can reach at all. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: The sitemap is the app's menu.
- **B:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The sitemap is the app's menu.
- **C:** Correct. The sitemap is the app's menu, so it decides what a user can reach at all. In this case: The sitemap is the app's menu.
- **D:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The sitemap is the app's menu.

### Question 35 — C

Answer: Add the chart and the views to a dashboard. A dashboard composes several components onto one page. A dashboard composes several components so a manager sees the whole picture on one page. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: A dashboard composes several components onto one page.
- **B:** Incorrect for this question. A chart bound to a view reuses that view's filter instead of duplicating it. Why the correct answer wins: A dashboard composes several components onto one page.
- **C:** Correct. A dashboard composes several components so a manager sees the whole picture on one page. In this case: A dashboard composes several components onto one page.
- **D:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: A dashboard composes several components onto one page.

### Question 36 — B

Answer: Generate a canvas app from the data source. Generating from data gives working screens immediately. Generating from data gives working screens over the chosen tables immediately. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Why the correct answer wins: Generating from data gives working screens immediately.
- **B:** Correct. Generating from data gives working screens over the chosen tables immediately. In this case: Generating from data gives working screens immediately.
- **C:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Generating from data gives working screens immediately.
- **D:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Generating from data gives working screens immediately.

### Question 37 — A, B

Answers: Write the filter so the data source performs the delegation; Use responsive containers so the layout adapts to the device. Delegation keeps the query on the source, and responsive containers fit both. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Delegation sends the query to the source, so the app never downloads more rows than it can handle. In this case: Delegation keeps the query on the source, and responsive containers fit both.
- **B:** Correct. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. In this case: Delegation keeps the query on the source, and responsive containers fit both.
- **C:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.
- **D:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.
- **E:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.

### Question 38 — C

Answer: Use responsive containers so the layout adapts to the device. Responsive containers reflow so one app fits both. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **C:** Correct. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. In this case: Responsive containers reflow so one app fits both.
- **D:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Responsive containers reflow so one app fits both.

### Question 39 — A

Answer: Define a named formula for the shared calculation. A named formula is reused by name instead of copied. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: A named formula is reused by name instead of copied.
- **B:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A named formula is reused by name instead of copied.
- **C:** Incorrect for this question. A component library is the reusable, versioned home for a control that several apps must share. Why the correct answer wins: A named formula is reused by name instead of copied.
- **D:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A named formula is reused by name instead of copied.

### Question 40 — D

Answer: Publish a component library for the shared header and controls. A component library is the reusable, versioned home for a shared control. A component library is the reusable, versioned home for a control that several apps must share. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **B:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **C:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **D:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: A component library is the reusable, versioned home for a shared control.

### Question 41 — A, D

Answers: Publish a component library for the shared header and controls; Define a named formula for the shared calculation. The library shares the control, and the named formula shares the calculation. A component library is the reusable, versioned home for a control that several apps must share. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: The library shares the control, and the named formula shares the calculation.
- **B:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **C:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **D:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: The library shares the control, and the named formula shares the calculation.
- **E:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.

### Question 42 — A

Answer: Wrap the call in IfError and surface the message to the user. IfError catches the failure and lets the app recover. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. In this case: IfError catches the failure and lets the app recover.
- **B:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: IfError catches the failure and lets the app recover.
- **C:** Incorrect for this question. Test Studio captures the screens and formulas that a regression would break. Why the correct answer wins: IfError catches the failure and lets the app recover.
- **D:** Incorrect for this question. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Why the correct answer wins: IfError catches the failure and lets the app recover.

### Question 43 — C

Answer: Clear the collection when the screen changes. An un-cleared collection keeps the previous user's rows in memory. An un-cleared collection keeps the previous user's rows in memory. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: An un-cleared collection keeps the previous user's rows in memory.
- **B:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: An un-cleared collection keeps the previous user's rows in memory.
- **C:** Correct. An un-cleared collection keeps the previous user's rows in memory. In this case: An un-cleared collection keeps the previous user's rows in memory.
- **D:** Incorrect for this question. A global variable persists across screens, which is what a signed-in user's selection needs. Why the correct answer wins: An un-cleared collection keeps the previous user's rows in memory.

### Question 44 — A, C

Answers: Use a global variable for the value that the whole app needs; Wrap the call in IfError and surface the message to the user. A global variable persists, and IfError handles the failure. A global variable persists across screens, which is what a signed-in user's selection needs. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists, and IfError handles the failure.
- **B:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **C:** Correct. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. In this case: A global variable persists, and IfError handles the failure.
- **D:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **E:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists, and IfError handles the failure.

### Question 45 — B

Answer: Run the app in Test Studio before publishing. Test Studio captures the screens and formulas a regression would break. Test Studio captures the screens and formulas that a regression would break. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **B:** Correct. Test Studio captures the screens and formulas that a regression would break. In this case: Test Studio captures the screens and formulas a regression would break.
- **C:** Incorrect for this question. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **D:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.

### Question 46 — B

Answer: Add the Copilot Studio agent to the canvas app as a component. The agent component adds a conversational surface to the app. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A second app multiplies the maintenance without adding capability. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **B:** Correct. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. In this case: The agent component adds a conversational surface to the app.
- **C:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **D:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: The agent component adds a conversational surface to the app.

### Question 47 — A

Answer: Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role. The app is composed from finished components, and access is granted last. The app is composed from finished components, and access is granted last. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. The app is composed from finished components, and access is granted last. In this case: The app is composed from finished components, and access is granted last.
- **B:** Incorrect for this question. Granting data access before the app exists gives access with nothing to use it in. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **C:** Incorrect for this question. Sharing an app that has no components shows users an empty shell. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **D:** Incorrect for this question. Navigation is meaningless until the components exist. Why the correct answer wins: The app is composed from finished components, and access is granted last.

### Question 48 — C

Answer: Build the canvas app → add the Copilot Studio agent as a component → configure the agent topics and knowledge → test the conversation in the app → publish. The agent is added to a working app, and its behaviour is tested before release. The agent is added to a working app, and its behaviour is tested before release. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Publishing before the host app exists delivers an agent nobody can reach. Why the correct answer wins: The agent is added to a working app, and its behaviour is tested before release.
- **B:** Incorrect for this question. The topics are what the test is checking, so they come first. Why the correct answer wins: The agent is added to a working app, and its behaviour is tested before release.
- **C:** Correct. The agent is added to a working app, and its behaviour is tested before release. In this case: The agent is added to a working app, and its behaviour is tested before release.
- **D:** Incorrect for this question. The conversation cannot be tested before the component is in an app. Why the correct answer wins: The agent is added to a working app, and its behaviour is tested before release.

### Question 49 — C

Answer: Use an automated trigger on record creation. An automated trigger runs without a user. An automated trigger runs without a user, which is what a background rule needs. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: An automated trigger runs without a user.
- **B:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: An automated trigger runs without a user.
- **C:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: An automated trigger runs without a user.
- **D:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: An automated trigger runs without a user.

### Question 50 — B

Answer: Use a manually triggered flow from the app. A manual trigger gives the user the decision. A manual trigger gives the user the decision about when the process runs. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A manual trigger gives the user the decision.
- **B:** Correct. A manual trigger gives the user the decision about when the process runs. In this case: A manual trigger gives the user the decision.
- **C:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: A manual trigger gives the user the decision.
- **D:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A manual trigger gives the user the decision.

### Question 51 — B

Answer: Trigger when a chosen column changes, with a filter condition. A column filter stops irrelevant updates. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A column filter stops irrelevant updates.
- **B:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: A column filter stops irrelevant updates.
- **C:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: A column filter stops irrelevant updates.
- **D:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A column filter stops irrelevant updates.

### Question 52 — D

Answer: Use the standard Dataverse connector. The standard connector covers Dataverse natively. The standard connector is included in the base licence and covers Dataverse natively. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: The standard connector covers Dataverse natively.
- **B:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: The standard connector covers Dataverse natively.
- **C:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: The standard connector covers Dataverse natively.
- **D:** Correct. The standard connector is included in the base licence and covers Dataverse natively. In this case: The standard connector covers Dataverse natively.

### Question 53 — D

Answer: Build a custom connector for the internal API. A custom connector wraps an authenticated API as a first-class action. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **B:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **C:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **D:** Correct. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. In this case: A custom connector wraps an authenticated API as a first-class action.

### Question 54 — B

Answer: Chain two approvals in sequence for the second-level sign-off. A second approval after the first adds a second-level sign-off. A second approval after the first is how a value threshold adds a second approver. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: A second approval after the first adds a second-level sign-off.
- **B:** Correct. A second approval after the first is how a value threshold adds a second approver. In this case: A second approval after the first adds a second-level sign-off.
- **C:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: A second approval after the first adds a second-level sign-off.
- **D:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: A second approval after the first adds a second-level sign-off.

### Question 55 — B

Answer: Send parallel approvals and require every response. Parallel approvals requiring every response match that rule. Everyone must approve is the right type when each stakeholder holds a veto. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Parallel approvals requiring every response match that rule.
- **B:** Correct. Everyone must approve is the right type when each stakeholder holds a veto. In this case: Parallel approvals requiring every response match that rule.
- **C:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: Parallel approvals requiring every response match that rule.
- **D:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Parallel approvals requiring every response match that rule.

### Question 56 — A

Answer: Parse JSON so later steps can use the fields. Parse JSON turns an opaque body into typed properties. Parse JSON turns an opaque body into typed properties the designer can offer you. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Parse JSON turns an opaque body into typed properties the designer can offer you. In this case: Parse JSON turns an opaque body into typed properties.
- **B:** Incorrect for this question. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **D:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.

### Question 57 — B

Answer: Apply to each over the returned rows. Apply to each iterates the array. Apply to each iterates the array, which is how one run processes many records. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: Apply to each iterates the array.
- **B:** Correct. Apply to each iterates the array, which is how one run processes many records. In this case: Apply to each iterates the array.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Apply to each iterates the array.
- **D:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Apply to each iterates the array.

### Question 58 — D

Answer: Add a condition to branch on the status. A condition is the explicit branch for two paths. A condition is the explicit branch that makes the two paths readable in the run history. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: A condition is the explicit branch for two paths.
- **B:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A condition is the explicit branch for two paths.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A condition is the explicit branch for two paths.
- **D:** Correct. A condition is the explicit branch that makes the two paths readable in the run history. In this case: A condition is the explicit branch for two paths.

### Question 59 — A

Answer: Use Do until with a bounded count for the retry loop. Do until repeats until the condition holds, with a count limit to stop a loop. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. In this case: Do until repeats until the condition holds, with a count limit to stop a loop.
- **B:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.
- **C:** Incorrect for this question. A loop with no bound can run until the run timeout, consuming the flow's quota. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.
- **D:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Do until repeats until the condition holds, with a count limit to stop a loop.

### Question 60 — D

Answer: Read the run history to find the failed action and its inputs. The run history shows each action's inputs and outputs. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **C:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **D:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows each action's inputs and outputs.

### Question 61 — D

Answer: Test the flow with the real trigger payload. A production-shaped payload proves the expressions resolve. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **C:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **D:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: A production-shaped payload proves the expressions resolve.

### Question 62 — C

Answer: Start from a prompt template in AI Hub. A template carries a tested instruction and the input contract. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **C:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: A template carries a tested instruction and the input contract.
- **D:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A template carries a tested instruction and the input contract.

### Question 63 — C

Answer: Build the prompt from blank. A blank prompt is right when no template covers the task. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **B:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **C:** Correct. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. In this case: A blank prompt is right when no template covers the task.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A blank prompt is right when no template covers the task.

### Question 64 — A

Answer: Add typed inputs so the prompt takes values. Typed inputs become the parameters an app or flow supplies. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Typed inputs become the parameters an app or flow supplies.
- **B:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **D:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.

### Question 65 — A

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in approved documents. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in approved documents.
- **B:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.

### Question 66 — B

Answer: Choose the model that fits the task instead of the largest available. Matching the model to the task controls cost. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Matching the model to the task controls cost.
- **B:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Matching the model to the task controls cost.
- **C:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Matching the model to the task controls cost.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Matching the model to the task controls cost.

### Question 67 — A

Answer: Copy the prompt text into each app so it can be tuned per app. Copied prompt text drifts, so the same question gets different answers. Copied prompt text drifts, so the same question gets different answers in different apps. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Copied prompt text drifts, so the same question gets different answers in different apps. In this case: Copied prompt text drifts, so the same question gets different answers.
- **B:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.
- **C:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.
- **D:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Copied prompt text drifts, so the same question gets different answers.

### Question 68 — C

Answer: Call the prompt from the canvas app through its connector. Consuming the published prompt keeps one instruction behind the app. Consuming the published prompt keeps one instruction and one model choice behind every app. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **B:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **C:** Correct. Consuming the published prompt keeps one instruction and one model choice behind every app. In this case: Consuming the published prompt keeps one instruction behind the app.
- **D:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.

### Question 69 — A

Answer: Call the prompt from the cloud flow action. A flow can run a prompt as a step and store the result. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A flow can run a prompt as a step, which is how a generated summary joins an automated process. In this case: A flow can run a prompt as a step and store the result.
- **B:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **D:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: A flow can run a prompt as a step and store the result.

### Question 70 — D

Answer: Configure a business rule on the table. A business rule enforces a condition or required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **C:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **D:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a condition or required field without code.

### Question 71 — C

Answer: Set the business rule scope to the table so it applies in every form. Table scope makes the rule apply to imports and flows. Table scope is what makes the rule hold for imports and flows as well as the main form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: Table scope makes the rule apply to imports and flows.
- **B:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: Table scope makes the rule apply to imports and flows.
- **C:** Correct. Table scope is what makes the rule hold for imports and flows as well as the main form. In this case: Table scope makes the rule apply to imports and flows.
- **D:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: Table scope makes the rule apply to imports and flows.

### Question 72 — B

Answer: Model the stages in a business process flow. A business process flow guides a record through stages. A business process flow guides a record through stages and pins the fields each stage needs. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A branch lets one process cover two variants without a second process and a duplicate set of stages. Why the correct answer wins: A business process flow guides a record through stages.
- **B:** Correct. A business process flow guides a record through stages and pins the fields each stage needs. In this case: A business process flow guides a record through stages.
- **C:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A business process flow guides a record through stages.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A business process flow guides a record through stages.

### Question 73 — C

Answer: Branch the business process flow on the case type. A branch covers two variants without a second process. A branch lets one process cover two variants without a second process and a duplicate set of stages. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A branch covers two variants without a second process.
- **B:** Incorrect for this question. A business process flow guides a record through stages and pins the fields each stage needs. Why the correct answer wins: A branch covers two variants without a second process.
- **C:** Correct. A branch lets one process cover two variants without a second process and a duplicate set of stages. In this case: A branch covers two variants without a second process.
- **D:** Incorrect for this question. One linear process forces every case through fields and stages it does not need. Why the correct answer wins: A branch covers two variants without a second process.

### Question 74 — B

Answer: Use a formula column where the rule needs Power Fx. A formula column evaluates a Power Fx expression. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **B:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column evaluates a Power Fx expression.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **D:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A formula column evaluates a Power Fx expression.

### Question 75 — C

Answer: Use a rollup column to aggregate the child records. A rollup aggregates related rows on a schedule. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **B:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **C:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A rollup aggregates related rows on a schedule.
- **D:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A rollup aggregates related rows on a schedule.

### Question 76 — C

Answer: Pick the logic mechanism that matches where the rule must hold. A mechanism is chosen by where the rule must hold. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. Local study-map skill 3.14 (Choosing the Right Business Logic), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A synchronous plug-in runs inside the save, so no caller can bypass it. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **B:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **C:** Correct. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. In this case: A mechanism is chosen by where the rule must hold.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A mechanism is chosen by where the rule must hold.

### Question 77 — B, E

Answers: Use an automated trigger on record creation; Trigger when a chosen column changes, with a filter condition. The automated trigger starts the run, and the filter stops irrelevant updates. An automated trigger runs without a user, which is what a background rule needs. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **B:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.
- **C:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **D:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **E:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.

### Question 78 — A, B

Answers: Start and wait for an approval; Choose the approval type that matches the sign-off the process requires. The approval action pauses the run, and the type encodes who must respond. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run, and the type encodes who must respond.
- **B:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: The approval action pauses the run, and the type encodes who must respond.
- **C:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **D:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **E:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.

### Question 79 — B, D

Answers: Wrap the steps in a Scope so one error path handles the failures; Configure run after so the failure path actually executes. A scope groups the steps, and run after makes the failure branch execute. A scope groups steps so a single run-after configuration can catch any failure inside it. By default a step runs only on success, so the failure branch never fires without this setting. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **B:** Correct. A scope groups steps so a single run-after configuration can catch any failure inside it. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **C:** Incorrect for this question. Concurrency runs iterations in parallel, which is faster but reorders side effects. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **D:** Correct. By default a step runs only on success, so the failure branch never fires without this setting. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **E:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.

### Question 80 — A, C

Answers: Read the run history to find the failed action and its inputs; Test the flow with the real trigger payload. The run history shows the wrong value, and a real payload proves the fix. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: The run history shows the wrong value, and a real payload proves the fix.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **C:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows the wrong value, and a real payload proves the fix.
- **D:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **E:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.

### Question 81 — B, C

Answers: Start from a prompt template in AI Hub; Add the knowledge source so the prompt grounds on approved content. The template supplies the instruction, and knowledge grounds the answer. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **B:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: The template supplies the instruction, and knowledge grounds the answer.
- **C:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: The template supplies the instruction, and knowledge grounds the answer.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **E:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.

### Question 82 — B, E

Answers: Choose the model that fits the task instead of the largest available; Add typed inputs so the prompt takes values. Inputs are the parameters, and the model choice controls cost and quality. Matching the model to the task controls cost and latency without losing the quality the task needs. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **B:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Inputs are the parameters, and the model choice controls cost and quality.
- **C:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **D:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **E:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Inputs are the parameters, and the model choice controls cost and quality.

### Question 83 — C, E

Answers: Configure a business rule on the table; Enforce the rule in a synchronous plug-in when it must run on every write. A table-scope business rule covers imports, and a synchronous plug-in runs inside the save. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. A synchronous plug-in runs inside the save, so no caller can bypass it. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **B:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **C:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **D:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **E:** Correct. A synchronous plug-in runs inside the save, so no caller can bypass it. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.

### Question 84 — B, D

Answers: Use a formula column where the rule needs Power Fx; Use a rollup column to aggregate the child records. A formula column recalculates, and a rollup aggregates children. A formula column evaluates a Power Fx expression, which is the current way to express derived values. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **B:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column recalculates, and a rollup aggregates children.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **D:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A formula column recalculates, and a rollup aggregates children.
- **E:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.

### Question 85 — D

Answer: Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run. The event decides the trigger, and the real payload decides whether the expressions resolve. The event decides the trigger, and the payload decides whether the expressions actually resolve. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. There is no payload to test until a trigger and actions exist. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **B:** Incorrect for this question. Actions placed before the trigger cannot know what data they receive. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **C:** Incorrect for this question. A run history only exists after a run has happened. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **D:** Correct. The event decides the trigger, and the payload decides whether the expressions actually resolve. In this case: The event decides the trigger, and the real payload decides whether the expressions resolve.

### Question 86 — D

Answer: Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester. The branch reads the approval outcome, and the record update carries the decision. The branch reads the approval outcome, and the record update carries the decision. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The record cannot be updated with a decision that has not been taken. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **B:** Incorrect for this question. Notifying first tells the requester about a decision that does not exist. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **C:** Incorrect for this question. A branch with no outcome yet has nothing to evaluate. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **D:** Correct. The branch reads the approval outcome, and the record update carries the decision. In this case: The branch reads the approval outcome, and the record update carries the decision.

### Question 87 — D

Answer: Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run. The run history turns a symptom into a specific wrong value. The run history is what turns a symptom into a specific wrong value. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. There is no run to inspect until the failure is reproduced. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **B:** Incorrect for this question. Resubmitting an unfixed flow repeats the same failure. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **C:** Incorrect for this question. A fix applied before diagnosis is a guess. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **D:** Correct. The run history is what turns a symptom into a specific wrong value. In this case: The run history turns a symptom into a specific wrong value.

### Question 88 — C

Answer: Define the stages the record moves through → choose the columns each stage requires → branch the process where the case types diverge → test a record through every stage → hand the process to the users. Stages and their required columns define the process. Stages and their required columns define the process; branching handles the variants without a second process. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A branch needs stages to branch from. Why the correct answer wins: Stages and their required columns define the process.
- **B:** Incorrect for this question. There is nothing to test through until the stages exist. Why the correct answer wins: Stages and their required columns define the process.
- **C:** Correct. Stages and their required columns define the process; branching handles the variants without a second process. In this case: Stages and their required columns define the process.
- **D:** Incorrect for this question. Users handed a process with no stages see an empty tracker. Why the correct answer wins: Stages and their required columns define the process.

### Question 89 — A

Answer: Extend the standard table instead of creating a duplicate. Extending the standard table keeps the built-in relationships. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. In this case: Extending the standard table keeps the built-in relationships.
- **B:** Incorrect for this question. A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **D:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: Extending the standard table keeps the built-in relationships.

### Question 90 — A

Answer: Create a user-defined function for the reused expression. A user-defined function accepts parameters and returns a value for reuse. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. In this case: A user-defined function accepts parameters and returns a value for reuse.
- **B:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **C:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **D:** Incorrect for this question. A component library is the reusable, versioned home for a control that several apps must share. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.

### Question 91 — A

Answer: Configure a business rule on the table. A business rule enforces a required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a required field without code.
- **B:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A business rule enforces a required field without code.
- **C:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a required field without code.
- **D:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a required field without code.

### Question 92 — A

Answer: Move the user to another business unit to fix access. Business units partition ownership, which separates districts. Business units partition ownership; moving a user changes far more than one record. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Business units partition ownership; moving a user changes far more than one record. In this case: Business units partition ownership, which separates districts.
- **B:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: Business units partition ownership, which separates districts.
- **C:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: Business units partition ownership, which separates districts.
- **D:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: Business units partition ownership, which separates districts.

### Question 93 — D

Answer: Create the chart on the view for the trend. A chart bound to a view reuses that view's filter. A chart bound to a view reuses that view's filter instead of duplicating it. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **B:** Incorrect for this question. A dashboard composes several components so a manager sees the whole picture on one page. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **C:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **D:** Correct. A chart bound to a view reuses that view's filter instead of duplicating it. In this case: A chart bound to a view reuses that view's filter.

### Question 94 — A

Answer: Call the model from the flow and store the result on the record. Calling the model from the flow and storing the result makes it auditable. Storing the result on the record is what makes the model output visible to the process and the audit. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Storing the result on the record is what makes the model output visible to the process and the audit. In this case: Calling the model from the flow and storing the result makes it auditable.
- **B:** Incorrect for this question. A model consumed this way keeps authentication and throttling in one governed place. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.
- **C:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.
- **D:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.

### Question 95 — A

Answer: Write the filter so the data source performs the delegation. Delegation keeps the query on the source. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Delegation sends the query to the source, so the app never downloads more rows than it can handle. In this case: Delegation keeps the query on the source.
- **B:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Delegation keeps the query on the source.
- **C:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: Delegation keeps the query on the source.
- **D:** Incorrect for this question. Generating from data gives working screens over the chosen tables immediately. Why the correct answer wins: Delegation keeps the query on the source.

### Question 96 — A

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close quickly. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close quickly.
- **B:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close quickly.
- **C:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close quickly.
- **D:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close quickly.

### Question 97 — D

Answer: Apply to each over the returned rows. Apply to each iterates the array. Apply to each iterates the array, which is how one run processes many records. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: Apply to each iterates the array.
- **B:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Apply to each iterates the array.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Apply to each iterates the array.
- **D:** Correct. Apply to each iterates the array, which is how one run processes many records. In this case: Apply to each iterates the array.

### Question 98 — C

Answer: Use Power Platform pipelines to deploy between environments. A pipeline runs the same solution through each stage and records it. A pipeline records the deployment and runs the same solution through each stage. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: A pipeline runs the same solution through each stage and records it.
- **B:** Incorrect for this question. The automation is not the hard part; the solution boundary and the deployment order are. Why the correct answer wins: A pipeline runs the same solution through each stage and records it.
- **C:** Correct. A pipeline records the deployment and runs the same solution through each stage. In this case: A pipeline runs the same solution through each stage and records it.
- **D:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: A pipeline runs the same solution through each stage and records it.

### Question 99 — C

Answer: Create a public view for the shared filtered list. A public view is shared with everyone who has access to the table. A public view is available to everyone with access to the table, so the team sees the same list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **B:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **C:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: A public view is shared with everyone who has access to the table.
- **D:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: A public view is shared with everyone who has access to the table.

### Question 100 — B

Answer: Start and wait for an approval. The approval action pauses the run and resumes with the outcome. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **B:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run and resumes with the outcome.
- **C:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **D:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.

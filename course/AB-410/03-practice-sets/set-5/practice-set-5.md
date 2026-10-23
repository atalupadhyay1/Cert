# Microsoft AB-410 — Full-Length Mock Exam 5

Intelligent Applications Builder Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the maker portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A distributor requirement spans a rep app, a pricing approval, and a quote document. What should be decided first?

Domain: Create a foundation for intelligent applications

- A. Build a working prototype in a week and let the business react to it
- B. Start with a custom connector and a plug-in for the first version
- C. Map each requirement to the Power Platform component that fits it
- D. Deliver every requirement as a single model-driven app

### 2. A maker proposes one model-driven app for reps, pricing, and finance. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Map each requirement to the Power Platform component that fits it
- B. Ship a code-first component now and replace it with low-code later
- C. Start with a custom connector and a plug-in for the first version
- D. Deliver every requirement as a single model-driven app

### 3. The business cannot describe the quoting rules and wants something to react to. What is the reasonable first move?

Domain: Create a foundation for intelligent applications

- A. Build a working prototype in a week and let the business react to it
- B. Start with a custom connector and a plug-in for the first version
- C. Map each requirement to the Power Platform component that fits it
- D. Deliver every requirement as a single model-driven app

### 4. Sales wants a helper that answers questions about quotes. What should be evaluated first?

Domain: Create a foundation for intelligent applications

- A. Build a custom Copilot Studio agent for every requirement
- B. Adopt the built-in agent that already covers the task
- C. Model the process as a cloud flow with no agent at all
- D. Build a Power Apps component framework control

### 5. The pricing team needs a margin-band visual no standard control provides. What should be built?

Domain: Create a foundation for intelligent applications

- A. Build a Power Apps component framework control
- B. Ship a code-first component now and replace it with low-code later
- C. Write a Dataverse plug-in in C#
- D. Add a JavaScript web resource to the form

### 6. The distributor solution must sit in its own governed boundary. What decides the environment?

Domain: Create a foundation for intelligent applications

- A. Use the trial environment for production after the pilot
- B. Choose the environment type that matches the data boundary and the licence
- C. Build in the default environment because everyone already has access
- D. Share a single environment between development and production

### 7. Customizations must move between environments without hand rework. What should they be packaged as?

Domain: Create a foundation for intelligent applications

- A. Import unmanaged customizations directly into production
- B. Use Power Platform pipelines to deploy between environments
- C. Package the customizations in a solution before moving them
- D. Clone the environment each time instead of using a pipeline

### 8. A distributor solution must carry a stable prefix and be removable. Which two practices apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Clone the environment each time instead of using a pipeline
- B. Import unmanaged customizations directly into production
- C. Do all building in the production environment to avoid deployment
- D. Define the solution publisher and prefix once, before the first table
- E. Promote a managed solution to test and production

### 9. A quote line list is proposed in SharePoint to avoid modelling. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Store the interactions in the Activity table
- B. Create the table in the Dataverse data workspace
- C. Extend the standard table instead of creating a duplicate
- D. Keep the records in a SharePoint list and skip Dataverse

### 10. Retailer contacts must reuse the fields users already know. What should be used?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Create a custom table for the new business entity
- C. Store the account name as text so the form stays simple
- D. Store the interactions in the Activity table

### 11. A quote must be owned by a rep and keep its history. What decides that?

Domain: Create a foundation for intelligent applications

- A. Enable auditing on the tables that hold regulated data
- B. Configure table properties such as ownership and auditing
- C. Extend the standard table instead of creating a duplicate
- D. Configure a row summary to summarize the record text

### 12. A quote status must accept only four approved values. What implements that?

Domain: Create a foundation for intelligent applications

- A. Add a choice column for the fixed set of options
- B. Store the account name as text so the form stays simple
- C. Use a lookup column instead of storing the name as text
- D. Use a global choice so several tables share one option list

### 13. A quote must point at its account rather than copy the name. What should be added?

Domain: Create a foundation for intelligent applications

- A. Use a lookup column instead of storing the name as text
- B. Use a currency column with the record currency
- C. Add a choice column for the fixed set of options
- D. Store the account name as text so the form stays simple

### 14. A quote line must carry its currency and a rate must stay exact. Which two column types apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Add a choice column for the fixed set of options
- B. Use a decimal column for an exact rate
- C. Use a currency column with the record currency
- D. Use an auto-number column for the case identifier
- E. Store the account name as text so the form stays simple

### 15. A quote has many lines and each line belongs to one quote. How should that be modelled?

Domain: Create a foundation for intelligent applications

- A. Model the many-to-many link with a native N:N relationship
- B. Keep the relationship referential so child records survive the parent delete
- C. Set the relationship behaviour to parental so child records are removed with the parent
- D. Configure a one-to-many relationship with a lookup on the child table

### 16. A quote line has no meaning without its quote. What relationship behaviour fits?

Domain: Create a foundation for intelligent applications

- A. Configure a one-to-many relationship with a lookup on the child table
- B. Model the many-to-many link with a native N:N relationship
- C. Keep the relationship referential so child records survive the parent delete
- D. Set the relationship behaviour to parental so child records are removed with the parent

### 17. A rep opens a quote to work on it. Which form is the primary editing surface?

Domain: Create a foundation for intelligent applications

- A. Add the column to a card form on the main form
- B. Add a quick-create form for entry from a lookup
- C. Design the main form around the record the user opens
- D. Organize the long form into tabs and sections

### 18. A rep must add a contact without leaving the quote. What should be added?

Domain: Create a foundation for intelligent applications

- A. Add the column to a card form on the main form
- B. Add a quick-create form for entry from a lookup
- C. Design the main form around the record the user opens
- D. Organize the long form into tabs and sections

### 19. A sales team needs one shared list and one working quote form. Which two components apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Design the main form around the record the user opens
- B. Create a public view for the shared filtered list
- C. Change the system view so the list order suits the team
- D. Rely on each user's personal view of the table
- E. Add a quick-create form for entry from a lookup

### 20. A rep may read only their own accounts. What grants that?

Domain: Create a foundation for intelligent applications

- A. Assign the record to a team that the group owns
- B. Use a field security profile for the sensitive column
- C. Assign a security role that grants only the privileges the role needs
- D. Move the user to another business unit to fix access

### 21. A margin column must stay hidden from reps while the quote stays visible. What should be used?

Domain: Create a foundation for intelligent applications

- A. Assign a security role that grants only the privileges the role needs
- B. Move the user to another business unit to fix access
- C. Assign the record to a team that the group owns
- D. Use a field security profile for the sensitive column

### 22. Access must be granted per table and the margin column hidden. Which two controls apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Assign a security role that grants only the privileges the role needs
- B. Create a public view for the shared filtered list
- C. Assign the record to a team that the group owns
- D. Use a field security profile for the sensitive column
- E. Move the user to another business unit to fix access

### 23. A distributor must decide whether an agent is worth building. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Check whether a built-in agent covers it → build a custom agent → adopt it in production → map the requirement to a component → pilot in development
- B. Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it
- C. Measure the outcome → pilot the agent in development → build a custom agent → map the requirement to a component → check built-in coverage
- D. Build a custom agent → map the requirement to a component → pilot in development → measure the outcome → check built-in coverage

### 24. A quoting solution must travel from build to production under control. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Import managed into test → build unmanaged in development → deploy to production → define the publisher prefix → export the solution
- B. Build unmanaged in production → export the solution → define the publisher prefix → import managed into test → deploy to development
- C. Export the solution → define the publisher prefix → build unmanaged in development → deploy to production → import into test
- D. Define the publisher prefix → build unmanaged in development → export the solution → import managed into test → deploy managed to production

### 25. A quote form carries forty columns and reps use twelve. What should change?

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Hide the field with a JavaScript web resource
- C. Add the columns the role uses to the main form
- D. Choose the view columns before setting the filter

### 26. A long quote form must stay reachable without a wall of inputs. What should be done?

Domain: Create intelligent applications

- A. Add the column to a card form on the main form
- B. Add the columns the role uses to the main form
- C. Choose the view columns before setting the filter
- D. Organize the long form into tabs and sections

### 27. A quote queue must be readable at a glance. What must be chosen first?

Domain: Create intelligent applications

- A. Create a public view for the shared filtered list
- B. Choose the view columns before setting the filter
- C. Write FetchXML for the view to get the exact rows
- D. Filter the view on the columns the team actually searches

### 28. A maker writes FetchXML for a standard quote view. What is the maintenance objection?

Domain: Create intelligent applications

- A. Write FetchXML for the view to get the exact rows
- B. Create a public view for the shared filtered list
- C. Filter the view on the columns the team actually searches
- D. Choose the view columns before setting the filter

### 29. A queue must show only open quotes in this territory and stay readable. Which two choices apply? Select two.

Domain: Create intelligent applications

- A. Rely on each user's personal view of the table
- B. Write FetchXML for the view to get the exact rows
- C. Filter the view on the columns the team actually searches
- D. Choose the view columns before setting the filter
- E. Create a public view for the shared filtered list

### 30. A territory summary page does not exist and a draft is needed this week. What should be done?

Domain: Create intelligent applications

- A. Generate the page from a natural-language description, then refine it
- B. Organize the long form into tabs and sections
- C. Publish the generated page without reviewing its data bindings
- D. Replace the main form with the generated page

### 31. A generated page displays a margin column the audience should not read. What was missed?

Domain: Create intelligent applications

- A. Hide the field with a JavaScript web resource
- B. Publish the generated page without reviewing its data bindings
- C. Generate the page from a natural-language description, then refine it
- D. Replace the main form with the generated page

### 32. The rep app must expose three forms and two views. What decides that?

Domain: Create intelligent applications

- A. Share the app only and rely on the app for access
- B. Configure the navigation in the sitemap designer
- C. Share the app and assign the security role that backs it
- D. Add the forms, views, and pages to the app in the app designer

### 33. A new rep can open the app but sees no quotes. What is missing?

Domain: Create intelligent applications

- A. Share the app and assign the security role that backs it
- B. Share the app only and rely on the app for access
- C. Add the forms, views, and pages to the app in the app designer
- D. Configure the navigation in the sitemap designer

### 34. A manager wants the win-rate trend without a second query definition. What should be created?

Domain: Create intelligent applications

- A. Build the chart in Power BI and embed it
- B. Filter the view on the columns the team actually searches
- C. Add the chart and the views to a dashboard
- D. Create the chart on the view for the trend

### 35. A rep app must exist over two tables by Friday. What should the maker do first?

Domain: Create intelligent applications

- A. Use the phone layout for field staff
- B. Write the filter so the data source performs the delegation
- C. Generate a canvas app from the data source
- D. Use the tablet layout for desk-based users

### 36. A rep app must search 300,000 quote rows. What must the filter do?

Domain: Create intelligent applications

- A. Generate a canvas app from the data source
- B. Filter in Power Fx after loading the rows into the app
- C. Collect the rows into a collection for in-memory work
- D. Write the filter so the data source performs the delegation

### 37. A rep app must handle a large table and fit a phone and a tablet. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Filter in Power Fx after loading the rows into the app
- B. Fix the layout to one pixel width so it always looks the same
- C. Write the filter so the data source performs the delegation
- D. Collect the rows into a collection for in-memory work
- E. Use responsive containers so the layout adapts to the device

### 38. One rep app must serve a phone on a visit and a tablet at a trade show. What should be used?

Domain: Create intelligent applications

- A. Use the phone layout for field staff
- B. Use the tablet layout for desk-based users
- C. Use responsive containers so the layout adapts to the device
- D. Fix the layout to one pixel width so it always looks the same

### 39. A retailer-facing app must work with a screen reader. What must be added?

Domain: Create intelligent applications

- A. Add accessible labels and screen-reader text to the controls
- B. Convey status with colour alone
- C. Fix the layout to one pixel width so it always looks the same
- D. Filter in Power Fx after loading the rows into the app

### 40. Three apps must share one distributor header. What should be used?

Domain: Create intelligent applications

- A. Define a named formula for the shared calculation
- B. Create a user-defined function for the reused expression
- C. Publish a component library for the shared header and controls
- D. Copy the screen into every app that needs it

### 41. A shared margin calculation takes three inputs. What should be used?

Domain: Create intelligent applications

- A. Create a user-defined function for the reused expression
- B. Copy the screen into every app that needs it
- C. Publish a component library for the shared header and controls
- D. Define a named formula for the shared calculation

### 42. Several apps must share one header and one margin calculation. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Copy the screen into every app that needs it
- B. Define a named formula for the shared calculation
- C. Fix the layout to one pixel width so it always looks the same
- D. Publish a component library for the shared header and controls
- E. Create a user-defined function for the reused expression

### 43. The signed-in rep's territory must be available on every screen. What should be used?

Domain: Create intelligent applications

- A. Clear the collection when the screen changes
- B. Use a global variable for the value that the whole app needs
- C. Collect the rows into a collection for in-memory work
- D. Use a context variable scoped to the screen

### 44. A save takes ten seconds and nobody knows which call is slow. What should be used?

Domain: Create intelligent applications

- A. Use Monitor to inspect the network call and the formula that fired
- B. Run the app in Test Studio before publishing
- C. Write a Trace message for the support team
- D. Wrap the call in IfError and surface the message to the user

### 45. A rep wants to ask about a quote inside the app. What should be added?

Domain: Create intelligent applications

- A. Call the agent's endpoint directly from Power Fx
- B. Build a custom Copilot Studio agent for every requirement
- C. Add the Copilot Studio agent to the canvas app as a component
- D. Build a second canvas app just to host the agent

### 46. A rep app must be composed and released. Which sequence is correct?

Domain: Create intelligent applications

- A. Assign the backing security role → configure the forms and views → set the navigation → compose the app → share the app
- B. Share the app → assign the backing security role → configure the forms and views → compose the app → set the navigation
- C. Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role
- D. Set the navigation in the sitemap → share the app → configure the forms and views → compose the app → assign the role

### 47. A rep app must reach users without a broken save. Which sequence is correct?

Domain: Create intelligent applications

- A. Publish the app → connect the data source → build the screens → add error handling → test with Monitor and Test Studio
- B. Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app
- C. Build the screens → test with Monitor → connect the data source → publish the app → add error handling
- D. Add error handling → connect the data source → test with Monitor → build the screens → publish the app

### 48. A quote record must start pricing approval the moment it is submitted. What should be used?

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Use a manually triggered flow from the app
- C. Expose an HTTP request trigger with a signed URL
- D. Use an automated trigger on record creation

### 49. The warehouse API must start a flow when stock is reserved. What should be used?

Domain: Build business application logic and automation

- A. Use an automated trigger on record creation
- B. Expose an HTTP request trigger with a signed URL
- C. Use a scheduled trigger for the nightly batch
- D. Use a manually triggered flow from the app

### 50. A flow must run only when a discount exceeds the band. What should be used?

Domain: Build business application logic and automation

- A. Use an automated trigger on record creation
- B. Trigger on every update so nothing is missed
- C. Trigger when a chosen column changes, with a filter condition
- D. Use a scheduled trigger for the nightly batch

### 51. The flow reads and writes Dataverse quotes. Which connector fits?

Domain: Build business application logic and automation

- A. Use the standard Dataverse connector
- B. Use the premium connector the source requires
- C. Build a custom connector for the internal API
- D. Copy the data into Excel to avoid a premium connector

### 52. The warehouse exposes a REST API behind a corporate gateway. What should be built?

Domain: Build business application logic and automation

- A. Use the standard Dataverse connector
- B. Copy the data into Excel to avoid a premium connector
- C. Use the premium connector the source requires
- D. Build a custom connector for the internal API

### 53. A discount above the band must be signed off before the quote is sent. What action fits?

Domain: Build business application logic and automation

- A. Start and wait for an approval
- B. Choose the approval type that matches the sign-off the process requires
- C. Send parallel approvals and require every response
- D. Send an email and treat silence as approval

### 54. The pricing lead and the sales director must both approve a large discount. Which approval type fits?

Domain: Build business application logic and automation

- A. Send an email and treat silence as approval
- B. Start and wait for an approval
- C. Send parallel approvals and require every response
- D. Choose the approval type that matches the sign-off the process requires

### 55. A downstream action expects one object built from three quote fields. What should be used?

Domain: Build business application logic and automation

- A. Use Compose to shape the payload the next step consumes
- B. Apply to each over the returned rows
- C. Add a condition to branch on the status
- D. Parse JSON so later steps can use the fields

### 56. A returned stock body is opaque and the designer offers no properties. What should be added?

Domain: Build business application logic and automation

- A. Apply to each over the returned rows
- B. Add a condition to branch on the status
- C. Parse JSON so later steps can use the fields
- D. Use Compose to shape the payload the next step consumes

### 57. A response contains fifty quote lines that must each be priced. What should be used?

Domain: Build business application logic and automation

- A. Use a switch for the multi-way branch
- B. Add a condition to branch on the status
- C. Use Do until with a bounded count for the retry loop
- D. Apply to each over the returned rows

### 58. A flow takes one of two paths based on the discount amount. What should be used?

Domain: Build business application logic and automation

- A. Apply to each over the returned rows
- B. Use a switch for the multi-way branch
- C. Use Do until with a bounded count for the retry loop
- D. Add a condition to branch on the status

### 59. A flow branches five ways by quote type. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Use a switch for the multi-way branch
- C. Add a condition to branch on the status
- D. Wrap the steps in a Scope so one error path handles the failures

### 60. An approval reaches the wrong approver and the failure text is generic. What reveals the resolved value?

Domain: Build business application logic and automation

- A. Read the run history to find the failed action and its inputs
- B. Resubmit the failed run after the fix
- C. Turn on static result to test the rest of the flow
- D. Test the flow with the real trigger payload

### 61. A new pricing flow must be proven with the real trigger payload. What should be done?

Domain: Build business application logic and automation

- A. Turn on static result to test the rest of the flow
- B. Read the run history to find the failed action and its inputs
- C. Test the flow with the real trigger payload
- D. Resubmit the failed run after the fix

### 62. A quote summary prompt must start from a tested instruction. What should be used?

Domain: Build business application logic and automation

- A. Start from a prompt template in AI Hub
- B. Build the prompt from blank
- C. Add typed inputs so the prompt takes values
- D. Copy the prompt text into each app so it can be tuned per app

### 63. A prompt must take the customer requirement as a value each run. What should be added?

Domain: Build business application logic and automation

- A. Add the knowledge source so the prompt grounds on approved content
- B. Copy the prompt text into each app so it can be tuned per app
- C. Choose the model that fits the task instead of the largest available
- D. Add typed inputs so the prompt takes values

### 64. A summary must cite the approved pricing policy. What should be attached?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Add the knowledge source so the prompt grounds on approved content
- C. Copy the prompt text into each app so it can be tuned per app
- D. Choose the model that fits the task instead of the largest available

### 65. A summary prompt runs on a large model although its quality is already acceptable. What should change?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Add the knowledge source so the prompt grounds on approved content
- C. Choose the model that fits the task instead of the largest available
- D. Add typed inputs so the prompt takes values

### 66. A rep must generate the summary while looking at the quote. What should be used?

Domain: Build business application logic and automation

- A. Call the prompt from the canvas app through its connector
- B. Choose the model that fits the task instead of the largest available
- C. Call the prompt from the cloud flow action
- D. Copy the prompt text into each app so it can be tuned per app

### 67. The summary must be written to the record during the overnight run. What should be used?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Call the prompt from the cloud flow action
- C. Add typed inputs so the prompt takes values
- D. Call the prompt from the canvas app through its connector

### 68. A custom AI Hub model must be called from the rep app with authentication in one place. What should be used?

Domain: Build business application logic and automation

- A. Call the prompt from the canvas app through its connector
- B. Consume the AI Hub model through the same connector pattern as a prompt
- C. Copy the prompt text into each app so it can be tuned per app
- D. Call the model from the flow and store the result on the record

### 69. A demand model must be called from the flow and its forecast stored on the quote. What should be used?

Domain: Build business application logic and automation

- A. Call the model from the flow and store the result on the record
- B. Call the prompt from the canvas app through its connector
- C. Call the prompt from the cloud flow action
- D. Consume the AI Hub model through the same connector pattern as a prompt

### 70. A discount reason must be required whenever the discount is non-zero. What should be used?

Domain: Build business application logic and automation

- A. Hide the field with a JavaScript web resource
- B. Add a JavaScript web resource to the form
- C. Configure a business rule on the table
- D. Set the business rule scope to the table so it applies in every form

### 71. An order needs different stages for custom and standard pumps. What should be used?

Domain: Build business application logic and automation

- A. Keep every case type in one linear process to stay simple
- B. Use a formula column where the rule needs Power Fx
- C. Branch the business process flow on the case type
- D. Model the stages in a business process flow

### 72. An order must move through four ordered stages with required information. What should be built?

Domain: Build business application logic and automation

- A. Branch the business process flow on the case type
- B. Configure a business rule on the table
- C. Use a rollup column to aggregate the child records
- D. Model the stages in a business process flow

### 73. A customer needs a running total of committed order value. What should be used?

Domain: Build business application logic and automation

- A. Use a calculated column for the value that must never change
- B. Use a formula column where the rule needs Power Fx
- C. Use a rollup column to aggregate the child records
- D. Write a plug-in to set the value on every update

### 74. A margin must recalculate from two columns whenever either changes. What should be used?

Domain: Build business application logic and automation

- A. Write a plug-in to set the value on every update
- B. Use a formula column where the rule needs Power Fx
- C. Use a rollup column to aggregate the child records
- D. Use a calculated column for the value that must never change

### 75. Each rule has a different reach: form only, every save, or read time. What determines that choice?

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Pick the logic mechanism that matches where the rule must hold
- C. Enforce the rule in a synchronous plug-in when it must run on every write
- D. Use a formula column where the rule needs Power Fx

### 76. A flow must start on a submitted quote but only when the discount exceeds the band. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Trigger when a chosen column changes, with a filter condition
- B. Expose an HTTP request trigger with a signed URL
- C. Use a scheduled trigger for the nightly batch
- D. Trigger on every update so nothing is missed
- E. Use an automated trigger on record creation

### 77. A discount sign-off must pause the process and match the approval rule. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Send an email and treat silence as approval
- B. Chain two approvals in sequence for the second-level sign-off
- C. Choose the approval type that matches the sign-off the process requires
- D. Start and wait for an approval
- E. Use a scheduled trigger for the nightly batch

### 78. A group of pricing steps needs one failure path that fires. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Wrap the steps in a Scope so one error path handles the failures
- B. Turn on concurrency control for the loop
- C. Use a switch for the multi-way branch
- D. Configure run after so the failure path actually executes
- E. Add a condition to branch on the status

### 79. A failing pricing flow must be diagnosed and proven. Which two practices apply? Select two.

Domain: Build business application logic and automation

- A. Resubmit the failed run after the fix
- B. Turn on static result to test the rest of the flow
- C. Parse JSON so later steps can use the fields
- D. Test the flow with the real trigger payload
- E. Read the run history to find the failed action and its inputs

### 80. A knowledge-grounded summary must start from a reviewed instruction. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Choose the model that fits the task instead of the largest available
- B. Start from a prompt template in AI Hub
- C. Add the knowledge source so the prompt grounds on approved content
- D. Copy the prompt text into each app so it can be tuned per app
- E. Build the prompt from blank

### 81. A prompt must accept a policy number per call and stay inside budget. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Start from a prompt template in AI Hub
- B. Add typed inputs so the prompt takes values
- C. Add the knowledge source so the prompt grounds on approved content
- D. Copy the prompt text into each app so it can be tuned per app
- E. Choose the model that fits the task instead of the largest available

### 82. A check must fire for a user editing a form and for a record written by an integration. Which two mechanisms apply? Select two.

Domain: Build business application logic and automation

- A. Enforce the rule in a synchronous plug-in when it must run on every write
- B. Hide the field with a JavaScript web resource
- C. Configure a business rule on the table
- D. Use a calculated column for the value that must never change
- E. Add a JavaScript web resource to the form

### 83. A margin must recalculate and a customer must show committed order value. Which two column types apply? Select two.

Domain: Build business application logic and automation

- A. Write a plug-in to set the value on every update
- B. Use a formula column where the rule needs Power Fx
- C. Use a rollup column to aggregate the child records
- D. Configure a business rule on the table
- E. Use a calculated column for the value that must never change

### 84. A pricing workflow must reach production without wrong expressions. Which sequence is correct?

Domain: Build business application logic and automation

- A. Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run
- B. Read the run history → add the trigger → decide which event starts the process → add the actions → test with a real payload
- C. Test with a real payload → decide which event starts the process → read the run history → add the trigger → add the actions
- D. Add the actions and branches → add the trigger → test with a real payload → decide which event starts the process → read the run history

### 85. A discount must be decided and the decision recorded. Which sequence is correct?

Domain: Build business application logic and automation

- A. Notify the requester → update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome
- B. Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester
- C. Update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome → notify the requester
- D. Branch on the outcome → trigger on the submitted request → notify the requester → start and wait for the approval → update the record

### 86. A discount rule must hold on the form and through an import. Which sequence is correct?

Domain: Build business application logic and automation

- A. Document it for the support team → test it through an import → choose the mechanism → state the rule → configure the rule
- B. Test it on the form → configure the rule → state the rule in business terms → choose the mechanism → document it
- C. Configure the rule at table scope → state the rule in business terms → document it → test it through an import → choose the mechanism
- D. State the rule in business terms → choose the mechanism that enforces it where it must hold → configure the rule at table scope → test it on the form and through an import → document it for the support team

### 87. An order process must guide users through four stages. Which sequence is correct?

Domain: Build business application logic and automation

- A. Define the stages the record moves through → choose the columns each stage requires → branch the process where the case types diverge → test a record through every stage → hand the process to the users
- B. Test a record through every stage → branch the process → define the stages → hand the process to the users → choose the columns
- C. Branch the process → define the stages → hand the process to the users → test a record through every stage → choose the columns each stage requires
- D. Choose the columns each stage requires → hand the process to the users → test a record → define the stages → branch the process

### 88. A release needs the screens verified and a slow action timed. Which two tools apply? Select two.

Domain: Create intelligent applications

- A. Use Monitor to inspect the network call and the formula that fired
- B. Wrap the call in IfError and surface the message to the user
- C. Write a Trace message for the support team
- D. Run the app in Test Studio before publishing
- E. Call the agent's endpoint directly from Power Fx

---

## Case study — Lakeshore Retail Group

Lakeshore Retail Group operates 60 stores and an e-commerce site. Customer service handles 5,000 contacts a month across phone, email, and chat, and agents cannot see a customer's order history without switching systems. The group wants a unified case record, an AI-drafted reply that an agent must review, a routing rule by contact reason, and a satisfaction survey after closure. The group has Copilot Studio, Dataverse, and a governance board that requires every AI feature to be reviewed before release.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. A case must point at its customer record. What should be added?

Domain: Create a foundation for intelligent applications

- A. Use a lookup column instead of storing the name as text
- B. Add a choice column for the fixed set of options
- C. Use a currency column with the record currency
- D. Store the account name as text so the form stays simple

### 90. Three apps share one service header. What should be used?

Domain: Create intelligent applications

- A. Define a named formula for the shared calculation
- B. Publish a component library for the shared header and controls
- C. Copy the screen into every app that needs it
- D. Create a user-defined function for the reused expression

### 91. AI-drafted replies must be affordable on every case. What should be chosen deliberately?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Copy the prompt text into each app so it can be tuned per app
- C. Choose the model that fits the task instead of the largest available
- D. Add the knowledge source so the prompt grounds on approved content

---

## Case study — Margie Travel

Margie Travel books corporate travel for 200 client companies. Consultants email itineraries, and the finance team reconciles invoices against bookings by hand. Travellers need an approval before a booking above their policy limit, and clients want a portal showing their own bookings only. The agency has 40 staff, Dataverse, and a Power Automate premium licence. Consultants work from phones while travelling. The agency's insurer requires that every policy exception be recorded with the approver and the reason.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Consultants must not see another client company's bookings. What partitions the data?

Domain: Create a foundation for intelligent applications

- A. Use a field security profile for the sensitive column
- B. Move the user to another business unit to fix access
- C. Assign the record to a team that the group owns
- D. Assign a security role that grants only the privileges the role needs

### 93. Consultants book from phones while travelling. Which design obligation applies?

Domain: Create intelligent applications

- A. Filter in Power Fx after loading the rows into the app
- B. Add accessible labels and screen-reader text to the controls
- C. Convey status with colour alone
- D. Use responsive containers so the layout adapts to the device

### 94. A booking above the policy limit needs one named decision. Which approval type fits?

Domain: Build business application logic and automation

- A. Send an email and treat silence as approval
- B. Start and wait for an approval
- C. Choose the approval type that matches the sign-off the process requires
- D. Send parallel approvals and require every response

---

## Case study — VanArsdel Manufacturing

VanArsdel Manufacturing builds industrial pumps to order. Each order runs through engineering review, costing, production, and shipping, and the handoffs happen by email. Costing frequently restarts because engineering changes a specification after the quote was issued. The operations director wants a stage-based order process with required fields, an approval when a costing change exceeds 10 percent, and a project dashboard. Engineering and costing are separate business units with separate managers. The company has Dataverse and has asked for an AI summary of each order's change history.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. An audit asks who changed a costing after the quote. What must be enabled?

Domain: Create a foundation for intelligent applications

- A. Configure table properties such as ownership and auditing
- B. Configure a row summary to summarize the record text
- C. Use a field security profile for the sensitive column
- D. Enable auditing on the tables that hold regulated data

### 96. Users cannot find the costing area in the app. What should be configured?

Domain: Create intelligent applications

- A. Add the forms, views, and pages to the app in the app designer
- B. Share the app only and rely on the app for access
- C. Share the app and assign the security role that backs it
- D. Configure the navigation in the sitemap designer

### 97. A costing change flow branches by change type. What should be used?

Domain: Build business application logic and automation

- A. Wrap the steps in a Scope so one error path handles the failures
- B. Add a condition to branch on the status
- C. Use a switch for the multi-way branch
- D. Use Do until with a bounded count for the retry loop

---

## Case study — Wide World Importers

Wide World Importers distributes 8,000 SKUs to 3,000 retail accounts across two countries. Sales reps use a quoting spreadsheet that is emailed between the rep, the pricing team, and the customer. Quotes above a discount threshold need pricing approval, and reps frequently quote stock the warehouse does not hold. The company wants a rep app, an approval flow, a stock check against the warehouse system, and a quote PDF. The warehouse exposes a REST API behind a corporate gateway. The company is migrating from on-premises CRM to Dataverse and must keep historical quotes readable.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Every rep must see the same open-quote list. What should be created?

Domain: Create a foundation for intelligent applications

- A. Change the system view so the list order suits the team
- B. Rely on each user's personal view of the table
- C. Create a public view for the shared filtered list
- D. Add a quick-create form for entry from a lookup

### 99. A quote queue must show only quotes awaiting pricing. What decides that?

Domain: Create intelligent applications

- A. Write FetchXML for the view to get the exact rows
- B. Choose the view columns before setting the filter
- C. Create a public view for the shared filtered list
- D. Filter the view on the columns the team actually searches

### 100. The warehouse API needs its own authentication. What should be built?

Domain: Build business application logic and automation

- A. Use the standard Dataverse connector
- B. Build a custom connector for the internal API
- C. Use the premium connector the source requires
- D. Copy the data into Excel to avoid a premium connector

---

## Answer key and explanations

### Question 1 — C

Answer: Map each requirement to the Power Platform component that fits it. Mapping requirements to components keeps the solution minimal. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.
- **B:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.
- **C:** Correct. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. In this case: Mapping requirements to components keeps the solution minimal.
- **D:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: Mapping requirements to components keeps the solution minimal.

### Question 2 — D

Answer: Deliver every requirement as a single model-driven app. One app widens access to every table it contains. One app for everything widens access and makes the smallest change a release of the whole solution. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Why the correct answer wins: One app widens access to every table it contains.
- **B:** Incorrect for this question. A deliberate later replacement rarely happens, and meanwhile two implementations must be maintained. Why the correct answer wins: One app widens access to every table it contains.
- **C:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: One app widens access to every table it contains.
- **D:** Correct. One app for everything widens access and makes the smallest change a release of the whole solution. In this case: One app widens access to every table it contains.

### Question 3 — A

Answer: Build a working prototype in a week and let the business react to it. A prototype answers questions sooner, though it does not settle which component owns the logic. A prototype answers questions sooner, but it does not settle which component should own the logic. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A prototype answers questions sooner, but it does not settle which component should own the logic. In this case: A prototype answers questions sooner, though it does not settle which component owns the logic.
- **B:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: A prototype answers questions sooner, though it does not settle which component owns the logic.
- **C:** Incorrect for this question. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Why the correct answer wins: A prototype answers questions sooner, though it does not settle which component owns the logic.
- **D:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: A prototype answers questions sooner, though it does not settle which component owns the logic.

### Question 4 — B

Answer: Adopt the built-in agent that already covers the task. A built-in agent is maintained by the platform and carries less build cost. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **B:** Correct. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. In this case: A built-in agent is maintained by the platform and carries less build cost.
- **C:** Incorrect for this question. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.
- **D:** Incorrect for this question. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Why the correct answer wins: A built-in agent is maintained by the platform and carries less build cost.

### Question 5 — A

Answer: Build a Power Apps component framework control. A PCF control covers a visual the standard control cannot express. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. In this case: A PCF control covers a visual the standard control cannot express.
- **B:** Incorrect for this question. A deliberate later replacement rarely happens, and meanwhile two implementations must be maintained. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **C:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.

### Question 6 — B

Answer: Choose the environment type that matches the data boundary and the licence. Environment type sets the boundary and licensing. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: Environment type sets the boundary and licensing.
- **B:** Correct. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. In this case: Environment type sets the boundary and licensing.
- **C:** Incorrect for this question. The default environment has the widest membership and the least governance, which is where a regulated solution should not start. Why the correct answer wins: Environment type sets the boundary and licensing.
- **D:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: Environment type sets the boundary and licensing.

### Question 7 — C

Answer: Package the customizations in a solution before moving them. A solution is the unit of deployment. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: A solution is the unit of deployment.
- **B:** Incorrect for this question. A pipeline records the deployment and runs the same solution through each stage. Why the correct answer wins: A solution is the unit of deployment.
- **C:** Correct. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. In this case: A solution is the unit of deployment.
- **D:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: A solution is the unit of deployment.

### Question 8 — D, E

Answers: Define the solution publisher and prefix once, before the first table; Promote a managed solution to test and production. The publisher fixes the prefix, and the managed import is removable. The prefix is baked into every schema name and is expensive to change after data exists. A managed solution is locked, so it can be upgraded and removed predictably. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **B:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **C:** Incorrect for this question. Building in production removes the test step and puts every unfinished change in front of users. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **D:** Correct. The prefix is baked into every schema name and is expensive to change after data exists. In this case: The publisher fixes the prefix, and the managed import is removable.
- **E:** Correct. A managed solution is locked, so it can be upgraded and removed predictably. In this case: The publisher fixes the prefix, and the managed import is removable.

### Question 9 — D

Answer: Keep the records in a SharePoint list and skip Dataverse. A list has no relationships, security roles, or rollup columns. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **B:** Incorrect for this question. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **C:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **D:** Correct. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. In this case: A list has no relationships, security roles, or rollup columns.

### Question 10 — A

Answer: Extend the standard table instead of creating a duplicate. Extending the standard table keeps the built-in relationships. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. In this case: Extending the standard table keeps the built-in relationships.
- **B:** Incorrect for this question. A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **C:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: Extending the standard table keeps the built-in relationships.
- **D:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: Extending the standard table keeps the built-in relationships.

### Question 11 — B

Answer: Configure table properties such as ownership and auditing. Ownership and auditing are table properties. Ownership decides who can see a row and auditing decides whether its history survives an investigation. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Auditing records who changed which column and when, which is what an audit asks for. Why the correct answer wins: Ownership and auditing are table properties.
- **B:** Correct. Ownership decides who can see a row and auditing decides whether its history survives an investigation. In this case: Ownership and auditing are table properties.
- **C:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Ownership and auditing are table properties.
- **D:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: Ownership and auditing are table properties.

### Question 12 — A

Answer: Add a choice column for the fixed set of options. A choice constrains input to the approved list. A choice constrains input to the approved list and renders as a dropdown on every form. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A choice constrains input to the approved list and renders as a dropdown on every form. In this case: A choice constrains input to the approved list.
- **B:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A choice constrains input to the approved list.
- **C:** Incorrect for this question. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Why the correct answer wins: A choice constrains input to the approved list.
- **D:** Incorrect for this question. One global choice keeps the list consistent instead of drifting across tables. Why the correct answer wins: A choice constrains input to the approved list.

### Question 13 — A

Answer: Use a lookup column instead of storing the name as text. A lookup stores a reference to the related row, so the item name is never copied. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. In this case: A lookup stores a reference to the related row, so the item name is never copied.
- **B:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.
- **C:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.
- **D:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.

### Question 14 — B, C

Answers: Use a currency column with the record currency; Use a decimal column for an exact rate. A currency column pairs amount and currency, and a decimal avoids rounding drift. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. A decimal avoids the rounding drift that a floating-point column introduces in a rate. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A currency column pairs amount and currency, and a decimal avoids rounding drift.
- **B:** Correct. A decimal avoids the rounding drift that a floating-point column introduces in a rate. In this case: A currency column pairs amount and currency, and a decimal avoids rounding drift.
- **C:** Correct. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. In this case: A currency column pairs amount and currency, and a decimal avoids rounding drift.
- **D:** Incorrect for this question. An auto-number gives every record a readable, unique reference that users can quote. Why the correct answer wins: A currency column pairs amount and currency, and a decimal avoids rounding drift.
- **E:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A currency column pairs amount and currency, and a decimal avoids rounding drift.

### Question 15 — D

Answer: Configure a one-to-many relationship with a lookup on the child table. A one-to-many relationship with the lookup on the child is the standard shape. The lookup on the child is what makes the parent select a record rather than a typed string. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **B:** Incorrect for this question. Referential behaviour leaves the children in place, which is what a shared dimension needs. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **C:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: A one-to-many relationship with the lookup on the child is the standard shape.
- **D:** Correct. The lookup on the child is what makes the parent select a record rather than a typed string. In this case: A one-to-many relationship with the lookup on the child is the standard shape.

### Question 16 — D

Answer: Set the relationship behaviour to parental so child records are removed with the parent. Parental behaviour removes the child when the parent is deleted. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The lookup on the child is what makes the parent select a record rather than a typed string. Why the correct answer wins: Parental behaviour removes the child when the parent is deleted.
- **B:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: Parental behaviour removes the child when the parent is deleted.
- **C:** Incorrect for this question. Referential behaviour leaves the children in place, which is what a shared dimension needs. Why the correct answer wins: Parental behaviour removes the child when the parent is deleted.
- **D:** Correct. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. In this case: Parental behaviour removes the child when the parent is deleted.

### Question 17 — C

Answer: Design the main form around the record the user opens. The main form carries the fields the role uses. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A card form gives a compact editing surface for a handful of fields. Why the correct answer wins: The main form carries the fields the role uses.
- **B:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: The main form carries the fields the role uses.
- **C:** Correct. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. In this case: The main form carries the fields the role uses.
- **D:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: The main form carries the fields the role uses.

### Question 18 — B

Answer: Add a quick-create form for entry from a lookup. A quick-create form creates the related record in place. A quick-create form lets a user create the related record without leaving the current one. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A card form gives a compact editing surface for a handful of fields. Why the correct answer wins: A quick-create form creates the related record in place.
- **B:** Correct. A quick-create form lets a user create the related record without leaving the current one. In this case: A quick-create form creates the related record in place.
- **C:** Incorrect for this question. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Why the correct answer wins: A quick-create form creates the related record in place.
- **D:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A quick-create form creates the related record in place.

### Question 19 — A, B

Answers: Create a public view for the shared filtered list; Design the main form around the record the user opens. The public view is the shared list, and the main form is the working surface. A public view is available to everyone with access to the table, so the team sees the same list. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. In this case: The public view is the shared list, and the main form is the working surface.
- **B:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: The public view is the shared list, and the main form is the working surface.
- **C:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **D:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **E:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.

### Question 20 — C

Answer: Assign a security role that grants only the privileges the role needs. A security role grants privileges at a scope. A security role is how Dataverse decides create, read, write, and delete per table. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A security role grants privileges at a scope.
- **B:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: A security role grants privileges at a scope.
- **C:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: A security role grants privileges at a scope.
- **D:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A security role grants privileges at a scope.

### Question 21 — D

Answer: Use a field security profile for the sensitive column. A field security profile hides a column without hiding the record. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **B:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **C:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **D:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: A field security profile hides a column without hiding the record.

### Question 22 — A, D

Answers: Assign a security role that grants only the privileges the role needs; Use a field security profile for the sensitive column. The role grants table privileges, and the profile hides the column. A security role is how Dataverse decides create, read, write, and delete per table. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: The role grants table privileges, and the profile hides the column.
- **B:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **C:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **D:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: The role grants table privileges, and the profile hides the column.
- **E:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: The role grants table privileges, and the profile hides the column.

### Question 23 — B

Answer: Map the requirement to a component → check whether a built-in agent covers it → pilot the agent in development → measure the outcome → adopt or extend it. Coverage is tested with a pilot before committing to a custom build. Coverage is tested with a pilot before anyone commits to a custom build. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Adopting before a pilot skips the step that would have caught the gap. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **B:** Correct. Coverage is tested with a pilot before anyone commits to a custom build. In this case: Coverage is tested with a pilot before committing to a custom build.
- **C:** Incorrect for this question. There is nothing to measure before a pilot exists. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.
- **D:** Incorrect for this question. Building first pays the custom-agent cost before coverage is even known. Why the correct answer wins: Coverage is tested with a pilot before committing to a custom build.

### Question 24 — D

Answer: Define the publisher prefix → build unmanaged in development → export the solution → import managed into test → deploy managed to production. The prefix is fixed before schema names exist, and each environment receives a managed copy. The prefix is fixed before schema names exist, and each later environment receives a managed copy rather than an edit. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A managed import cannot precede the unmanaged build it is supposed to carry. Why the correct answer wins: The prefix is fixed before schema names exist, and each environment receives a managed copy.
- **B:** Incorrect for this question. Building in production exposes unfinished work, and a prefix chosen afterwards leaves the schema names inconsistent. Why the correct answer wins: The prefix is fixed before schema names exist, and each environment receives a managed copy.
- **C:** Incorrect for this question. Exporting before the solution exists and testing after production both break the promotion order. Why the correct answer wins: The prefix is fixed before schema names exist, and each environment receives a managed copy.
- **D:** Correct. The prefix is fixed before schema names exist, and each later environment receives a managed copy rather than an edit. In this case: The prefix is fixed before schema names exist, and each environment receives a managed copy.

### Question 25 — C

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A form carries the working set of fields for the role.
- **C:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 26 — D

Answer: Organize the long form into tabs and sections. Tabs keep a long form scannable. Tabs keep a forty-column form scannable without hiding the fields behind a click. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A card form gives a compact editing surface for a handful of fields. Why the correct answer wins: Tabs keep a long form scannable.
- **B:** Incorrect for this question. A form carries the working set of fields; everything else belongs in a tab or a view. Why the correct answer wins: Tabs keep a long form scannable.
- **C:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: Tabs keep a long form scannable.
- **D:** Correct. Tabs keep a forty-column form scannable without hiding the fields behind a click. In this case: Tabs keep a long form scannable.

### Question 27 — B

Answer: Choose the view columns before setting the filter. The columns decide what is readable without opening the record. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The columns decide what is readable without opening the record.
- **B:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The columns decide what is readable without opening the record.
- **C:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The columns decide what is readable without opening the record.
- **D:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: The columns decide what is readable without opening the record.

### Question 28 — A

Answer: Write FetchXML for the view to get the exact rows. FetchXML bypasses the visual designer the next maker will use. FetchXML is powerful but bypasses the visual designer the next maker will use. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. FetchXML is powerful but bypasses the visual designer the next maker will use. In this case: FetchXML bypasses the visual designer the next maker will use.
- **B:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: FetchXML bypasses the visual designer the next maker will use.
- **C:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: FetchXML bypasses the visual designer the next maker will use.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: FetchXML bypasses the visual designer the next maker will use.

### Question 29 — C, D

Answers: Filter the view on the columns the team actually searches; Choose the view columns before setting the filter. The filter decides the rows, and the columns make them readable. The filter decides which records appear, so it must match the question the list answers. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **B:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **C:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides the rows, and the columns make them readable.
- **D:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The filter decides the rows, and the columns make them readable.
- **E:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides the rows, and the columns make them readable.

### Question 30 — A

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close, and the maker owns the bindings. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close, and the maker owns the bindings.
- **B:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **C:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.
- **D:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close, and the maker owns the bindings.

### Question 31 — B

Answer: Publish the generated page without reviewing its data bindings. An unreviewed generated page can bind to data the audience is not entitled to. An unreviewed page can bind to a table the audience should not read. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.
- **B:** Correct. An unreviewed page can bind to a table the audience should not read. In this case: An unreviewed generated page can bind to data the audience is not entitled to.
- **C:** Incorrect for this question. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.
- **D:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: An unreviewed generated page can bind to data the audience is not entitled to.

### Question 32 — D

Answer: Add the forms, views, and pages to the app in the app designer. The app designer decides which components the app exposes. The app designer decides which components the app exposes, so composition is a security-relevant choice. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The app designer decides which components the app exposes.
- **B:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: The app designer decides which components the app exposes.
- **C:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The app designer decides which components the app exposes.
- **D:** Correct. The app designer decides which components the app exposes, so composition is a security-relevant choice. In this case: The app designer decides which components the app exposes.

### Question 33 — A

Answer: Share the app and assign the security role that backs it. Sharing grants the app and the role grants the data. Sharing an app grants the app, and the role grants the data; both are needed. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Sharing an app grants the app, and the role grants the data; both are needed. In this case: Sharing grants the app and the role grants the data.
- **B:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **C:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **D:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: Sharing grants the app and the role grants the data.

### Question 34 — D

Answer: Create the chart on the view for the trend. A chart bound to a view reuses that view's filter. A chart bound to a view reuses that view's filter instead of duplicating it. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **C:** Incorrect for this question. A dashboard composes several components so a manager sees the whole picture on one page. Why the correct answer wins: A chart bound to a view reuses that view's filter.
- **D:** Correct. A chart bound to a view reuses that view's filter instead of duplicating it. In this case: A chart bound to a view reuses that view's filter.

### Question 35 — C

Answer: Generate a canvas app from the data source. Generating from data gives working screens immediately. Generating from data gives working screens over the chosen tables immediately. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Generating from data gives working screens immediately.
- **B:** Incorrect for this question. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Why the correct answer wins: Generating from data gives working screens immediately.
- **C:** Correct. Generating from data gives working screens over the chosen tables immediately. In this case: Generating from data gives working screens immediately.
- **D:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Generating from data gives working screens immediately.

### Question 36 — D

Answer: Write the filter so the data source performs the delegation. Delegation keeps the query on the source. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Generating from data gives working screens over the chosen tables immediately. Why the correct answer wins: Delegation keeps the query on the source.
- **B:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Delegation keeps the query on the source.
- **C:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: Delegation keeps the query on the source.
- **D:** Correct. Delegation sends the query to the source, so the app never downloads more rows than it can handle. In this case: Delegation keeps the query on the source.

### Question 37 — C, E

Answers: Write the filter so the data source performs the delegation; Use responsive containers so the layout adapts to the device. Delegation keeps the query on the source, and responsive containers fit both. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.
- **C:** Correct. Delegation sends the query to the source, so the app never downloads more rows than it can handle. In this case: Delegation keeps the query on the source, and responsive containers fit both.
- **D:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: Delegation keeps the query on the source, and responsive containers fit both.
- **E:** Correct. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. In this case: Delegation keeps the query on the source, and responsive containers fit both.

### Question 38 — C

Answer: Use responsive containers so the layout adapts to the device. Responsive containers reflow so one app fits both. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The phone layout controls the size and reach of controls on a handheld device. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **B:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: Responsive containers reflow so one app fits both.
- **C:** Correct. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. In this case: Responsive containers reflow so one app fits both.
- **D:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: Responsive containers reflow so one app fits both.

### Question 39 — A

Answer: Add accessible labels and screen-reader text to the controls. A control without a label is unusable with a screen reader. A control without a label is unusable with a screen reader, however clear it looks. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A control without a label is unusable with a screen reader, however clear it looks. In this case: A control without a label is unusable with a screen reader.
- **B:** Incorrect for this question. Colour alone fails for a colour-blind user and for anyone reading the app in high contrast. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **C:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **D:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: A control without a label is unusable with a screen reader.

### Question 40 — C

Answer: Publish a component library for the shared header and controls. A component library is the reusable, versioned home for a shared control. A component library is the reusable, versioned home for a control that several apps must share. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **B:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **C:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: A component library is the reusable, versioned home for a shared control.
- **D:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.

### Question 41 — A

Answer: Create a user-defined function for the reused expression. A user-defined function accepts parameters and returns a value for reuse. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. In this case: A user-defined function accepts parameters and returns a value for reuse.
- **B:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **C:** Incorrect for this question. A component library is the reusable, versioned home for a control that several apps must share. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.
- **D:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A user-defined function accepts parameters and returns a value for reuse.

### Question 42 — B, D

Answers: Publish a component library for the shared header and controls; Define a named formula for the shared calculation. The library shares the control, and the named formula shares the calculation. A component library is the reusable, versioned home for a control that several apps must share. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **B:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: The library shares the control, and the named formula shares the calculation.
- **C:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **D:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: The library shares the control, and the named formula shares the calculation.
- **E:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.

### Question 43 — B

Answer: Use a global variable for the value that the whole app needs. A global variable persists across screens. A global variable persists across screens, which is what a signed-in user's selection needs. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An un-cleared collection keeps the previous user's rows in memory. Why the correct answer wins: A global variable persists across screens.
- **B:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists across screens.
- **C:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists across screens.
- **D:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists across screens.

### Question 44 — A

Answer: Use Monitor to inspect the network call and the formula that fired. Monitor shows the request, response, and timing. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. In this case: Monitor shows the request, response, and timing.
- **B:** Incorrect for this question. Test Studio captures the screens and formulas that a regression would break. Why the correct answer wins: Monitor shows the request, response, and timing.
- **C:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Monitor shows the request, response, and timing.
- **D:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Monitor shows the request, response, and timing.

### Question 45 — C

Answer: Add the Copilot Studio agent to the canvas app as a component. The agent component adds a conversational surface to the app. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **B:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **C:** Correct. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. In this case: The agent component adds a conversational surface to the app.
- **D:** Incorrect for this question. A second app multiplies the maintenance without adding capability. Why the correct answer wins: The agent component adds a conversational surface to the app.

### Question 46 — C

Answer: Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role. The app is composed from finished components, and access is granted last. The app is composed from finished components, and access is granted last. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Granting data access before the app exists gives access with nothing to use it in. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **B:** Incorrect for this question. Sharing an app that has no components shows users an empty shell. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **C:** Correct. The app is composed from finished components, and access is granted last. In this case: The app is composed from finished components, and access is granted last.
- **D:** Incorrect for this question. Navigation is meaningless until the components exist. Why the correct answer wins: The app is composed from finished components, and access is granted last.

### Question 47 — B

Answer: Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app. The data source comes first, and testing precedes publishing. The data source comes first, and testing precedes publishing. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Publishing before testing is how a broken save reaches users. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **B:** Correct. The data source comes first, and testing precedes publishing. In this case: The data source comes first, and testing precedes publishing.
- **C:** Incorrect for this question. Screens need a data source, and publishing needs a tested app. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **D:** Incorrect for this question. Error handling has nothing to wrap before the calls exist. Why the correct answer wins: The data source comes first, and testing precedes publishing.

### Question 48 — D

Answer: Use an automated trigger on record creation. An automated trigger runs without a user. An automated trigger runs without a user, which is what a background rule needs. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: An automated trigger runs without a user.
- **B:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: An automated trigger runs without a user.
- **C:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: An automated trigger runs without a user.
- **D:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: An automated trigger runs without a user.

### Question 49 — B

Answer: Expose an HTTP request trigger with a signed URL. An HTTP trigger lets an external system start the flow. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: An HTTP trigger lets an external system start the flow.
- **B:** Correct. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. In this case: An HTTP trigger lets an external system start the flow.
- **C:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: An HTTP trigger lets an external system start the flow.
- **D:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: An HTTP trigger lets an external system start the flow.

### Question 50 — C

Answer: Trigger when a chosen column changes, with a filter condition. A column filter stops irrelevant updates. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A column filter stops irrelevant updates.
- **B:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: A column filter stops irrelevant updates.
- **C:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: A column filter stops irrelevant updates.
- **D:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: A column filter stops irrelevant updates.

### Question 51 — A

Answer: Use the standard Dataverse connector. The standard connector covers Dataverse natively. The standard connector is included in the base licence and covers Dataverse natively. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The standard connector is included in the base licence and covers Dataverse natively. In this case: The standard connector covers Dataverse natively.
- **B:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: The standard connector covers Dataverse natively.
- **C:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: The standard connector covers Dataverse natively.
- **D:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: The standard connector covers Dataverse natively.

### Question 52 — D

Answer: Build a custom connector for the internal API. A custom connector wraps an authenticated API as a first-class action. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **B:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **C:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **D:** Correct. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. In this case: A custom connector wraps an authenticated API as a first-class action.

### Question 53 — A

Answer: Start and wait for an approval. The approval action pauses the run and resumes with the outcome. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run and resumes with the outcome.
- **B:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **C:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.
- **D:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run and resumes with the outcome.

### Question 54 — D

Answer: Choose the approval type that matches the sign-off the process requires. Everyone must approve is the right type when each approver holds a veto. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **B:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **C:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **D:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: Everyone must approve is the right type when each approver holds a veto.

### Question 55 — A

Answer: Use Compose to shape the payload the next step consumes. Compose builds the exact object the next action expects. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Compose builds the exact object the next action expects, which avoids mapping errors downstream. In this case: Compose builds the exact object the next action expects.
- **B:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Compose builds the exact object the next action expects.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Compose builds the exact object the next action expects.
- **D:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: Compose builds the exact object the next action expects.

### Question 56 — C

Answer: Parse JSON so later steps can use the fields. Parse JSON turns an opaque body into typed properties. Parse JSON turns an opaque body into typed properties the designer can offer you. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **C:** Correct. Parse JSON turns an opaque body into typed properties the designer can offer you. In this case: Parse JSON turns an opaque body into typed properties.
- **D:** Incorrect for this question. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.

### Question 57 — D

Answer: Apply to each over the returned rows. Apply to each iterates the array. Apply to each iterates the array, which is how one run processes many records. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Apply to each iterates the array.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Apply to each iterates the array.
- **C:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: Apply to each iterates the array.
- **D:** Correct. Apply to each iterates the array, which is how one run processes many records. In this case: Apply to each iterates the array.

### Question 58 — D

Answer: Add a condition to branch on the status. A condition is the explicit branch for two paths. A condition is the explicit branch that makes the two paths readable in the run history. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: A condition is the explicit branch for two paths.
- **B:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A condition is the explicit branch for two paths.
- **C:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A condition is the explicit branch for two paths.
- **D:** Correct. A condition is the explicit branch that makes the two paths readable in the run history. In this case: A condition is the explicit branch for two paths.

### Question 59 — B

Answer: Use a switch for the multi-way branch. A switch keeps five outcomes readable. A switch keeps four or five outcomes readable where nested conditions become unreadable. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A switch keeps five outcomes readable.
- **B:** Correct. A switch keeps four or five outcomes readable where nested conditions become unreadable. In this case: A switch keeps five outcomes readable.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A switch keeps five outcomes readable.
- **D:** Incorrect for this question. A scope groups steps so a single run-after configuration can catch any failure inside it. Why the correct answer wins: A switch keeps five outcomes readable.

### Question 60 — A

Answer: Read the run history to find the failed action and its inputs. The run history shows each action's inputs and outputs. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows each action's inputs and outputs.
- **B:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **C:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **D:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: The run history shows each action's inputs and outputs.

### Question 61 — C

Answer: Test the flow with the real trigger payload. A production-shaped payload proves the expressions resolve. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **B:** Incorrect for this question. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **C:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: A production-shaped payload proves the expressions resolve.
- **D:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: A production-shaped payload proves the expressions resolve.

### Question 62 — A

Answer: Start from a prompt template in AI Hub. A template carries a tested instruction and the input contract. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: A template carries a tested instruction and the input contract.
- **B:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A template carries a tested instruction and the input contract.

### Question 63 — D

Answer: Add typed inputs so the prompt takes values. Typed inputs become the parameters an app or flow supplies. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **D:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Typed inputs become the parameters an app or flow supplies.

### Question 64 — B

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in approved documents. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **B:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in approved documents.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **D:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.

### Question 65 — C

Answer: Choose the model that fits the task instead of the largest available. Matching the model to the task controls cost. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Matching the model to the task controls cost.
- **B:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Matching the model to the task controls cost.
- **C:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Matching the model to the task controls cost.
- **D:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Matching the model to the task controls cost.

### Question 66 — A

Answer: Call the prompt from the canvas app through its connector. Consuming the published prompt keeps one instruction behind the app. Consuming the published prompt keeps one instruction and one model choice behind every app. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Consuming the published prompt keeps one instruction and one model choice behind every app. In this case: Consuming the published prompt keeps one instruction behind the app.
- **B:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **C:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.

### Question 67 — B

Answer: Call the prompt from the cloud flow action. A flow can run a prompt as a step and store the result. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **B:** Correct. A flow can run a prompt as a step, which is how a generated summary joins an automated process. In this case: A flow can run a prompt as a step and store the result.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **D:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: A flow can run a prompt as a step and store the result.

### Question 68 — B

Answer: Consume the AI Hub model through the same connector pattern as a prompt. Consuming the model through the connector keeps authentication governed. A model consumed this way keeps authentication and throttling in one governed place. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.
- **B:** Correct. A model consumed this way keeps authentication and throttling in one governed place. In this case: Consuming the model through the connector keeps authentication governed.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.
- **D:** Incorrect for this question. Storing the result on the record is what makes the model output visible to the process and the audit. Why the correct answer wins: Consuming the model through the connector keeps authentication governed.

### Question 69 — A

Answer: Call the model from the flow and store the result on the record. Calling the model from the flow and storing the result makes it auditable. Storing the result on the record is what makes the model output visible to the process and the audit. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Storing the result on the record is what makes the model output visible to the process and the audit. In this case: Calling the model from the flow and storing the result makes it auditable.
- **B:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.
- **C:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.
- **D:** Incorrect for this question. A model consumed this way keeps authentication and throttling in one governed place. Why the correct answer wins: Calling the model from the flow and storing the result makes it auditable.

### Question 70 — C

Answer: Configure a business rule on the table. A business rule enforces a condition or required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **B:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **C:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a condition or required field without code.
- **D:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a condition or required field without code.

### Question 71 — C

Answer: Branch the business process flow on the case type. A branch covers two variants without a second process. A branch lets one process cover two variants without a second process and a duplicate set of stages. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. One linear process forces every case through fields and stages it does not need. Why the correct answer wins: A branch covers two variants without a second process.
- **B:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A branch covers two variants without a second process.
- **C:** Correct. A branch lets one process cover two variants without a second process and a duplicate set of stages. In this case: A branch covers two variants without a second process.
- **D:** Incorrect for this question. A business process flow guides a record through stages and pins the fields each stage needs. Why the correct answer wins: A branch covers two variants without a second process.

### Question 72 — D

Answer: Model the stages in a business process flow. A business process flow guides a record through stages. A business process flow guides a record through stages and pins the fields each stage needs. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A branch lets one process cover two variants without a second process and a duplicate set of stages. Why the correct answer wins: A business process flow guides a record through stages.
- **B:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A business process flow guides a record through stages.
- **C:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A business process flow guides a record through stages.
- **D:** Correct. A business process flow guides a record through stages and pins the fields each stage needs. In this case: A business process flow guides a record through stages.

### Question 73 — C

Answer: Use a rollup column to aggregate the child records. A rollup aggregates related rows on a schedule. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **B:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **C:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A rollup aggregates related rows on a schedule.
- **D:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A rollup aggregates related rows on a schedule.

### Question 74 — B

Answer: Use a formula column where the rule needs Power Fx. A formula column evaluates a Power Fx expression. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **B:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column evaluates a Power Fx expression.
- **C:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A formula column evaluates a Power Fx expression.
- **D:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column evaluates a Power Fx expression.

### Question 75 — B

Answer: Pick the logic mechanism that matches where the rule must hold. A mechanism is chosen by where the rule must hold. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. Local study-map skill 3.14 (Choosing the Right Business Logic), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **B:** Correct. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. In this case: A mechanism is chosen by where the rule must hold.
- **C:** Incorrect for this question. A synchronous plug-in runs inside the save, so no caller can bypass it. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **D:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A mechanism is chosen by where the rule must hold.

### Question 76 — A, E

Answers: Use an automated trigger on record creation; Trigger when a chosen column changes, with a filter condition. The automated trigger starts the run, and the filter stops irrelevant updates. An automated trigger runs without a user, which is what a background rule needs. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.
- **B:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **C:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **D:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **E:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.

### Question 77 — C, D

Answers: Start and wait for an approval; Choose the approval type that matches the sign-off the process requires. The approval action pauses the run, and the type encodes who must respond. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **B:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **C:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: The approval action pauses the run, and the type encodes who must respond.
- **D:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run, and the type encodes who must respond.
- **E:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.

### Question 78 — A, D

Answers: Wrap the steps in a Scope so one error path handles the failures; Configure run after so the failure path actually executes. A scope groups the steps, and run after makes the failure branch execute. A scope groups steps so a single run-after configuration can catch any failure inside it. By default a step runs only on success, so the failure branch never fires without this setting. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A scope groups steps so a single run-after configuration can catch any failure inside it. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **B:** Incorrect for this question. Concurrency runs iterations in parallel, which is faster but reorders side effects. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **D:** Correct. By default a step runs only on success, so the failure branch never fires without this setting. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **E:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.

### Question 79 — D, E

Answers: Read the run history to find the failed action and its inputs; Test the flow with the real trigger payload. The run history shows the wrong value, and a real payload proves the fix. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **C:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **D:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: The run history shows the wrong value, and a real payload proves the fix.
- **E:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows the wrong value, and a real payload proves the fix.

### Question 80 — B, C

Answers: Start from a prompt template in AI Hub; Add the knowledge source so the prompt grounds on approved content. The template supplies the instruction, and knowledge grounds the answer. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **B:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: The template supplies the instruction, and knowledge grounds the answer.
- **C:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: The template supplies the instruction, and knowledge grounds the answer.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **E:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.

### Question 81 — B, E

Answers: Choose the model that fits the task instead of the largest available; Add typed inputs so the prompt takes values. Inputs are the parameters, and the model choice controls cost and quality. Matching the model to the task controls cost and latency without losing the quality the task needs. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **B:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Inputs are the parameters, and the model choice controls cost and quality.
- **C:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **E:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Inputs are the parameters, and the model choice controls cost and quality.

### Question 82 — A, C

Answers: Configure a business rule on the table; Enforce the rule in a synchronous plug-in when it must run on every write. A table-scope business rule covers imports, and a synchronous plug-in runs inside the save. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. A synchronous plug-in runs inside the save, so no caller can bypass it. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A synchronous plug-in runs inside the save, so no caller can bypass it. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **C:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **D:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **E:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.

### Question 83 — B, C

Answers: Use a formula column where the rule needs Power Fx; Use a rollup column to aggregate the child records. A formula column recalculates, and a rollup aggregates children. A formula column evaluates a Power Fx expression, which is the current way to express derived values. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **B:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column recalculates, and a rollup aggregates children.
- **C:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A formula column recalculates, and a rollup aggregates children.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **E:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.

### Question 84 — A

Answer: Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run. The event decides the trigger, and the real payload decides whether the expressions resolve. The event decides the trigger, and the payload decides whether the expressions actually resolve. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The event decides the trigger, and the payload decides whether the expressions actually resolve. In this case: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **B:** Incorrect for this question. A run history only exists after a run has happened. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **C:** Incorrect for this question. There is no payload to test until a trigger and actions exist. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **D:** Incorrect for this question. Actions placed before the trigger cannot know what data they receive. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.

### Question 85 — B

Answer: Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester. The branch reads the approval outcome, and the record update carries the decision. The branch reads the approval outcome, and the record update carries the decision. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Notifying first tells the requester about a decision that does not exist. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **B:** Correct. The branch reads the approval outcome, and the record update carries the decision. In this case: The branch reads the approval outcome, and the record update carries the decision.
- **C:** Incorrect for this question. The record cannot be updated with a decision that has not been taken. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **D:** Incorrect for this question. A branch with no outcome yet has nothing to evaluate. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.

### Question 86 — D

Answer: State the rule in business terms → choose the mechanism that enforces it where it must hold → configure the rule at table scope → test it on the form and through an import → document it for the support team. Choosing the mechanism first stops a form-only rule being used for a table-wide requirement. Choosing the mechanism before configuring anything is what stops a form-only rule being used for a rule that must survive an import. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Documentation of an unconfigured rule describes an intention, not a system. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **B:** Incorrect for this question. A test needs the configured rule and the stated requirement behind it. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **C:** Incorrect for this question. Configuration before the rule is stated produces a rule nobody agreed to. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **D:** Correct. Choosing the mechanism before configuring anything is what stops a form-only rule being used for a rule that must survive an import. In this case: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.

### Question 87 — A

Answer: Define the stages the record moves through → choose the columns each stage requires → branch the process where the case types diverge → test a record through every stage → hand the process to the users. Stages and their required columns define the process. Stages and their required columns define the process; branching handles the variants without a second process. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Stages and their required columns define the process; branching handles the variants without a second process. In this case: Stages and their required columns define the process.
- **B:** Incorrect for this question. There is nothing to test through until the stages exist. Why the correct answer wins: Stages and their required columns define the process.
- **C:** Incorrect for this question. A branch needs stages to branch from. Why the correct answer wins: Stages and their required columns define the process.
- **D:** Incorrect for this question. Users handed a process with no stages see an empty tracker. Why the correct answer wins: Stages and their required columns define the process.

### Question 88 — A, D

Answers: Use Monitor to inspect the network call and the formula that fired; Run the app in Test Studio before publishing. Test Studio proves the screens, and Monitor explains the timing. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Test Studio captures the screens and formulas that a regression would break. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. In this case: Test Studio proves the screens, and Monitor explains the timing.
- **B:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.
- **C:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.
- **D:** Correct. Test Studio captures the screens and formulas that a regression would break. In this case: Test Studio proves the screens, and Monitor explains the timing.
- **E:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: Test Studio proves the screens, and Monitor explains the timing.

### Question 89 — A

Answer: Use a lookup column instead of storing the name as text. A lookup stores a reference to the related row, so the item name is never copied. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. In this case: A lookup stores a reference to the related row, so the item name is never copied.
- **B:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.
- **C:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.
- **D:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A lookup stores a reference to the related row, so the item name is never copied.

### Question 90 — B

Answer: Publish a component library for the shared header and controls. A component library is the reusable home for a shared control. A component library is the reusable, versioned home for a control that several apps must share. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A component library is the reusable home for a shared control.
- **B:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: A component library is the reusable home for a shared control.
- **C:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A component library is the reusable home for a shared control.
- **D:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A component library is the reusable home for a shared control.

### Question 91 — C

Answer: Choose the model that fits the task instead of the largest available. Matching the model to the task controls cost per reply. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Matching the model to the task controls cost per reply.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Matching the model to the task controls cost per reply.
- **C:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Matching the model to the task controls cost per reply.
- **D:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Matching the model to the task controls cost per reply.

### Question 92 — B

Answer: Move the user to another business unit to fix access. Business units partition ownership, which separates client companies. Business units partition ownership; moving a user changes far more than one record. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: Business units partition ownership, which separates client companies.
- **B:** Correct. Business units partition ownership; moving a user changes far more than one record. In this case: Business units partition ownership, which separates client companies.
- **C:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: Business units partition ownership, which separates client companies.
- **D:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: Business units partition ownership, which separates client companies.

### Question 93 — B

Answer: Add accessible labels and screen-reader text to the controls. Labelling and contrast make the app usable for everyone. A control without a label is unusable with a screen reader, however clear it looks. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Labelling and contrast make the app usable for everyone.
- **B:** Correct. A control without a label is unusable with a screen reader, however clear it looks. In this case: Labelling and contrast make the app usable for everyone.
- **C:** Incorrect for this question. Colour alone fails for a colour-blind user and for anyone reading the app in high contrast. Why the correct answer wins: Labelling and contrast make the app usable for everyone.
- **D:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: Labelling and contrast make the app usable for everyone.

### Question 94 — C

Answer: Choose the approval type that matches the sign-off the process requires. Approve or reject is the type for one named approver. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Approve or reject is the type for one named approver.
- **B:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Approve or reject is the type for one named approver.
- **C:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: Approve or reject is the type for one named approver.
- **D:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: Approve or reject is the type for one named approver.

### Question 95 — D

Answer: Enable auditing on the tables that hold regulated data. Auditing records who changed which column and when. Auditing records who changed which column and when, which is what an audit asks for. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Ownership decides who can see a row and auditing decides whether its history survives an investigation. Why the correct answer wins: Auditing records who changed which column and when.
- **B:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: Auditing records who changed which column and when.
- **C:** Incorrect for this question. Field security is the only control that hides a column while the record stays visible. Why the correct answer wins: Auditing records who changed which column and when.
- **D:** Correct. Auditing records who changed which column and when, which is what an audit asks for. In this case: Auditing records who changed which column and when.

### Question 96 — D

Answer: Configure the navigation in the sitemap designer. The sitemap is the app's menu. The sitemap is the app's menu, so it decides what a user can reach at all. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: The sitemap is the app's menu.
- **B:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: The sitemap is the app's menu.
- **C:** Incorrect for this question. Sharing an app grants the app, and the role grants the data; both are needed. Why the correct answer wins: The sitemap is the app's menu.
- **D:** Correct. The sitemap is the app's menu, so it decides what a user can reach at all. In this case: The sitemap is the app's menu.

### Question 97 — C

Answer: Use a switch for the multi-way branch. A switch keeps several outcomes readable. A switch keeps four or five outcomes readable where nested conditions become unreadable. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A scope groups steps so a single run-after configuration can catch any failure inside it. Why the correct answer wins: A switch keeps several outcomes readable.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A switch keeps several outcomes readable.
- **C:** Correct. A switch keeps four or five outcomes readable where nested conditions become unreadable. In this case: A switch keeps several outcomes readable.
- **D:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A switch keeps several outcomes readable.

### Question 98 — C

Answer: Create a public view for the shared filtered list. A public view is shared with everyone who has access to the table. A public view is available to everyone with access to the table, so the team sees the same list. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **B:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **C:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: A public view is shared with everyone who has access to the table.
- **D:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: A public view is shared with everyone who has access to the table.

### Question 99 — D

Answer: Filter the view on the columns the team actually searches. The filter decides which records are in the list. The filter decides which records appear, so it must match the question the list answers. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides which records are in the list.
- **B:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The filter decides which records are in the list.
- **C:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides which records are in the list.
- **D:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides which records are in the list.

### Question 100 — B

Answer: Build a custom connector for the internal API. A custom connector wraps an authenticated API as a first-class action. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **B:** Correct. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. In this case: A custom connector wraps an authenticated API as a first-class action.
- **C:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **D:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.

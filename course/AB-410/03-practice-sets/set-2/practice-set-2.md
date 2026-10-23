# Microsoft AB-410 — Full-Length Mock Exam 2

Intelligent Applications Builder Associate · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, interactive components in the maker portal, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A claims requirement spans a supervisor view, an adjuster form, and an approval. What should the maker produce first?

Domain: Create a foundation for intelligent applications

- A. Start with a custom connector and a plug-in for the first version
- B. Deliver every requirement as a single model-driven app
- C. Map each requirement to the Power Platform component that fits it
- D. Build a working prototype in a week and let the business react to it

### 2. A settlement approval must follow the same path every time with no judgement. What should be used?

Domain: Create a foundation for intelligent applications

- A. Build a custom Copilot Studio agent for every requirement
- B. Adopt the built-in agent that already covers the task
- C. Model the process as a cloud flow with no agent at all
- D. Deliver every requirement as a single model-driven app

### 3. An adjuster needs a timeline control that no standard component provides. What should be built?

Domain: Create a foundation for intelligent applications

- A. Write a Dataverse plug-in in C#
- B. Build a Power Apps component framework control
- C. Ship a code-first component now and replace it with low-code later
- D. Add a JavaScript web resource to the form

### 4. A field must appear only when the claim type is litigation, and only on the adjuster form. What fits?

Domain: Create a foundation for intelligent applications

- A. Write a Dataverse plug-in in C#
- B. Build a Power Apps component framework control
- C. Add a JavaScript web resource to the form
- D. Configure a business rule on the table

### 5. An acceptance test must run against the same configuration as production without touching live claims. What should be used?

Domain: Create a foundation for intelligent applications

- A. Choose the environment type that matches the data boundary and the licence
- B. Do all building in the production environment to avoid deployment
- C. Run production workloads in a sandbox environment
- D. Share a single environment between development and production

### 6. A single field label must change in production without re-importing the whole solution. What should be shipped?

Domain: Create a foundation for intelligent applications

- A. Import unmanaged customizations directly into production
- B. Package the customizations in a solution before moving them
- C. Ship a patch to the managed solution
- D. Clone the environment each time instead of using a pipeline

### 7. A team copies the production environment to build a test environment including its claims. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Automate export and import with an Azure DevOps pipeline
- B. Use the trial environment for production after the pilot
- C. Clone the environment each time instead of using a pipeline
- D. Use Power Platform pipelines to deploy between environments

### 8. An insurance solution must carry a stable prefix and be removable from production. Which two practices apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Define the solution publisher and prefix once, before the first table
- B. Ship a patch to the managed solution
- C. Import unmanaged customizations directly into production
- D. Do all building in the production environment to avoid deployment
- E. Promote a managed solution to test and production

### 9. A claim intake list is proposed in SharePoint to avoid modelling. What is the objection?

Domain: Create a foundation for intelligent applications

- A. Keep the records in a SharePoint list and skip Dataverse
- B. Extend the standard table instead of creating a duplicate
- C. Create the table in the Dataverse data workspace
- D. Add a choice column for the fixed set of options

### 10. Phone calls, letters, and visits must appear on one timeline per claim. Which table fits?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Create a custom table for the new business entity
- C. Store the interactions in the Activity table
- D. Store the account name as text so the form stays simple

### 11. A claim record must record which adjuster owns it and keep its history. What decides that?

Domain: Create a foundation for intelligent applications

- A. Extend the standard table instead of creating a duplicate
- B. Configure a row summary to summarize the record text
- C. Enable auditing on the tables that hold regulated data
- D. Configure table properties such as ownership and auditing

### 12. Claim types must be identical in the claim table and the settlement table. What should be used?

Domain: Create a foundation for intelligent applications

- A. Store the account name as text so the form stays simple
- B. Add a choice column for the fixed set of options
- C. Use a global choice so several tables share one option list
- D. Use a lookup column instead of storing the name as text

### 13. A reserve ratio must stay exact across repeated recalculation. Which column type fits?

Domain: Create a foundation for intelligent applications

- A. Use a decimal column for an exact rate
- B. Use an auto-number column for the case identifier
- C. Use a currency column with the record currency
- D. Store the account name as text so the form stays simple

### 14. Every claim needs a reference the customer can quote on the phone. What should be used?

Domain: Create a foundation for intelligent applications

- A. Use a currency column with the record currency
- B. Store the account name as text so the form stays simple
- C. Use an auto-number column for the case identifier
- D. Use a calculated column for the value that must never change

### 15. A field must accept only approved values and point at the policy record. Which two column types apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Add a choice column for the fixed set of options
- B. Use a currency column with the record currency
- C. Use a calculated column for the value that must never change
- D. Use a lookup column instead of storing the name as text
- E. Store the account name as text so the form stays simple

### 16. A policy can cover many properties and a property can appear on many policies. What fits?

Domain: Create a foundation for intelligent applications

- A. Use a lookup column instead of storing the name as text
- B. Set the relationship behaviour to parental so child records are removed with the parent
- C. Configure a one-to-many relationship with a lookup on the child table
- D. Model the many-to-many link with a native N:N relationship

### 17. A property must survive the deletion of an old policy. What relationship behaviour fits?

Domain: Create a foundation for intelligent applications

- A. Set the relationship behaviour to parental so child records are removed with the parent
- B. Model the many-to-many link with a native N:N relationship
- C. Configure a one-to-many relationship with a lookup on the child table
- D. Keep the relationship referential so child records survive the parent delete

### 18. Every adjuster must see the same list of claims awaiting decision. What should be created?

Domain: Create a foundation for intelligent applications

- A. Change the system view so the list order suits the team
- B. Rely on each user's personal view of the table
- C. Create a public view for the shared filtered list
- D. Design the main form around the record the user opens

### 19. A team needs one shared list and one working record surface. Which two components apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Rely on each user's personal view of the table
- B. Design the main form around the record the user opens
- C. Add a quick-create form for entry from a lookup
- D. Change the system view so the list order suits the team
- E. Create a public view for the shared filtered list

### 20. The national identifier must be hidden from claims assistants while the claim stays visible. What should be used?

Domain: Create a foundation for intelligent applications

- A. Assign a security role that grants only the privileges the role needs
- B. Move the user to another business unit to fix access
- C. Use a field security profile for the sensitive column
- D. Assign the record to a team that the group owns

### 21. Access must be granted per table and one column kept hidden. Which two controls apply? Select two.

Domain: Create a foundation for intelligent applications

- A. Assign a security role that grants only the privileges the role needs
- B. Create a public view for the shared filtered list
- C. Use a field security profile for the sensitive column
- D. Move the user to another business unit to fix access
- E. Assign the record to a team that the group owns

### 22. A claims solution must reach the right environment boundary under control. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Create the solution with its publisher → deploy through the pipeline → identify the data boundary → choose the environment type
- B. Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline
- C. Choose the environment type → deploy through the pipeline → identify the data boundary → create the solution with its publisher
- D. Deploy through the pipeline → create the solution with its publisher → choose the environment type → identify the data boundary

### 23. An insurer must prove that adjusters see only their own claims. Which sequence is correct?

Domain: Create a foundation for intelligent applications

- A. Verify with a test user → assign the security role → identify who must see which records → set the business unit scope → add a field profile
- B. Add a field profile for the sensitive column → verify with a test user → identify who must see which records → assign the security role → set the business unit scope
- C. Identify who must see which records → assign the security role → set the business unit scope → add a field profile for the sensitive column → verify with a test user
- D. Set the business unit scope → add a field profile → identify who must see which records → verify with a test user → assign the security role

### 24. An adjuster form carries fifty columns and users scroll past the eight they use. What should change?

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Choose the view columns before setting the filter
- C. Add the columns the role uses to the main form
- D. Hide the field with a JavaScript web resource

### 25. A queue must be readable at a glance without opening each claim. What must be chosen first?

Domain: Create intelligent applications

- A. Filter the view on the columns the team actually searches
- B. Choose the view columns before setting the filter
- C. Write FetchXML for the view to get the exact rows
- D. Create a public view for the shared filtered list

### 26. A queue must show only claims awaiting a decision in this region. What decides that?

Domain: Create intelligent applications

- A. Choose the view columns before setting the filter
- B. Create a public view for the shared filtered list
- C. Write FetchXML for the view to get the exact rows
- D. Filter the view on the columns the team actually searches

### 27. A supervisor summary page does not exist and a draft is needed this week. What should be done?

Domain: Create intelligent applications

- A. Replace the main form with the generated page
- B. Organize the long form into tabs and sections
- C. Generate the page from a natural-language description, then refine it
- D. Publish the generated page without reviewing its data bindings

### 28. A new adjuster can open the app but sees an empty claims list. What is missing?

Domain: Create intelligent applications

- A. Share the app only and rely on the app for access
- B. Add the forms, views, and pages to the app in the app designer
- C. Configure the navigation in the sitemap designer
- D. Share the app and assign the security role that backs it

### 29. A supervisor wants the ageing chart, the queue, and the count on one page. What should be assembled?

Domain: Create intelligent applications

- A. Create the chart on the view for the trend
- B. Filter the view on the columns the team actually searches
- C. Build the chart in Power BI and embed it
- D. Add the chart and the views to a dashboard

### 30. Adjusters capture loss details on site with one hand. Which layout fits?

Domain: Create intelligent applications

- A. Use responsive containers so the layout adapts to the device
- B. Fix the layout to one pixel width so it always looks the same
- C. Use the tablet layout for desk-based users
- D. Use the phone layout for field staff

### 31. The claims team includes a screen-reader user. What must be added to the controls?

Domain: Create intelligent applications

- A. Fix the layout to one pixel width so it always looks the same
- B. Convey status with colour alone
- C. Add accessible labels and screen-reader text to the controls
- D. Filter in Power Fx after loading the rows into the app

### 32. Three apps must share one branded claims header. What should be used?

Domain: Create intelligent applications

- A. Publish a component library for the shared header and controls
- B. Create a user-defined function for the reused expression
- C. Define a named formula for the shared calculation
- D. Copy the screen into every app that needs it

### 33. The signed-in adjuster's region must be available on every screen. What should be used?

Domain: Create intelligent applications

- A. Use a context variable scoped to the screen
- B. Use a global variable for the value that the whole app needs
- C. Clear the collection when the screen changes
- D. Collect the rows into a collection for in-memory work

### 34. A claim save can fail on a timeout and the user sees nothing. What should be added?

Domain: Create intelligent applications

- A. Use Monitor to inspect the network call and the formula that fired
- B. Run the app in Test Studio before publishing
- C. Write a Trace message for the support team
- D. Wrap the call in IfError and surface the message to the user

### 35. A change to the intake screen must not break the existing flow of screens. What should be run first?

Domain: Create intelligent applications

- A. Run the app in Test Studio before publishing
- B. Wrap the call in IfError and surface the message to the user
- C. Use Monitor to inspect the network call and the formula that fired
- D. Write a Trace message for the support team

### 36. An adjuster wants to ask questions about a claim from inside the app. What should be added?

Domain: Create intelligent applications

- A. Call the agent's endpoint directly from Power Fx
- B. Add the Copilot Studio agent to the canvas app as a component
- C. Build a custom Copilot Studio agent for every requirement
- D. Build a second canvas app just to host the agent

### 37. A claims app must be composed and released to supervisors. Which sequence is correct?

Domain: Create intelligent applications

- A. Set the navigation in the sitemap → share the app → configure the forms and views → compose the app → assign the role
- B. Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role
- C. Assign the backing security role → configure the forms and views → set the navigation → compose the app → share the app
- D. Share the app → assign the backing security role → configure the forms and views → compose the app → set the navigation

### 38. A field app must reach adjusters without a broken save. Which sequence is correct?

Domain: Create intelligent applications

- A. Add error handling → connect the data source → test with Monitor → build the screens → publish the app
- B. Build the screens → test with Monitor → connect the data source → publish the app → add error handling
- C. Publish the app → connect the data source → build the screens → add error handling → test with Monitor and Test Studio
- D. Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app

### 39. A claim decision must notify the policy holder the moment it is recorded. What should be used?

Domain: Build business application logic and automation

- A. Expose an HTTP request trigger with a signed URL
- B. Use a scheduled trigger for the nightly batch
- C. Use an automated trigger on record creation
- D. Use a manually triggered flow from the app

### 40. A claims ageing report must be emailed every weekday at six. What should be used?

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Expose an HTTP request trigger with a signed URL
- C. Use a manually triggered flow from the app
- D. Use an automated trigger on record creation

### 41. A flow must run only when a claim status becomes settled. What should be used?

Domain: Build business application logic and automation

- A. Trigger on every update so nothing is missed
- B. Use an automated trigger on record creation
- C. Use a scheduled trigger for the nightly batch
- D. Trigger when a chosen column changes, with a filter condition

### 42. The flow reads and writes Dataverse claim records. Which connector fits?

Domain: Build business application logic and automation

- A. Copy the data into Excel to avoid a premium connector
- B. Use the premium connector the source requires
- C. Build a custom connector for the internal API
- D. Use the standard Dataverse connector

### 43. An underwriting API must be called with its own authentication. What should be built?

Domain: Build business application logic and automation

- A. Build a custom connector for the internal API
- B. Copy the data into Excel to avoid a premium connector
- C. Use the standard Dataverse connector
- D. Use the premium connector the source requires

### 44. The claims director and the compliance lead must both approve a settlement. Which approval type fits?

Domain: Build business application logic and automation

- A. Start and wait for an approval
- B. Send parallel approvals and require every response
- C. Send an email and treat silence as approval
- D. Choose the approval type that matches the sign-off the process requires

### 45. A settlement above 100,000 needs the supervisor and then the director. What should be built?

Domain: Build business application logic and automation

- A. Choose the approval type that matches the sign-off the process requires
- B. Chain two approvals in sequence for the second-level sign-off
- C. Send parallel approvals and require every response
- D. Send an email and treat silence as approval

### 46. A team treats an unanswered email as approval. What is the objection?

Domain: Build business application logic and automation

- A. Start and wait for an approval
- B. Send an email and treat silence as approval
- C. Chain two approvals in sequence for the second-level sign-off
- D. Choose the approval type that matches the sign-off the process requires

### 47. A downstream action expects one object built from three claim fields. What should be used?

Domain: Build business application logic and automation

- A. Apply to each over the returned rows
- B. Use Compose to shape the payload the next step consumes
- C. Parse JSON so later steps can use the fields
- D. Add a condition to branch on the status

### 48. A returned body is an opaque string and the designer offers no properties. What should be added?

Domain: Build business application logic and automation

- A. Parse JSON so later steps can use the fields
- B. Add a condition to branch on the status
- C. Use Compose to shape the payload the next step consumes
- D. Apply to each over the returned rows

### 49. A flow branches five ways by claim type. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Use a switch for the multi-way branch
- C. Add a condition to branch on the status
- D. Wrap the steps in a Scope so one error path handles the failures

### 50. A failure branch exists but never executes. What must be configured?

Domain: Build business application logic and automation

- A. Configure run after so the failure path actually executes
- B. Write a Trace message for the support team
- C. Add a condition to branch on the status
- D. Wrap the steps in a Scope so one error path handles the failures

### 51. A loop retries until a record is found with no exit limit. What is the defect?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Add a condition to branch on the status
- C. Use a switch for the multi-way branch
- D. Loop until the record is found with no exit limit

### 52. A flow fails and the message names no field. What shows the wrong value?

Domain: Build business application logic and automation

- A. Read the run history to find the failed action and its inputs
- B. Turn on static result to test the rest of the flow
- C. Test the flow with the real trigger payload
- D. Resubmit the failed run after the fix

### 53. A manager wants the approval flow exercised with the payload a real submission produces. What should be used?

Domain: Build business application logic and automation

- A. Turn on static result to test the rest of the flow
- B. Read the run history to find the failed action and its inputs
- C. Test the flow with the real trigger payload
- D. Resubmit the failed run after the fix

### 54. A connector call is throttled and the remaining steps still need testing. What should be used?

Domain: Build business application logic and automation

- A. Turn on static result to test the rest of the flow
- B. Test the flow with the real trigger payload
- C. Read the run history to find the failed action and its inputs
- D. Resubmit the failed run after the fix

### 55. A claim summary prompt must start from a tested instruction. What should be used?

Domain: Build business application logic and automation

- A. Build the prompt from blank
- B. Start from a prompt template in AI Hub
- C. Add typed inputs so the prompt takes values
- D. Copy the prompt text into each app so it can be tuned per app

### 56. A novel task has no template and the instruction must be written from scratch. What should be done?

Domain: Build business application logic and automation

- A. Start from a prompt template in AI Hub
- B. Build the prompt from blank
- C. Copy the prompt text into each app so it can be tuned per app
- D. Add typed inputs so the prompt takes values

### 57. A prompt must take the claim narrative as a value on each run. What should be added?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Copy the prompt text into each app so it can be tuned per app
- C. Add the knowledge source so the prompt grounds on approved content
- D. Choose the model that fits the task instead of the largest available

### 58. Summaries must be grounded in the approved claims-handling manual. What should be added?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Add the knowledge source so the prompt grounds on approved content
- C. Choose the model that fits the task instead of the largest available
- D. Copy the prompt text into each app so it can be tuned per app

### 59. Summaries are good enough on a mid-sized model and the bill is high. What should change?

Domain: Build business application logic and automation

- A. Add the knowledge source so the prompt grounds on approved content
- B. Copy the prompt text into each app so it can be tuned per app
- C. Add typed inputs so the prompt takes values
- D. Choose the model that fits the task instead of the largest available

### 60. An adjuster must generate the summary while looking at the claim form. What should be used?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Call the prompt from the cloud flow action
- C. Choose the model that fits the task instead of the largest available
- D. Call the prompt from the canvas app through its connector

### 61. The summary must be written to the record as part of the overnight process. What should be used?

Domain: Build business application logic and automation

- A. Call the prompt from the canvas app through its connector
- B. Copy the prompt text into each app so it can be tuned per app
- C. Add typed inputs so the prompt takes values
- D. Call the prompt from the cloud flow action

### 62. A settlement model must be called from the flow and its score stored on the claim. What should be used?

Domain: Build business application logic and automation

- A. Call the prompt from the cloud flow action
- B. Call the model from the flow and store the result on the record
- C. Choose the model that fits the task instead of the largest available
- D. Consume the AI Hub model through the same connector pattern as a prompt

### 63. A settlement amount must be required whenever the decision is approved. What should be used?

Domain: Build business application logic and automation

- A. Configure a business rule on the table
- B. Add a JavaScript web resource to the form
- C. Set the business rule scope to the table so it applies in every form
- D. Hide the field with a JavaScript web resource

### 64. A business rule works on the form but not through an import. What should change?

Domain: Build business application logic and automation

- A. Write a Dataverse plug-in in C#
- B. Hide the field with a JavaScript web resource
- C. Configure a business rule on the table
- D. Set the business rule scope to the table so it applies in every form

### 65. A claim must move through five ordered stages with required information at each. What should be built?

Domain: Build business application logic and automation

- A. Model the stages in a business process flow
- B. Branch the business process flow on the case type
- C. Configure a business rule on the table
- D. Use a rollup column to aggregate the child records

### 66. A policy needs a running total of settled amounts from its claims. What should be used?

Domain: Build business application logic and automation

- A. Use a formula column where the rule needs Power Fx
- B. Use a rollup column to aggregate the child records
- C. Use a calculated column for the value that must never change
- D. Write a plug-in to set the value on every update

### 67. A flow must start on a new decision and only for approved claims. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Use an automated trigger on record creation
- C. Trigger when a chosen column changes, with a filter condition
- D. Trigger on every update so nothing is missed
- E. Expose an HTTP request trigger with a signed URL

### 68. A settlement sign-off must pause the run and match the approval rule. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Use a scheduled trigger for the nightly batch
- B. Chain two approvals in sequence for the second-level sign-off
- C. Send an email and treat silence as approval
- D. Choose the approval type that matches the sign-off the process requires
- E. Start and wait for an approval

### 69. A group of steps needs one failure path that fires. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Wrap the steps in a Scope so one error path handles the failures
- B. Add a condition to branch on the status
- C. Use a switch for the multi-way branch
- D. Configure run after so the failure path actually executes
- E. Turn on concurrency control for the loop

### 70. An intermittent flow failure must be traced to a value and the fix confirmed before release. Which two practices apply? Select two.

Domain: Build business application logic and automation

- A. Resubmit the failed run after the fix
- B. Read the run history to find the failed action and its inputs
- C. Parse JSON so later steps can use the fields
- D. Turn on static result to test the rest of the flow
- E. Test the flow with the real trigger payload

### 71. A summary prompt must start tested and stay grounded. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Choose the model that fits the task instead of the largest available
- B. Copy the prompt text into each app so it can be tuned per app
- C. Add the knowledge source so the prompt grounds on approved content
- D. Build the prompt from blank
- E. Start from a prompt template in AI Hub

### 72. A prompt must be parameterised and run on a model suited to the workload. Which two features apply? Select two.

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Start from a prompt template in AI Hub
- C. Choose the model that fits the task instead of the largest available
- D. Add the knowledge source so the prompt grounds on approved content
- E. Copy the prompt text into each app so it can be tuned per app

### 73. A rule must apply from the table and inside every write. Which two mechanisms apply? Select two.

Domain: Build business application logic and automation

- A. Hide the field with a JavaScript web resource
- B. Use a calculated column for the value that must never change
- C. Configure a business rule on the table
- D. Add a JavaScript web resource to the form
- E. Enforce the rule in a synchronous plug-in when it must run on every write

### 74. A derived value must recalculate and a parent must show a child count. Which two column types apply? Select two.

Domain: Build business application logic and automation

- A. Use a rollup column to aggregate the child records
- B. Write a plug-in to set the value on every update
- C. Configure a business rule on the table
- D. Use a formula column where the rule needs Power Fx
- E. Use a calculated column for the value that must never change

### 75. A settlement workflow must reach production without wrong expressions. Which sequence is correct?

Domain: Build business application logic and automation

- A. Add the actions and branches → add the trigger → test with a real payload → decide which event starts the process → read the run history
- B. Test with a real payload → decide which event starts the process → read the run history → add the trigger → add the actions
- C. Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run
- D. Read the run history → add the trigger → decide which event starts the process → add the actions → test with a real payload

### 76. A settlement must be decided and the decision recorded. Which sequence is correct?

Domain: Build business application logic and automation

- A. Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester
- B. Update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome → notify the requester
- C. Notify the requester → update the record → start and wait for the approval → trigger on the submitted request → branch on the outcome
- D. Branch on the outcome → trigger on the submitted request → notify the requester → start and wait for the approval → update the record

### 77. A failing claim notification must be fixed with confidence. Which sequence is correct?

Domain: Build business application logic and automation

- A. Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run
- B. Resubmit the run → open the run history → reproduce the failure → fix the expression → inspect the failing action
- C. Fix the expression → reproduce the failure → resubmit the run → inspect the failing action → open the run history
- D. Open the run history → resubmit the run → reproduce the failure → inspect the failing action → fix the expression

### 78. A settlement rule must hold on the form and through an import. Which sequence is correct?

Domain: Build business application logic and automation

- A. Document it for the support team → test it through an import → choose the mechanism → state the rule → configure the rule
- B. State the rule in business terms → choose the mechanism that enforces it where it must hold → configure the rule at table scope → test it on the form and through an import → document it for the support team
- C. Test it on the form → configure the rule → state the rule in business terms → choose the mechanism → document it
- D. Configure the rule at table scope → state the rule in business terms → document it → test it through an import → choose the mechanism

### 79. A new claim-note entity belongs to no standard table. Where should it be modelled?

Domain: Create a foundation for intelligent applications

- A. Create the table in the Dataverse data workspace
- B. Store the interactions in the Activity table
- C. Keep the records in a SharePoint list and skip Dataverse
- D. Extend the standard table instead of creating a duplicate

### 80. A rule must run during every claim save, including those made by an integration. What enforces it?

Domain: Create a foundation for intelligent applications

- A. Write a Dataverse plug-in in C#
- B. Hide the field with a JavaScript web resource
- C. Add a JavaScript web resource to the form
- D. Build a Power Apps component framework control

### 81. A settlement amount must record the currency it was agreed in. Which column type fits?

Domain: Create a foundation for intelligent applications

- A. Use a currency column with the record currency
- B. Use an auto-number column for the case identifier
- C. Use a decimal column for an exact rate
- D. Store the account name as text so the form stays simple

### 82. A team pastes the summary instruction into each app to tune it separately. What is the objection?

Domain: Build business application logic and automation

- A. Copy the prompt text into each app so it can be tuned per app
- B. Call the prompt from the cloud flow action
- C. Start from a prompt template in AI Hub
- D. Call the prompt from the canvas app through its connector

### 83. An answer must cite the policy wording rather than general knowledge. What should be attached?

Domain: Build business application logic and automation

- A. Add typed inputs so the prompt takes values
- B. Copy the prompt text into each app so it can be tuned per app
- C. Choose the model that fits the task instead of the largest available
- D. Add the knowledge source so the prompt grounds on approved content

### 84. Rules must hold in different places: one on a form, one on every write, one at read time. What decides the mechanism?

Domain: Build business application logic and automation

- A. Use a formula column where the rule needs Power Fx
- B. Enforce the rule in a synchronous plug-in when it must run on every write
- C. Pick the logic mechanism that matches where the rule must hold
- D. Configure a business rule on the table

### 85. A queue must show only this region's open claims and stay readable at a glance. Which two choices apply? Select two.

Domain: Create intelligent applications

- A. Rely on each user's personal view of the table
- B. Create a public view for the shared filtered list
- C. Filter the view on the columns the team actually searches
- D. Choose the view columns before setting the filter
- E. Write FetchXML for the view to get the exact rows

### 86. Three apps must share one header and one margin calculation. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Publish a component library for the shared header and controls
- B. Fix the layout to one pixel width so it always looks the same
- C. Define a named formula for the shared calculation
- D. Copy the screen into every app that needs it
- E. Create a user-defined function for the reused expression

### 87. A chosen region must persist across screens and failures must be recoverable. Which two practices apply? Select two.

Domain: Create intelligent applications

- A. Write a Trace message for the support team
- B. Use a context variable scoped to the screen
- C. Collect the rows into a collection for in-memory work
- D. Wrap the call in IfError and surface the message to the user
- E. Use a global variable for the value that the whole app needs

### 88. A response contains forty claim rows that must each be updated. What should be used?

Domain: Build business application logic and automation

- A. Use Do until with a bounded count for the retry loop
- B. Apply to each over the returned rows
- C. Add a condition to branch on the status
- D. Use a switch for the multi-way branch

---

## Case study — Contoso Real Estate

Contoso Real Estate lists 4,000 properties across five regions with photographs, inspections, and offers. Agents work from phones on site, and the back office works from desktops. Inspection reports are dictated and typed up days later, which delays listings. The marketing team wants AI-written listing descriptions reviewed by a person before publication. Every property has a responsible agent, and a regional manager must see every property in the region but may edit none of them. Offers above the asking price need a manager approval.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Agents want a listing page drafted from a description. What should be used?

Domain: Create intelligent applications

- A. Publish the generated page without reviewing its data bindings
- B. Organize the long form into tabs and sections
- C. Generate the page from a natural-language description, then refine it
- D. Replace the main form with the generated page

### 90. Agents capture inspections on a phone at the property. Which layout fits?

Domain: Create intelligent applications

- A. Use the tablet layout for desk-based users
- B. Use responsive containers so the layout adapts to the device
- C. Fix the layout to one pixel width so it always looks the same
- D. Use the phone layout for field staff

### 91. Listing data must sit in its own governed boundary. What decides the environment?

Domain: Create a foundation for intelligent applications

- A. Use the trial environment for production after the pilot
- B. Choose the environment type that matches the data boundary and the licence
- C. Build in the default environment because everyone already has access
- D. Share a single environment between development and production

---

## Case study — Litware Health

Litware Health operates 22 clinics and a central scheduling team. Patient intake is collected on paper, and clinic staff rekey it into a booking system that has no mobile interface. The clinical director wants a phone app for intake that works on poor connectivity, a desktop app for the scheduling team, and an automated reminder sequence. Patient contact details are regulated, and the compliance team requires field-level control over the national identifier. The organisation has Dataverse, Power Apps per-user licences, and a governance policy that forbids custom code in the first release.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. Clinic staff include a low-vision user on a tablet. What must be added?

Domain: Create intelligent applications

- A. Use responsive containers so the layout adapts to the device
- B. Filter in Power Fx after loading the rows into the app
- C. Add accessible labels and screen-reader text to the controls
- D. Convey status with colour alone

### 93. An appointment gallery must search a large table. What must the filter do?

Domain: Create intelligent applications

- A. Write the filter so the data source performs the delegation
- B. Filter in Power Fx after loading the rows into the app
- C. Collect the rows into a collection for in-memory work
- D. Generate a canvas app from the data source

### 94. The national identifier must be hidden from reception staff. What should be used?

Domain: Create a foundation for intelligent applications

- A. Assign the record to a team that the group owns
- B. Use a field security profile for the sensitive column
- C. Move the user to another business unit to fix access
- D. Assign a security role that grants only the privileges the role needs

---

## Case study — Proseware Consulting

Proseware Consulting sells fixed-fee engagements and tracks them in a dozen project spreadsheets. Partners want a single view of engagement profitability, computed from time entries and expenses, with the margin recalculated whenever a rate changes. Delivery managers need a weekly exception list of engagements running over budget. Finance needs a rollup of committed cost per client. The firm has Dataverse and Power BI, and its partners have asked repeatedly for a chatbot that answers questions about engagement status without training users on a new app.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. The same margin calculation appears on five screens. What should be used?

Domain: Create intelligent applications

- A. Publish a component library for the shared header and controls
- B. Copy the screen into every app that needs it
- C. Create a user-defined function for the reused expression
- D. Define a named formula for the shared calculation

### 96. Consultants shape a temporary set of engagements to sort in the app. What should be used?

Domain: Create intelligent applications

- A. Clear the collection when the screen changes
- B. Use a global variable for the value that the whole app needs
- C. Use a context variable scoped to the screen
- D. Collect the rows into a collection for in-memory work

### 97. Partners want to ask about engagement status inside the app. What should be added?

Domain: Create intelligent applications

- A. Call the agent's endpoint directly from Power Fx
- B. Add the Copilot Studio agent to the canvas app as a component
- C. Build a second canvas app just to host the agent
- D. Run the app in Test Studio before publishing

---

## Case study — Woodgrove Insurance

Woodgrove Insurance processes 12,000 claims a month through a claims centre and four regional offices. Adjusters record notes in a free-text field that has grown to a page per claim, and supervisors cannot tell which claims are stuck. Regulators require a claim decision to record the adjuster, the timestamp, and the information considered. The company wants an AI-generated summary of each claim for the supervisor view, a stage-based process with required information at each stage, and an approval when a settlement exceeds 25,000. Only the assigned adjuster may edit a claim; supervisors may read every claim in their region.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Adjusters need the fields they use without scrolling. What should change?

Domain: Create intelligent applications

- A. Add a JavaScript web resource to the form
- B. Add the columns the role uses to the main form
- C. Organize the long form into tabs and sections
- D. Choose the view columns before setting the filter

### 99. Supervisors can open the app but see no claims. What is missing?

Domain: Create intelligent applications

- A. Share the app and assign the security role that backs it
- B. Configure the navigation in the sitemap designer
- C. Add the forms, views, and pages to the app in the app designer
- D. Share the app only and rely on the app for access

### 100. A long claim form must stay reachable and readable. Which two choices apply? Select two.

Domain: Create intelligent applications

- A. Organize the long form into tabs and sections
- B. Add the columns the role uses to the main form
- C. Add the column to a card form on the main form
- D. Choose the view columns before setting the filter
- E. Hide the field with a JavaScript web resource

---

## Answer key and explanations

### Question 1 — C

Answer: Map each requirement to the Power Platform component that fits it. Mapping requirements to components keeps the solution to the smallest set that satisfies them. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Code-first components raise the support and upgrade cost before the requirement is understood. Why the correct answer wins: Mapping requirements to components keeps the solution to the smallest set that satisfies them.
- **B:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: Mapping requirements to components keeps the solution to the smallest set that satisfies them.
- **C:** Correct. Deciding whether something is a table, an app screen, a flow, a prompt, or an agent before building is what keeps a low-code solution small. In this case: Mapping requirements to components keeps the solution to the smallest set that satisfies them.
- **D:** Incorrect for this question. A prototype answers questions sooner, but it does not settle which component should own the logic. Why the correct answer wins: Mapping requirements to components keeps the solution to the smallest set that satisfies them.

### Question 2 — C

Answer: Model the process as a cloud flow with no agent at all. A deterministic process belongs in a flow, not an agent. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. Local study-map skill 1.1 (Requirements Analysis and Component Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: A deterministic process belongs in a flow, not an agent.
- **B:** Incorrect for this question. A built-in agent is maintained by the platform, so it carries less build and lifecycle cost than a custom agent. Why the correct answer wins: A deterministic process belongs in a flow, not an agent.
- **C:** Correct. A deterministic process belongs in a flow; adding an agent adds a language model where none is needed. In this case: A deterministic process belongs in a flow, not an agent.
- **D:** Incorrect for this question. One app for everything widens access and makes the smallest change a release of the whole solution. Why the correct answer wins: A deterministic process belongs in a flow, not an agent.

### Question 3 — B

Answer: Build a Power Apps component framework control. A PCF control covers a visual the standard control cannot express. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **B:** Correct. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. In this case: A PCF control covers a visual the standard control cannot express.
- **C:** Incorrect for this question. A deliberate later replacement rarely happens, and meanwhile two implementations must be maintained. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A PCF control covers a visual the standard control cannot express.

### Question 4 — C

Answer: Add a JavaScript web resource to the form. A form script changes visibility on that form without changing the table. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: A form script changes visibility on that form without changing the table.
- **B:** Incorrect for this question. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Why the correct answer wins: A form script changes visibility on that form without changing the table.
- **C:** Correct. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. In this case: A form script changes visibility on that form without changing the table.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A form script changes visibility on that form without changing the table.

### Question 5 — C

Answer: Run production workloads in a sandbox environment. A sandbox is for build, test, and acceptance, which is exactly the rehearsal step. A sandbox is for build, test, and acceptance; it is not a production target. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Why the correct answer wins: A sandbox is for build, test, and acceptance, which is exactly the rehearsal step.
- **B:** Incorrect for this question. Building in production removes the test step and puts every unfinished change in front of users. Why the correct answer wins: A sandbox is for build, test, and acceptance, which is exactly the rehearsal step.
- **C:** Correct. A sandbox is for build, test, and acceptance; it is not a production target. In this case: A sandbox is for build, test, and acceptance, which is exactly the rehearsal step.
- **D:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: A sandbox is for build, test, and acceptance, which is exactly the rehearsal step.

### Question 6 — C

Answer: Ship a patch to the managed solution. A patch delivers a small fix against the same parent version. A patch delivers a small fix against the same parent version without a full re-import. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: A patch delivers a small fix against the same parent version.
- **B:** Incorrect for this question. A solution is the unit of deployment, so anything outside it has to be recreated by hand in the next environment. Why the correct answer wins: A patch delivers a small fix against the same parent version.
- **C:** Correct. A patch delivers a small fix against the same parent version without a full re-import. In this case: A patch delivers a small fix against the same parent version.
- **D:** Incorrect for this question. Cloning copies data as well as configuration and is not a repeatable deployment path. Why the correct answer wins: A patch delivers a small fix against the same parent version.

### Question 7 — C

Answer: Clone the environment each time instead of using a pipeline. Cloning copies data as well as configuration, which is rarely what a test environment needs. Cloning copies data as well as configuration and is not a repeatable deployment path. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The automation is not the hard part; the solution boundary and the deployment order are. Why the correct answer wins: Cloning copies data as well as configuration, which is rarely what a test environment needs.
- **B:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: Cloning copies data as well as configuration, which is rarely what a test environment needs.
- **C:** Correct. Cloning copies data as well as configuration and is not a repeatable deployment path. In this case: Cloning copies data as well as configuration, which is rarely what a test environment needs.
- **D:** Incorrect for this question. A pipeline records the deployment and runs the same solution through each stage. Why the correct answer wins: Cloning copies data as well as configuration, which is rarely what a test environment needs.

### Question 8 — A, E

Answers: Define the solution publisher and prefix once, before the first table; Promote a managed solution to test and production. The publisher fixes the prefix, and the managed import is removable. The prefix is baked into every schema name and is expensive to change after data exists. A managed solution is locked, so it can be upgraded and removed predictably. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The prefix is baked into every schema name and is expensive to change after data exists. In this case: The publisher fixes the prefix, and the managed import is removable.
- **B:** Incorrect for this question. A patch delivers a small fix against the same parent version without a full re-import. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **C:** Incorrect for this question. Unmanaged layers in production cannot be cleanly removed or upgraded. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **D:** Incorrect for this question. Building in production removes the test step and puts every unfinished change in front of users. Why the correct answer wins: The publisher fixes the prefix, and the managed import is removable.
- **E:** Correct. A managed solution is locked, so it can be upgraded and removed predictably. In this case: The publisher fixes the prefix, and the managed import is removable.

### Question 9 — A

Answer: Keep the records in a SharePoint list and skip Dataverse. A list has no relationships, security roles, or rollup columns. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. In this case: A list has no relationships, security roles, or rollup columns.
- **B:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **C:** Incorrect for this question. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.
- **D:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A list has no relationships, security roles, or rollup columns.

### Question 10 — C

Answer: Store the interactions in the Activity table. Activities inherit the timeline and the regarding relationship. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.
- **B:** Incorrect for this question. A new entity with no standard equivalent deserves its own table rather than a column on an unrelated one. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.
- **C:** Correct. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. In this case: Activities inherit the timeline and the regarding relationship.
- **D:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: Activities inherit the timeline and the regarding relationship.

### Question 11 — D

Answer: Configure table properties such as ownership and auditing. Ownership and auditing are table properties. Ownership decides who can see a row and auditing decides whether its history survives an investigation. Local study-map skill 1.5 (Standard Tables and Table Properties), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: Ownership and auditing are table properties.
- **B:** Incorrect for this question. A row summary condenses the record's own text, which is what a case recap needs. Why the correct answer wins: Ownership and auditing are table properties.
- **C:** Incorrect for this question. Auditing records who changed which column and when, which is what an audit asks for. Why the correct answer wins: Ownership and auditing are table properties.
- **D:** Correct. Ownership decides who can see a row and auditing decides whether its history survives an investigation. In this case: Ownership and auditing are table properties.

### Question 12 — C

Answer: Use a global choice so several tables share one option list. A global choice keeps one approved list across tables. One global choice keeps the list consistent instead of drifting across tables. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A global choice keeps one approved list across tables.
- **B:** Incorrect for this question. A choice constrains input to the approved list and renders as a dropdown on every form. Why the correct answer wins: A global choice keeps one approved list across tables.
- **C:** Correct. One global choice keeps the list consistent instead of drifting across tables. In this case: A global choice keeps one approved list across tables.
- **D:** Incorrect for this question. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Why the correct answer wins: A global choice keeps one approved list across tables.

### Question 13 — A

Answer: Use a decimal column for an exact rate. A decimal avoids rounding drift in a rate. A decimal avoids the rounding drift that a floating-point column introduces in a rate. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A decimal avoids the rounding drift that a floating-point column introduces in a rate. In this case: A decimal avoids rounding drift in a rate.
- **B:** Incorrect for this question. An auto-number gives every record a readable, unique reference that users can quote. Why the correct answer wins: A decimal avoids rounding drift in a rate.
- **C:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A decimal avoids rounding drift in a rate.
- **D:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A decimal avoids rounding drift in a rate.

### Question 14 — C

Answer: Use an auto-number column for the case identifier. An auto-number gives each record a readable, unique reference. An auto-number gives every record a readable, unique reference that users can quote. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: An auto-number gives each record a readable, unique reference.
- **B:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: An auto-number gives each record a readable, unique reference.
- **C:** Correct. An auto-number gives every record a readable, unique reference that users can quote. In this case: An auto-number gives each record a readable, unique reference.
- **D:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: An auto-number gives each record a readable, unique reference.

### Question 15 — A, D

Answers: Add a choice column for the fixed set of options; Use a lookup column instead of storing the name as text. A choice constrains the value, and a lookup carries the relationship. A choice constrains input to the approved list and renders as a dropdown on every form. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A choice constrains input to the approved list and renders as a dropdown on every form. In this case: A choice constrains the value, and a lookup carries the relationship.
- **B:** Incorrect for this question. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.
- **D:** Correct. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. In this case: A choice constrains the value, and a lookup carries the relationship.
- **E:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A choice constrains the value, and a lookup carries the relationship.

### Question 16 — D

Answer: Model the many-to-many link with a native N:N relationship. A native N:N relationship handles an intersect where neither side owns the other. A native N:N relationship handles the intersect table when neither side owns the other. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A lookup carries the relationship, so the related record can be filtered, secured, and rolled up. Why the correct answer wins: A native N:N relationship handles an intersect where neither side owns the other.
- **B:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: A native N:N relationship handles an intersect where neither side owns the other.
- **C:** Incorrect for this question. The lookup on the child is what makes the parent select a record rather than a typed string. Why the correct answer wins: A native N:N relationship handles an intersect where neither side owns the other.
- **D:** Correct. A native N:N relationship handles the intersect table when neither side owns the other. In this case: A native N:N relationship handles an intersect where neither side owns the other.

### Question 17 — D

Answer: Keep the relationship referential so child records survive the parent delete. Referential behaviour leaves the parent in place. Referential behaviour leaves the children in place, which is what a shared dimension needs. Local study-map skill 1.7 (Prompt Columns and Row Summaries), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Parental behaviour cascades the delete, which is correct when the child has no meaning alone. Why the correct answer wins: Referential behaviour leaves the parent in place.
- **B:** Incorrect for this question. A native N:N relationship handles the intersect table when neither side owns the other. Why the correct answer wins: Referential behaviour leaves the parent in place.
- **C:** Incorrect for this question. The lookup on the child is what makes the parent select a record rather than a typed string. Why the correct answer wins: Referential behaviour leaves the parent in place.
- **D:** Correct. Referential behaviour leaves the children in place, which is what a shared dimension needs. In this case: Referential behaviour leaves the parent in place.

### Question 18 — C

Answer: Create a public view for the shared filtered list. A public view is shared with everyone who has access to the table. A public view is available to everyone with access to the table, so the team sees the same list. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **B:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: A public view is shared with everyone who has access to the table.
- **C:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: A public view is shared with everyone who has access to the table.
- **D:** Incorrect for this question. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Why the correct answer wins: A public view is shared with everyone who has access to the table.

### Question 19 — B, E

Answers: Create a public view for the shared filtered list; Design the main form around the record the user opens. The public view is the shared list, and the main form is the working surface. A public view is available to everyone with access to the table, so the team sees the same list. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. Local study-map skill 1.8 (Public Views and Main Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **B:** Correct. The main form is the primary editing surface, so it carries the fields and tabs the role actually uses. In this case: The public view is the shared list, and the main form is the working surface.
- **C:** Incorrect for this question. A quick-create form lets a user create the related record without leaving the current one. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **D:** Incorrect for this question. The system view is the fallback for every view and every app, so editing it changes behaviour users did not ask about. Why the correct answer wins: The public view is the shared list, and the main form is the working surface.
- **E:** Correct. A public view is available to everyone with access to the table, so the team sees the same list. In this case: The public view is the shared list, and the main form is the working surface.

### Question 20 — C

Answer: Use a field security profile for the sensitive column. A field security profile hides a column without hiding the record. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **B:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A field security profile hides a column without hiding the record.
- **C:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: A field security profile hides a column without hiding the record.
- **D:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A field security profile hides a column without hiding the record.

### Question 21 — A, C

Answers: Assign a security role that grants only the privileges the role needs; Use a field security profile for the sensitive column. The role grants table privileges, and the profile hides the column. A security role is how Dataverse decides create, read, write, and delete per table. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A security role is how Dataverse decides create, read, write, and delete per table. In this case: The role grants table privileges, and the profile hides the column.
- **B:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **C:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: The role grants table privileges, and the profile hides the column.
- **D:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: The role grants table privileges, and the profile hides the column.
- **E:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: The role grants table privileges, and the profile hides the column.

### Question 22 — B

Answer: Identify the data boundary and licence → choose the environment type → create the solution with its publisher → deploy through the pipeline. The boundary and licence decide the environment type, and the pipeline carries the packaged result. The boundary and licence decide the environment type, and the pipeline carries the packaged result. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Choosing an environment after deploying is how a solution ends up in the wrong data boundary. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the packaged result.
- **B:** Correct. The boundary and licence decide the environment type, and the pipeline carries the packaged result. In this case: The boundary and licence decide the environment type, and the pipeline carries the packaged result.
- **C:** Incorrect for this question. Deployment before packaging has nothing to deploy. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the packaged result.
- **D:** Incorrect for this question. Every step here runs ahead of the decision it depends on. Why the correct answer wins: The boundary and licence decide the environment type, and the pipeline carries the packaged result.

### Question 23 — C

Answer: Identify who must see which records → assign the security role → set the business unit scope → add a field profile for the sensitive column → verify with a test user. Access is designed from the data outward, and a test user proves the result. Access is designed from the data outward, and a test user proves the result. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Verification with no design behind it confirms nothing in particular. Why the correct answer wins: Access is designed from the data outward, and a test user proves the result.
- **B:** Incorrect for this question. Field security is a refinement of the role, not a substitute for it. Why the correct answer wins: Access is designed from the data outward, and a test user proves the result.
- **C:** Correct. Access is designed from the data outward, and a test user proves the result. In this case: Access is designed from the data outward, and a test user proves the result.
- **D:** Incorrect for this question. The role has to exist before scope or field profiles can narrow it. Why the correct answer wins: Access is designed from the data outward, and a test user proves the result.

### Question 24 — C

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.
- **B:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.
- **C:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 25 — B

Answer: Choose the view columns before setting the filter. The columns decide what is readable without opening the record. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: The columns decide what is readable without opening the record.
- **B:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The columns decide what is readable without opening the record.
- **C:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The columns decide what is readable without opening the record.
- **D:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The columns decide what is readable without opening the record.

### Question 26 — D

Answer: Filter the view on the columns the team actually searches. The filter decides which records are in the list. The filter decides which records appear, so it must match the question the list answers. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The filter decides which records are in the list.
- **B:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides which records are in the list.
- **C:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides which records are in the list.
- **D:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides which records are in the list.

### Question 27 — C

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close, and the maker still owns the bindings. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close, and the maker still owns the bindings.
- **B:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close, and the maker still owns the bindings.
- **C:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close, and the maker still owns the bindings.
- **D:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close, and the maker still owns the bindings.

### Question 28 — D

Answer: Share the app and assign the security role that backs it. Sharing grants the app and the role grants the data. Sharing an app grants the app, and the role grants the data; both are needed. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **B:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **C:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **D:** Correct. Sharing an app grants the app, and the role grants the data; both are needed. In this case: Sharing grants the app and the role grants the data.

### Question 29 — D

Answer: Add the chart and the views to a dashboard. A dashboard composes several components onto one page. A dashboard composes several components so a manager sees the whole picture on one page. Local study-map skill 2.5 (Model-Driven Charts and Dashboards), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A chart bound to a view reuses that view's filter instead of duplicating it. Why the correct answer wins: A dashboard composes several components onto one page.
- **B:** Incorrect for this question. The filter decides which records appear, so it must match the question the list answers. Why the correct answer wins: A dashboard composes several components onto one page.
- **C:** Incorrect for this question. Embedding brings a second security model and a refresh dependency into the app. Why the correct answer wins: A dashboard composes several components onto one page.
- **D:** Correct. A dashboard composes several components so a manager sees the whole picture on one page. In this case: A dashboard composes several components onto one page.

### Question 30 — D

Answer: Use the phone layout for field staff. The phone layout controls size and reach on a handheld. The phone layout controls the size and reach of controls on a handheld device. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **C:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **D:** Correct. The phone layout controls the size and reach of controls on a handheld device. In this case: The phone layout controls size and reach on a handheld.

### Question 31 — C

Answer: Add accessible labels and screen-reader text to the controls. A control without a label is unusable with a screen reader. A control without a label is unusable with a screen reader, however clear it looks. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **B:** Incorrect for this question. Colour alone fails for a colour-blind user and for anyone reading the app in high contrast. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **C:** Correct. A control without a label is unusable with a screen reader, however clear it looks. In this case: A control without a label is unusable with a screen reader.
- **D:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: A control without a label is unusable with a screen reader.

### Question 32 — A

Answer: Publish a component library for the shared header and controls. A component library is the reusable, versioned home for a shared control. A component library is the reusable, versioned home for a control that several apps must share. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: A component library is the reusable, versioned home for a shared control.
- **B:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **C:** Incorrect for this question. A named formula evaluates once in the app and is reused by name instead of being copied. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.
- **D:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A component library is the reusable, versioned home for a shared control.

### Question 33 — B

Answer: Use a global variable for the value that the whole app needs. A global variable persists across screens. A global variable persists across screens, which is what a signed-in user's selection needs. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists across screens.
- **B:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists across screens.
- **C:** Incorrect for this question. An un-cleared collection keeps the previous user's rows in memory. Why the correct answer wins: A global variable persists across screens.
- **D:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists across screens.

### Question 34 — D

Answer: Wrap the call in IfError and surface the message to the user. IfError catches the failure and lets the app show a recoverable message. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Why the correct answer wins: IfError catches the failure and lets the app show a recoverable message.
- **B:** Incorrect for this question. Test Studio captures the screens and formulas that a regression would break. Why the correct answer wins: IfError catches the failure and lets the app show a recoverable message.
- **C:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: IfError catches the failure and lets the app show a recoverable message.
- **D:** Correct. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. In this case: IfError catches the failure and lets the app show a recoverable message.

### Question 35 — A

Answer: Run the app in Test Studio before publishing. Test Studio captures the screens and formulas a regression would break. Test Studio captures the screens and formulas that a regression would break. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Test Studio captures the screens and formulas that a regression would break. In this case: Test Studio captures the screens and formulas a regression would break.
- **B:** Incorrect for this question. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **C:** Incorrect for this question. Monitor shows the request, the response, and the timing, which is how a slow or failing call is diagnosed. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.
- **D:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: Test Studio captures the screens and formulas a regression would break.

### Question 36 — B

Answer: Add the Copilot Studio agent to the canvas app as a component. The agent component puts a conversational surface in the app. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: The agent component puts a conversational surface in the app.
- **B:** Correct. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. In this case: The agent component puts a conversational surface in the app.
- **C:** Incorrect for this question. A custom agent is worth its lifecycle cost only when the built-in one cannot reach the data or the process. Why the correct answer wins: The agent component puts a conversational surface in the app.
- **D:** Incorrect for this question. A second app multiplies the maintenance without adding capability. Why the correct answer wins: The agent component puts a conversational surface in the app.

### Question 37 — B

Answer: Configure the forms and views → compose the app in the app designer → set the navigation in the sitemap → share the app → assign the backing security role. The app is composed from finished components, and access is granted last. The app is composed from finished components, and access is granted last. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Navigation is meaningless until the components exist. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **B:** Correct. The app is composed from finished components, and access is granted last. In this case: The app is composed from finished components, and access is granted last.
- **C:** Incorrect for this question. Granting data access before the app exists gives access with nothing to use it in. Why the correct answer wins: The app is composed from finished components, and access is granted last.
- **D:** Incorrect for this question. Sharing an app that has no components shows users an empty shell. Why the correct answer wins: The app is composed from finished components, and access is granted last.

### Question 38 — D

Answer: Connect the data source → build the screens against it → add error handling → test with Monitor and Test Studio → publish the app. The data source comes first, and testing precedes publishing. The data source comes first, and testing precedes publishing. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Error handling has nothing to wrap before the calls exist. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **B:** Incorrect for this question. Screens need a data source, and publishing needs a tested app. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **C:** Incorrect for this question. Publishing before testing is how a broken save reaches users. Why the correct answer wins: The data source comes first, and testing precedes publishing.
- **D:** Correct. The data source comes first, and testing precedes publishing. In this case: The data source comes first, and testing precedes publishing.

### Question 39 — C

Answer: Use an automated trigger on record creation. An automated trigger runs without a user. An automated trigger runs without a user, which is what a background rule needs. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: An automated trigger runs without a user.
- **B:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: An automated trigger runs without a user.
- **C:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: An automated trigger runs without a user.
- **D:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: An automated trigger runs without a user.

### Question 40 — A

Answer: Use a scheduled trigger for the nightly batch. A schedule matches work that must run at a time. A schedule matches work that must run at a time rather than on an event. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A schedule matches work that must run at a time rather than on an event. In this case: A schedule matches work that must run at a time.
- **B:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: A schedule matches work that must run at a time.
- **C:** Incorrect for this question. A manual trigger gives the user the decision about when the process runs. Why the correct answer wins: A schedule matches work that must run at a time.
- **D:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A schedule matches work that must run at a time.

### Question 41 — D

Answer: Trigger when a chosen column changes, with a filter condition. A column filter stops the flow running for irrelevant updates. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: A column filter stops the flow running for irrelevant updates.
- **B:** Incorrect for this question. An automated trigger runs without a user, which is what a background rule needs. Why the correct answer wins: A column filter stops the flow running for irrelevant updates.
- **C:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: A column filter stops the flow running for irrelevant updates.
- **D:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: A column filter stops the flow running for irrelevant updates.

### Question 42 — D

Answer: Use the standard Dataverse connector. The standard connector covers Dataverse natively and is included in the base licence. The standard connector is included in the base licence and covers Dataverse natively. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: The standard connector covers Dataverse natively and is included in the base licence.
- **B:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: The standard connector covers Dataverse natively and is included in the base licence.
- **C:** Incorrect for this question. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Why the correct answer wins: The standard connector covers Dataverse natively and is included in the base licence.
- **D:** Correct. The standard connector is included in the base licence and covers Dataverse natively. In this case: The standard connector covers Dataverse natively and is included in the base licence.

### Question 43 — A

Answer: Build a custom connector for the internal API. A custom connector wraps an authenticated API as a first-class action. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. Local study-map skill 3.2 (Connector Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A custom connector wraps an authenticated API so flows and apps can call it as a first-class action. In this case: A custom connector wraps an authenticated API as a first-class action.
- **B:** Incorrect for this question. A manual copy becomes stale and moves the integration cost to a person. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **C:** Incorrect for this question. The standard connector is included in the base licence and covers Dataverse natively. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.
- **D:** Incorrect for this question. A premium connector is justified when the data lives where no standard connector reaches. Why the correct answer wins: A custom connector wraps an authenticated API as a first-class action.

### Question 44 — D

Answer: Choose the approval type that matches the sign-off the process requires. Everyone must approve is the right type when each approver holds a veto. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **B:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **C:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: Everyone must approve is the right type when each approver holds a veto.
- **D:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: Everyone must approve is the right type when each approver holds a veto.

### Question 45 — B

Answer: Chain two approvals in sequence for the second-level sign-off. A second approval after the first adds a second-level sign-off. A second approval after the first is how a value threshold adds a second approver. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: A second approval after the first adds a second-level sign-off.
- **B:** Correct. A second approval after the first is how a value threshold adds a second approver. In this case: A second approval after the first adds a second-level sign-off.
- **C:** Incorrect for this question. Everyone must approve is the right type when each stakeholder holds a veto. Why the correct answer wins: A second approval after the first adds a second-level sign-off.
- **D:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: A second approval after the first adds a second-level sign-off.

### Question 46 — B

Answer: Send an email and treat silence as approval. Silence is not a decision and leaves no auditable response. Silence is not a decision, and it leaves no auditable response. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Why the correct answer wins: Silence is not a decision and leaves no auditable response.
- **B:** Correct. Silence is not a decision, and it leaves no auditable response. In this case: Silence is not a decision and leaves no auditable response.
- **C:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: Silence is not a decision and leaves no auditable response.
- **D:** Incorrect for this question. Approve or reject, everyone must approve, and first to respond are different business rules. Why the correct answer wins: Silence is not a decision and leaves no auditable response.

### Question 47 — B

Answer: Use Compose to shape the payload the next step consumes. Compose builds the exact object the next action expects. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Compose builds the exact object the next action expects.
- **B:** Correct. Compose builds the exact object the next action expects, which avoids mapping errors downstream. In this case: Compose builds the exact object the next action expects.
- **C:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: Compose builds the exact object the next action expects.
- **D:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Compose builds the exact object the next action expects.

### Question 48 — A

Answer: Parse JSON so later steps can use the fields. Parse JSON turns an opaque body into typed properties. Parse JSON turns an opaque body into typed properties the designer can offer you. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Parse JSON turns an opaque body into typed properties the designer can offer you. In this case: Parse JSON turns an opaque body into typed properties.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **C:** Incorrect for this question. Compose builds the exact object the next action expects, which avoids mapping errors downstream. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.
- **D:** Incorrect for this question. Apply to each iterates the array, which is how one run processes many records. Why the correct answer wins: Parse JSON turns an opaque body into typed properties.

### Question 49 — B

Answer: Use a switch for the multi-way branch. A switch keeps five outcomes readable. A switch keeps four or five outcomes readable where nested conditions become unreadable. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A switch keeps five outcomes readable.
- **B:** Correct. A switch keeps four or five outcomes readable where nested conditions become unreadable. In this case: A switch keeps five outcomes readable.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A switch keeps five outcomes readable.
- **D:** Incorrect for this question. A scope groups steps so a single run-after configuration can catch any failure inside it. Why the correct answer wins: A switch keeps five outcomes readable.

### Question 50 — A

Answer: Configure run after so the failure path actually executes. A step runs only on success until run after allows the failure path. By default a step runs only on success, so the failure branch never fires without this setting. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. By default a step runs only on success, so the failure branch never fires without this setting. In this case: A step runs only on success until run after allows the failure path.
- **B:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: A step runs only on success until run after allows the failure path.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A step runs only on success until run after allows the failure path.
- **D:** Incorrect for this question. A scope groups steps so a single run-after configuration can catch any failure inside it. Why the correct answer wins: A step runs only on success until run after allows the failure path.

### Question 51 — D

Answer: Loop until the record is found with no exit limit. A loop with no bound can consume the flow's quota. A loop with no bound can run until the run timeout, consuming the flow's quota. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A loop with no bound can consume the flow's quota.
- **D:** Correct. A loop with no bound can run until the run timeout, consuming the flow's quota. In this case: A loop with no bound can consume the flow's quota.

### Question 52 — A

Answer: Read the run history to find the failed action and its inputs. The run history shows each action's inputs and outputs. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows each action's inputs and outputs.
- **B:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **C:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: The run history shows each action's inputs and outputs.
- **D:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows each action's inputs and outputs.

### Question 53 — C

Answer: Test the flow with the real trigger payload. A production-shaped payload proves the expressions resolve. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **B:** Incorrect for this question. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Why the correct answer wins: A production-shaped payload proves the expressions resolve.
- **C:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: A production-shaped payload proves the expressions resolve.
- **D:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: A production-shaped payload proves the expressions resolve.

### Question 54 — A

Answer: Turn on static result to test the rest of the flow. Static result pins one action's output so the remaining steps can be tested. Static result pins one action's output so the remaining steps can be tested without re-running it. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Static result pins one action's output so the remaining steps can be tested without re-running it. In this case: Static result pins one action's output so the remaining steps can be tested.
- **B:** Incorrect for this question. A run started with the production-shaped payload is what proves the expressions resolve. Why the correct answer wins: Static result pins one action's output so the remaining steps can be tested.
- **C:** Incorrect for this question. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. Why the correct answer wins: Static result pins one action's output so the remaining steps can be tested.
- **D:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: Static result pins one action's output so the remaining steps can be tested.

### Question 55 — B

Answer: Start from a prompt template in AI Hub. A template carries a tested instruction and the input contract. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **B:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: A template carries a tested instruction and the input contract.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A template carries a tested instruction and the input contract.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A template carries a tested instruction and the input contract.

### Question 56 — B

Answer: Build the prompt from blank. A blank prompt is right when no template covers the task. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **B:** Correct. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. In this case: A blank prompt is right when no template covers the task.
- **C:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A blank prompt is right when no template covers the task.
- **D:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A blank prompt is right when no template covers the task.

### Question 57 — A

Answer: Add typed inputs so the prompt takes values. Typed inputs become the parameters an app or flow supplies. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Typed inputs become the parameters an app or flow supplies.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **C:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.
- **D:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Typed inputs become the parameters an app or flow supplies.

### Question 58 — B

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in approved documents. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.8 (Prompt Inputs and Knowledge), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **B:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in approved documents.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **D:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.

### Question 59 — D

Answer: Choose the model that fits the task instead of the largest available. Matching the model to the task controls cost. Matching the model to the task controls cost and latency without losing the quality the task needs. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Matching the model to the task controls cost.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Matching the model to the task controls cost.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Matching the model to the task controls cost.
- **D:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Matching the model to the task controls cost.

### Question 60 — D

Answer: Call the prompt from the canvas app through its connector. Consuming the published prompt keeps one instruction behind the app. Consuming the published prompt keeps one instruction and one model choice behind every app. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **B:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Consuming the published prompt keeps one instruction behind the app.
- **D:** Correct. Consuming the published prompt keeps one instruction and one model choice behind every app. In this case: Consuming the published prompt keeps one instruction behind the app.

### Question 61 — D

Answer: Call the prompt from the cloud flow action. A flow can run a prompt as a step and store the result. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **C:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: A flow can run a prompt as a step and store the result.
- **D:** Correct. A flow can run a prompt as a step, which is how a generated summary joins an automated process. In this case: A flow can run a prompt as a step and store the result.

### Question 62 — B

Answer: Call the model from the flow and store the result on the record. Calling the model from the flow and storing the result makes the output visible and auditable. Storing the result on the record is what makes the model output visible to the process and the audit. Local study-map skill 3.10 (Consuming Prompts and Models in Apps and Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Calling the model from the flow and storing the result makes the output visible and auditable.
- **B:** Correct. Storing the result on the record is what makes the model output visible to the process and the audit. In this case: Calling the model from the flow and storing the result makes the output visible and auditable.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Calling the model from the flow and storing the result makes the output visible and auditable.
- **D:** Incorrect for this question. A model consumed this way keeps authentication and throttling in one governed place. Why the correct answer wins: Calling the model from the flow and storing the result makes the output visible and auditable.

### Question 63 — A

Answer: Configure a business rule on the table. A business rule enforces a condition or required field without code. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A business rule enforces a condition or required field without code.
- **B:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **C:** Incorrect for this question. Table scope is what makes the rule hold for imports and flows as well as the main form. Why the correct answer wins: A business rule enforces a condition or required field without code.
- **D:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A business rule enforces a condition or required field without code.

### Question 64 — D

Answer: Set the business rule scope to the table so it applies in every form. Table scope makes the rule apply to imports and flows too. Table scope is what makes the rule hold for imports and flows as well as the main form. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Why the correct answer wins: Table scope makes the rule apply to imports and flows too.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: Table scope makes the rule apply to imports and flows too.
- **C:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: Table scope makes the rule apply to imports and flows too.
- **D:** Correct. Table scope is what makes the rule hold for imports and flows as well as the main form. In this case: Table scope makes the rule apply to imports and flows too.

### Question 65 — A

Answer: Model the stages in a business process flow. A business process flow guides a record through stages. A business process flow guides a record through stages and pins the fields each stage needs. Local study-map skill 3.12 (Business Process Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A business process flow guides a record through stages and pins the fields each stage needs. In this case: A business process flow guides a record through stages.
- **B:** Incorrect for this question. A branch lets one process cover two variants without a second process and a duplicate set of stages. Why the correct answer wins: A business process flow guides a record through stages.
- **C:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A business process flow guides a record through stages.
- **D:** Incorrect for this question. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Why the correct answer wins: A business process flow guides a record through stages.

### Question 66 — B

Answer: Use a rollup column to aggregate the child records. A rollup aggregates related rows on a schedule. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **B:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A rollup aggregates related rows on a schedule.
- **C:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A rollup aggregates related rows on a schedule.
- **D:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A rollup aggregates related rows on a schedule.

### Question 67 — B, C

Answers: Use an automated trigger on record creation; Trigger when a chosen column changes, with a filter condition. The automated trigger starts the run, and the filter stops irrelevant updates. An automated trigger runs without a user, which is what a background rule needs. A column filter stops the flow running for updates that cannot affect the outcome. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **B:** Correct. An automated trigger runs without a user, which is what a background rule needs. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.
- **C:** Correct. A column filter stops the flow running for updates that cannot affect the outcome. In this case: The automated trigger starts the run, and the filter stops irrelevant updates.
- **D:** Incorrect for this question. A trigger on every update multiplies runs, cost, and the chance of a loop. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.
- **E:** Incorrect for this question. An HTTP trigger lets an external system start the flow, provided the caller can hold the URL secret. Why the correct answer wins: The automated trigger starts the run, and the filter stops irrelevant updates.

### Question 68 — D, E

Answers: Start and wait for an approval; Choose the approval type that matches the sign-off the process requires. The approval action pauses the run, and the type encodes who must respond. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. Approve or reject, everyone must approve, and first to respond are different business rules. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A schedule matches work that must run at a time rather than on an event. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **B:** Incorrect for this question. A second approval after the first is how a value threshold adds a second approver. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **C:** Incorrect for this question. Silence is not a decision, and it leaves no auditable response. Why the correct answer wins: The approval action pauses the run, and the type encodes who must respond.
- **D:** Correct. Approve or reject, everyone must approve, and first to respond are different business rules. In this case: The approval action pauses the run, and the type encodes who must respond.
- **E:** Correct. The approval action pauses the run and resumes with the outcome, which is what a sign-off needs. In this case: The approval action pauses the run, and the type encodes who must respond.

### Question 69 — A, D

Answers: Wrap the steps in a Scope so one error path handles the failures; Configure run after so the failure path actually executes. A scope groups the steps, and run after makes the failure branch execute. A scope groups steps so a single run-after configuration can catch any failure inside it. By default a step runs only on success, so the failure branch never fires without this setting. Local study-map skill 3.5 (Flow Control with Conditions and Loops), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A scope groups steps so a single run-after configuration can catch any failure inside it. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **B:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **C:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.
- **D:** Correct. By default a step runs only on success, so the failure branch never fires without this setting. In this case: A scope groups the steps, and run after makes the failure branch execute.
- **E:** Incorrect for this question. Concurrency runs iterations in parallel, which is faster but reorders side effects. Why the correct answer wins: A scope groups the steps, and run after makes the failure branch execute.

### Question 70 — B, E

Answers: Read the run history to find the failed action and its inputs; Test the flow with the real trigger payload. The run history shows the wrong value, and a real payload proves the fix. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. A run started with the production-shaped payload is what proves the expressions resolve. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Resubmit replays the same inputs, which is safe only when the actions are idempotent. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **B:** Correct. The run history shows each action's inputs and outputs, which is where the wrong value becomes visible. In this case: The run history shows the wrong value, and a real payload proves the fix.
- **C:** Incorrect for this question. Parse JSON turns an opaque body into typed properties the designer can offer you. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **D:** Incorrect for this question. Static result pins one action's output so the remaining steps can be tested without re-running it. Why the correct answer wins: The run history shows the wrong value, and a real payload proves the fix.
- **E:** Correct. A run started with the production-shaped payload is what proves the expressions resolve. In this case: The run history shows the wrong value, and a real payload proves the fix.

### Question 71 — C, E

Answers: Start from a prompt template in AI Hub; Add the knowledge source so the prompt grounds on approved content. The template supplies the instruction, and knowledge grounds the answer. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **C:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: The template supplies the instruction, and knowledge grounds the answer.
- **D:** Incorrect for this question. A blank prompt is right when no template covers the task, but it means authoring the instruction and test cases yourself. Why the correct answer wins: The template supplies the instruction, and knowledge grounds the answer.
- **E:** Correct. A template carries a tested instruction and the input contract, so the prompt starts from something that works. In this case: The template supplies the instruction, and knowledge grounds the answer.

### Question 72 — A, C

Answers: Choose the model that fits the task instead of the largest available; Add typed inputs so the prompt takes values. Inputs are the parameters, and the model choice controls cost and quality. Matching the model to the task controls cost and latency without losing the quality the task needs. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Typed inputs become the parameters an app or flow supplies when it calls the prompt. In this case: Inputs are the parameters, and the model choice controls cost and quality.
- **B:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **C:** Correct. Matching the model to the task controls cost and latency without losing the quality the task needs. In this case: Inputs are the parameters, and the model choice controls cost and quality.
- **D:** Incorrect for this question. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.
- **E:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Inputs are the parameters, and the model choice controls cost and quality.

### Question 73 — C, E

Answers: Configure a business rule on the table; Enforce the rule in a synchronous plug-in when it must run on every write. A table-scope business rule covers imports, and a synchronous plug-in runs inside the save. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. A synchronous plug-in runs inside the save, so no caller can bypass it. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **B:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **C:** Correct. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **D:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.
- **E:** Correct. A synchronous plug-in runs inside the save, so no caller can bypass it. In this case: A table-scope business rule covers imports, and a synchronous plug-in runs inside the save.

### Question 74 — A, D

Answers: Use a formula column where the rule needs Power Fx; Use a rollup column to aggregate the child records. A formula column recalculates, and a rollup aggregates children. A formula column evaluates a Power Fx expression, which is the current way to express derived values. A rollup sums or counts related rows on a schedule, which is what a parent total needs. Local study-map skill 3.13 (Calculated, Rollup, and Formula Columns), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. A rollup sums or counts related rows on a schedule, which is what a parent total needs. In this case: A formula column recalculates, and a rollup aggregates children.
- **B:** Incorrect for this question. A plug-in is heavier than a column or a business rule and needs a developer to maintain it. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **C:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.
- **D:** Correct. A formula column evaluates a Power Fx expression, which is the current way to express derived values. In this case: A formula column recalculates, and a rollup aggregates children.
- **E:** Incorrect for this question. A calculated column recomputes on read, so it cannot preserve a historic value. Why the correct answer wins: A formula column recalculates, and a rollup aggregates children.

### Question 75 — C

Answer: Decide which event should start the process → add the trigger with a filter → add the actions and branches → test with a real payload → read the run history after the first run. The event decides the trigger, and the real payload decides whether the expressions resolve. The event decides the trigger, and the payload decides whether the expressions actually resolve. Local study-map skill 3.1 (Cloud Flow Triggers), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Actions placed before the trigger cannot know what data they receive. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **B:** Incorrect for this question. There is no payload to test until a trigger and actions exist. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **C:** Correct. The event decides the trigger, and the payload decides whether the expressions actually resolve. In this case: The event decides the trigger, and the real payload decides whether the expressions resolve.
- **D:** Incorrect for this question. A run history only exists after a run has happened. Why the correct answer wins: The event decides the trigger, and the real payload decides whether the expressions resolve.

### Question 76 — A

Answer: Trigger on the submitted request → start and wait for the approval → branch on the outcome → update the record → notify the requester. The branch reads the approval outcome, and the record update carries the decision. The branch reads the approval outcome, and the record update carries the decision. Local study-map skill 3.3 (Approvals in Cloud Flows), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The branch reads the approval outcome, and the record update carries the decision. In this case: The branch reads the approval outcome, and the record update carries the decision.
- **B:** Incorrect for this question. The record cannot be updated with a decision that has not been taken. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **C:** Incorrect for this question. Notifying first tells the requester about a decision that does not exist. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.
- **D:** Incorrect for this question. A branch with no outcome yet has nothing to evaluate. Why the correct answer wins: The branch reads the approval outcome, and the record update carries the decision.

### Question 77 — A

Answer: Reproduce the failure with the real inputs → open the run history → inspect the failing action's inputs and outputs → fix the expression or mapping → resubmit the run. The run history turns a symptom into a specific wrong value. The run history is what turns a symptom into a specific wrong value. Local study-map skill 3.6 (Cloud Flow Testing and Troubleshooting), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. The run history is what turns a symptom into a specific wrong value. In this case: The run history turns a symptom into a specific wrong value.
- **B:** Incorrect for this question. Resubmitting an unfixed flow repeats the same failure. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **C:** Incorrect for this question. A fix applied before diagnosis is a guess. Why the correct answer wins: The run history turns a symptom into a specific wrong value.
- **D:** Incorrect for this question. There is no run to inspect until the failure is reproduced. Why the correct answer wins: The run history turns a symptom into a specific wrong value.

### Question 78 — B

Answer: State the rule in business terms → choose the mechanism that enforces it where it must hold → configure the rule at table scope → test it on the form and through an import → document it for the support team. Choosing the mechanism first stops a form-only rule being used for a table-wide requirement. Choosing the mechanism before configuring anything is what stops a form-only rule being used for a rule that must survive an import. Local study-map skill 3.11 (Business Rules), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Documentation of an unconfigured rule describes an intention, not a system. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **B:** Correct. Choosing the mechanism before configuring anything is what stops a form-only rule being used for a rule that must survive an import. In this case: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **C:** Incorrect for this question. A test needs the configured rule and the stated requirement behind it. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.
- **D:** Incorrect for this question. Configuration before the rule is stated produces a rule nobody agreed to. Why the correct answer wins: Choosing the mechanism first stops a form-only rule being used for a table-wide requirement.

### Question 79 — A

Answer: Create the table in the Dataverse data workspace. The data workspace is where a maker creates and models a new table. The data workspace lets a maker model tables and relationships without leaving the app-building flow. Local study-map skill 1.4 (Tables in the Data Workspace), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. The data workspace lets a maker model tables and relationships without leaving the app-building flow. In this case: The data workspace is where a maker creates and models a new table.
- **B:** Incorrect for this question. Activities model calls, tasks, and appointments, which inherit the timeline and the regarding relationship. Why the correct answer wins: The data workspace is where a maker creates and models a new table.
- **C:** Incorrect for this question. A list has no relationships, security roles, or rollup columns, so the model runs out as soon as the process needs them. Why the correct answer wins: The data workspace is where a maker creates and models a new table.
- **D:** Incorrect for this question. Reusing Account or Contact keeps the built-in relationships, security, and integrations that users already expect. Why the correct answer wins: The data workspace is where a maker creates and models a new table.

### Question 80 — A

Answer: Write a Dataverse plug-in in C#. A plug-in runs on the server inside the save. A plug-in is for server-side logic that must run on every write, not for a screen interaction. Local study-map skill 1.2 (Built-in Agents and Extensibility Options), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A plug-in is for server-side logic that must run on every write, not for a screen interaction. In this case: A plug-in runs on the server inside the save.
- **B:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: A plug-in runs on the server inside the save.
- **C:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A plug-in runs on the server inside the save.
- **D:** Incorrect for this question. PCF is the right answer when the requirement is a visual or interaction the standard control cannot express. Why the correct answer wins: A plug-in runs on the server inside the save.

### Question 81 — A

Answer: Use a currency column with the record currency. A currency column keeps the amount and currency together. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. Local study-map skill 1.6 (Columns and Table Relationships), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Correct. A currency column keeps the amount and its currency together, which matters as soon as two currencies appear. In this case: A currency column keeps the amount and currency together.
- **B:** Incorrect for this question. An auto-number gives every record a readable, unique reference that users can quote. Why the correct answer wins: A currency column keeps the amount and currency together.
- **C:** Incorrect for this question. A decimal avoids the rounding drift that a floating-point column introduces in a rate. Why the correct answer wins: A currency column keeps the amount and currency together.
- **D:** Incorrect for this question. A copied name cannot be joined, renamed, or secured with its source record. Why the correct answer wins: A currency column keeps the amount and currency together.

### Question 82 — A

Answer: Copy the prompt text into each app so it can be tuned per app. Copied prompt text drifts, so the same claim gets different summaries. Copied prompt text drifts, so the same question gets different answers in different apps. Local study-map skill 3.7 (Prompts in AI Hub), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Correct. Copied prompt text drifts, so the same question gets different answers in different apps. In this case: Copied prompt text drifts, so the same claim gets different summaries.
- **B:** Incorrect for this question. A flow can run a prompt as a step, which is how a generated summary joins an automated process. Why the correct answer wins: Copied prompt text drifts, so the same claim gets different summaries.
- **C:** Incorrect for this question. A template carries a tested instruction and the input contract, so the prompt starts from something that works. Why the correct answer wins: Copied prompt text drifts, so the same claim gets different summaries.
- **D:** Incorrect for this question. Consuming the published prompt keeps one instruction and one model choice behind every app. Why the correct answer wins: Copied prompt text drifts, so the same claim gets different summaries.

### Question 83 — D

Answer: Add the knowledge source so the prompt grounds on approved content. Knowledge retrieval grounds the answer in approved documents. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. Local study-map skill 3.9 (Prompt Settings and Model Selection), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Typed inputs become the parameters an app or flow supplies when it calls the prompt. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **B:** Incorrect for this question. Copied prompt text drifts, so the same question gets different answers in different apps. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **C:** Incorrect for this question. Matching the model to the task controls cost and latency without losing the quality the task needs. Why the correct answer wins: Knowledge retrieval grounds the answer in approved documents.
- **D:** Correct. Knowledge retrieval grounds the answer in the documents rather than in the model's memory. In this case: Knowledge retrieval grounds the answer in approved documents.

### Question 84 — C

Answer: Pick the logic mechanism that matches where the rule must hold. A mechanism is chosen by where the rule must hold. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. Local study-map skill 3.14 (Choosing the Right Business Logic), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. A formula column evaluates a Power Fx expression, which is the current way to express derived values. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **B:** Incorrect for this question. A synchronous plug-in runs inside the save, so no caller can bypass it. Why the correct answer wins: A mechanism is chosen by where the rule must hold.
- **C:** Correct. A form script, a business rule, a column, and a plug-in enforce at different points, and only some apply outside the form. In this case: A mechanism is chosen by where the rule must hold.
- **D:** Incorrect for this question. A business rule enforces a condition, visibility, or required field without code and applies to the table, not one form. Why the correct answer wins: A mechanism is chosen by where the rule must hold.

### Question 85 — C, D

Answers: Filter the view on the columns the team actually searches; Choose the view columns before setting the filter. The filter decides the rows, and the columns make them readable. The filter decides which records appear, so it must match the question the list answers. The columns decide what is readable at a glance; the filter decides what is in the list. Local study-map skill 2.2 (Model-Driven Views), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A personal view is private, so every new user starts from the default list instead. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **B:** Incorrect for this question. A public view is available to everyone with access to the table, so the team sees the same list. Why the correct answer wins: The filter decides the rows, and the columns make them readable.
- **C:** Correct. The filter decides which records appear, so it must match the question the list answers. In this case: The filter decides the rows, and the columns make them readable.
- **D:** Correct. The columns decide what is readable at a glance; the filter decides what is in the list. In this case: The filter decides the rows, and the columns make them readable.
- **E:** Incorrect for this question. FetchXML is powerful but bypasses the visual designer the next maker will use. Why the correct answer wins: The filter decides the rows, and the columns make them readable.

### Question 86 — A, C

Answers: Publish a component library for the shared header and controls; Define a named formula for the shared calculation. The library shares the control, and the named formula shares the calculation. A component library is the reusable, versioned home for a control that several apps must share. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. A component library is the reusable, versioned home for a control that several apps must share. In this case: The library shares the control, and the named formula shares the calculation.
- **B:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **C:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: The library shares the control, and the named formula shares the calculation.
- **D:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.
- **E:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: The library shares the control, and the named formula shares the calculation.

### Question 87 — D, E

Answers: Use a global variable for the value that the whole app needs; Wrap the call in IfError and surface the message to the user. A global variable persists, and IfError handles the failure. A global variable persists across screens, which is what a signed-in user's selection needs. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Trace records what happened in a session, which is what support needs after a failed save. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **B:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **C:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: A global variable persists, and IfError handles the failure.
- **D:** Correct. IfError catches the failure and lets the app show a recoverable message instead of a silent blank. In this case: A global variable persists, and IfError handles the failure.
- **E:** Correct. A global variable persists across screens, which is what a signed-in user's selection needs. In this case: A global variable persists, and IfError handles the failure.

### Question 88 — B

Answer: Apply to each over the returned rows. Apply to each iterates the array. Apply to each iterates the array, which is how one run processes many records. Local study-map skill 3.4 (Cloud Flow Actions and Data Operations), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Automate cloud flows and AI Hub: https://learn.microsoft.com/en-us/power-automate/

- **A:** Incorrect for this question. Do until repeats until the condition holds, and the count limit is what stops an infinite loop. Why the correct answer wins: Apply to each iterates the array.
- **B:** Correct. Apply to each iterates the array, which is how one run processes many records. In this case: Apply to each iterates the array.
- **C:** Incorrect for this question. A condition is the explicit branch that makes the two paths readable in the run history. Why the correct answer wins: Apply to each iterates the array.
- **D:** Incorrect for this question. A switch keeps four or five outcomes readable where nested conditions become unreadable. Why the correct answer wins: Apply to each iterates the array.

### Question 89 — C

Answer: Generate the page from a natural-language description, then refine it. A generative page gets the layout close quickly. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. Local study-map skill 2.3 (Generative Pages), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An unreviewed page can bind to a table the audience should not read. Why the correct answer wins: A generative page gets the layout close quickly.
- **B:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A generative page gets the layout close quickly.
- **C:** Correct. A generative page gets the layout close quickly, and the maker still owns the data bindings and access. In this case: A generative page gets the layout close quickly.
- **D:** Incorrect for this question. A generative page complements the form; replacing it drops the scripting and business rules attached to it. Why the correct answer wins: A generative page gets the layout close quickly.

### Question 90 — D

Answer: Use the phone layout for field staff. The phone layout controls size and reach on a handheld. The phone layout controls the size and reach of controls on a handheld device. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. The tablet layout gives the room a wide screen needs and stays readable on a laptop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **B:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **C:** Incorrect for this question. A fixed width is either cut off on a phone or stranded in the middle of a desktop. Why the correct answer wins: The phone layout controls size and reach on a handheld.
- **D:** Correct. The phone layout controls the size and reach of controls on a handheld device. In this case: The phone layout controls size and reach on a handheld.

### Question 91 — B

Answer: Choose the environment type that matches the data boundary and the licence. Environment type sets the boundary and licensing. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. Local study-map skill 1.3 (Environment Types, Solutions, and ALM), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. A trial environment expires, taking the solution and its data with it. Why the correct answer wins: Environment type sets the boundary and licensing.
- **B:** Correct. Environment type decides data residency, capacity, and which features are available, so it follows the requirement rather than convenience. In this case: Environment type sets the boundary and licensing.
- **C:** Incorrect for this question. The default environment has the widest membership and the least governance, which is where a regulated solution should not start. Why the correct answer wins: Environment type sets the boundary and licensing.
- **D:** Incorrect for this question. One environment cannot separate an unfinished change from live data. Why the correct answer wins: Environment type sets the boundary and licensing.

### Question 92 — C

Answer: Add accessible labels and screen-reader text to the controls. A control without a label is unusable with a screen reader. A control without a label is unusable with a screen reader, however clear it looks. Local study-map skill 2.7 (Accessibility, Performance, and Responsiveness), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Responsive containers reflow, so one app fits a phone and a desktop without two layouts. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **B:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: A control without a label is unusable with a screen reader.
- **C:** Correct. A control without a label is unusable with a screen reader, however clear it looks. In this case: A control without a label is unusable with a screen reader.
- **D:** Incorrect for this question. Colour alone fails for a colour-blind user and for anyone reading the app in high contrast. Why the correct answer wins: A control without a label is unusable with a screen reader.

### Question 93 — A

Answer: Write the filter so the data source performs the delegation. Delegation keeps the query on the source. Delegation sends the query to the source, so the app never downloads more rows than it can handle. Local study-map skill 2.6 (Canvas Apps Built From Data), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Delegation sends the query to the source, so the app never downloads more rows than it can handle. In this case: Delegation keeps the query on the source.
- **B:** Incorrect for this question. A local filter only sees the rows the app already fetched, so results silently truncate. Why the correct answer wins: Delegation keeps the query on the source.
- **C:** Incorrect for this question. A collection is the right tool for a shaped, temporary set that the app manipulates. Why the correct answer wins: Delegation keeps the query on the source.
- **D:** Incorrect for this question. Generating from data gives working screens over the chosen tables immediately. Why the correct answer wins: Delegation keeps the query on the source.

### Question 94 — B

Answer: Use a field security profile for the sensitive column. A field security profile hides a column while the record stays visible. Field security is the only control that hides a column while the record stays visible. Local study-map skill 1.9 (Record and Column Security), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Platform data models, environments, and ALM: https://learn.microsoft.com/en-us/power-platform/alm/

- **A:** Incorrect for this question. Team ownership shares one queue of records without granting each member the owner role. Why the correct answer wins: A field security profile hides a column while the record stays visible.
- **B:** Correct. Field security is the only control that hides a column while the record stays visible. In this case: A field security profile hides a column while the record stays visible.
- **C:** Incorrect for this question. Business units partition ownership; moving a user changes far more than one record. Why the correct answer wins: A field security profile hides a column while the record stays visible.
- **D:** Incorrect for this question. A security role is how Dataverse decides create, read, write, and delete per table. Why the correct answer wins: A field security profile hides a column while the record stays visible.

### Question 95 — D

Answer: Define a named formula for the shared calculation. A named formula is reused by name instead of copied. A named formula evaluates once in the app and is reused by name instead of being copied. Local study-map skill 2.8 (Reusable Components, Named Formulas, and Functions), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A component library is the reusable, versioned home for a control that several apps must share. Why the correct answer wins: A named formula is reused by name instead of copied.
- **B:** Incorrect for this question. A copy is a fork: the next design change has to be made in every app. Why the correct answer wins: A named formula is reused by name instead of copied.
- **C:** Incorrect for this question. A user-defined function takes parameters, which is what a repeated calculation with inputs needs. Why the correct answer wins: A named formula is reused by name instead of copied.
- **D:** Correct. A named formula evaluates once in the app and is reused by name instead of being copied. In this case: A named formula is reused by name instead of copied.

### Question 96 — D

Answer: Collect the rows into a collection for in-memory work. A collection is the right tool for a shaped, temporary set. A collection is the right tool for a shaped, temporary set that the app manipulates. Local study-map skill 2.9 (Variables, Collections, and Error Handling), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. An un-cleared collection keeps the previous user's rows in memory. Why the correct answer wins: A collection is the right tool for a shaped, temporary set.
- **B:** Incorrect for this question. A global variable persists across screens, which is what a signed-in user's selection needs. Why the correct answer wins: A collection is the right tool for a shaped, temporary set.
- **C:** Incorrect for this question. A context variable lives with the screen, so it cannot leak into an unrelated part of the app. Why the correct answer wins: A collection is the right tool for a shaped, temporary set.
- **D:** Correct. A collection is the right tool for a shaped, temporary set that the app manipulates. In this case: A collection is the right tool for a shaped, temporary set.

### Question 97 — B

Answer: Add the Copilot Studio agent to the canvas app as a component. The agent component adds a conversational surface to the app. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. Local study-map skill 2.10 (Canvas App Testing and Copilot Studio Agents), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. Calling the endpoint directly bypasses the agent component's authentication and telemetry. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **B:** Correct. The agent component puts a conversational surface in the app while the agent keeps its own topics and knowledge. In this case: The agent component adds a conversational surface to the app.
- **C:** Incorrect for this question. A second app multiplies the maintenance without adding capability. Why the correct answer wins: The agent component adds a conversational surface to the app.
- **D:** Incorrect for this question. Test Studio captures the screens and formulas that a regression would break. Why the correct answer wins: The agent component adds a conversational surface to the app.

### Question 98 — B

Answer: Add the columns the role uses to the main form. A form carries the working set of fields for the role. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Incorrect for this question. A form script can hide or validate fields, but it does not enforce anything when the record is written elsewhere. Why the correct answer wins: A form carries the working set of fields for the role.
- **B:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: A form carries the working set of fields for the role.
- **C:** Incorrect for this question. Tabs keep a forty-column form scannable without hiding the fields behind a click. Why the correct answer wins: A form carries the working set of fields for the role.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: A form carries the working set of fields for the role.

### Question 99 — A

Answer: Share the app and assign the security role that backs it. Sharing grants the app and the role grants the data. Sharing an app grants the app, and the role grants the data; both are needed. Local study-map skill 2.4 (Model-Driven App Composition and Access), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Sharing an app grants the app, and the role grants the data; both are needed. In this case: Sharing grants the app and the role grants the data.
- **B:** Incorrect for this question. The sitemap is the app's menu, so it decides what a user can reach at all. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **C:** Incorrect for this question. The app designer decides which components the app exposes, so composition is a security-relevant choice. Why the correct answer wins: Sharing grants the app and the role grants the data.
- **D:** Incorrect for this question. An app is not a permission boundary in Dataverse; the role is. Why the correct answer wins: Sharing grants the app and the role grants the data.

### Question 100 — A, B

Answers: Organize the long form into tabs and sections; Add the columns the role uses to the main form. The columns are the working set, and tabs keep the form scannable. Tabs keep a forty-column form scannable without hiding the fields behind a click. A form carries the working set of fields; everything else belongs in a tab or a view. Local study-map skill 2.1 (Model-Driven Forms), mapped to the official guide: Microsoft AB-410 study guide, skills measured as of October 16, 2026 Primary reference: Power Apps model-driven and canvas apps: https://learn.microsoft.com/en-us/power-apps/maker/

- **A:** Correct. Tabs keep a forty-column form scannable without hiding the fields behind a click. In this case: The columns are the working set, and tabs keep the form scannable.
- **B:** Correct. A form carries the working set of fields; everything else belongs in a tab or a view. In this case: The columns are the working set, and tabs keep the form scannable.
- **C:** Incorrect for this question. A card form gives a compact editing surface for a handful of fields. Why the correct answer wins: The columns are the working set, and tabs keep the form scannable.
- **D:** Incorrect for this question. The columns decide what is readable at a glance; the filter decides what is in the list. Why the correct answer wins: The columns are the working set, and tabs keep the form scannable.
- **E:** Incorrect for this question. A form script only affects that form, so the field is still editable everywhere else. Why the correct answer wins: The columns are the working set, and tabs keep the form scannable.

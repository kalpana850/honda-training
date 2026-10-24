1. What is automation?

Automation means making a computer perform repetitive tasks automatically instead of doing them manually every time.

Imagine you are a developer and you write code every day. Whenever you update your code, you might need to:
- Run tests to check whether the code works.
- Check for errors.
- Build the application.
- Upload or deploy the application.
Doing all of these manually every time takes effort. Automation lets the computer do these tasks for you.

Without automation-

You run tests, check errors, build the project, and upload it manually.

With automation-

You configure the steps once, and the computer performs them when the specified event occurs.

2. What is a CI workflow?

CI stands for Continuous Integration.

It is a development practice in which developers frequently merge their code changes into a shared repository, and automated checks help identify problems early.

A CI workflow is the set of automated steps that checks your code whenever a particular event occurs.

For example, GitHub Actions can run a CI workflow whenever you push code to GitHub.

1. Write or update code

You make changes to your project.

2. Push code to GitHub

Your changes are uploaded to the repository.

3. CI workflow starts

GitHub Actions starts the configured tasks.

Tests pass - Continue to the next step.


Tests fail - Show errors so you can fix them.


Think of CI as an automatic quality checker for your code.

It does not necessarily deploy your application. Its main purpose is to help detect errors early.

3. What is GitHub Actions?
GitHub Actions is a tool that lets you automate tasks directly within your GitHub repository.

You can use it to:
- Run tests automatically.
- Build Java, Python, or JavaScript applications.
- Check code quality.
- Publish packages to GitHub Packages.
- Deploy applications.
- Run scheduled tasks.
To use it, you generally create a YAML file inside your repository's .github/workflows/ directory.

For example:

.github/workflows/ci.yml

The .yml or .yaml file contains instructions describing what should trigger the workflow and what tasks it should perform.

4. Understand the important terms
Term	Simple meaning
Workflow	The complete automated process.
Event / Trigger	What starts the process, such as pushing code.
Job	A group of tasks that run together.
Step	One individual task inside a job.
Runner	The computer or virtual machine that executes the tasks.
Action	A reusable component that helps perform a task.

Practical Example of CI workflow:

name: Java CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Get the code
        uses: actions/checkout@v4

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: Run tests and build
        run: mvn -B verify



6. How automation, CI, and CD are related

These terms are connected, but they are not identical.
Automation
Any repetitive task performed automatically.

Example: Automatically organize or process files.


CI - Continuous Integration
Automatically build and test code changes.

Example: Check whether your Java application passes its tests.


CD - Continuous Delivery / Deployment
Automate the process of preparing or releasing software.

Continuous Delivery keeps software ready for release; Continuous Deployment automatically releases qualifying changes to production.


CI (Continuous Integration) Workflow Chart
1. Developer writes code

2. Commit and push code to GitHub

3. CI workflow triggers automatically

GitHub Actions

4. Build the application

5. Run automated tests

6. Tests successful?

YES

Continue to merge or release.


NO

Fix errors and push again.
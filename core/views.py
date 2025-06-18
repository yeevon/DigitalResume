from django.shortcuts import render

# Create your views here.
def home(request):
    jobs = [
        {
            "title": "S-Nimbus",
            "role": "Senior QA Engineer",
            "dates": "10/24 – Present",
            "url": "https://snimbus.ai/",
            "summary": "I lead a team in building automation test suites for over 30 applications, focusing on API and " +
                    "UI testing using Selenium with Java. Developed flexible templates to create custom frameworks " +
                    "tailored to individual application requirements. Coordinated with developers and business " +
                    "stakeholders to ensure testing solutions align with project needs.",
            "bullets": [
                "Contributed to CI/CD pipeline integration, ensuring automated test suites were seamlessly executed in dev workflows.",
                "Implemented scalable automation frameworks, enabling seamless test execution across multiple applications.",
                "Designed and maintained flexible templates to streamline the creation of custom automation frameworks.",
                "Led automation efforts for both API and UI testing, ensuring comprehensive test coverage.",
                "Verified application performance and reliability through automated regression and functional testing.",
                "Trained team members in best practices for automation testing, fostering a culture of quality and efficiency.",
                "Collaborated on full-stack feature validation efforts, supporting frontend/backend debugging and integration with development teams.",
            ]
        },
        {
            "title": "SID, Inc.",
            "role": "Senior QA Engineer",
            "dates": "01/23 – 10/24",
            "url": "https://www.sidonline.com/",
            "summary": "I led QA efforts for a government contract for the DMDC, focusing on automation (C# with Selenium), " +
                        "API testing, and database validation. Created and executed test cases to validate user stories, built " +
                        "unit test standards, and provided regular reporting through Jira.",
            "bullets": [
                "Designed and maintained a custom regression suite in C# with Selenium, integrated into CI workflows for faster release cycles.",
                "Developed handoff documentation to ensure seamless project transitions.",
                "Delivered training and process docs for onboarding new testers.",
                "Verified data accuracy using SQL across multiple testing environments.",
                "Collaborated with cross-functional teams and developers to launch modernized features, improving coverage and release confidence.",
                "Contributed to backend testing strategy and supported development of test utilities to improve team velocity.",
            ],
            "accomplishments":[
                "Assisted in modernizing DMDC's WageMod application by integrating a modern tech stack, reducing reliance on legacy systems.",
                "Built an automation framework in C# with Selenium that cut regression time and improved deployment speed.",
                "Helped design a new field data system for agents, improving accuracy and efficiency.",
                "Reduced technical debt through reusable test modules and development-aligned QA practices.",
            ],
        },
        {
            "title": "USAA",
            "role": "QA Engineer",
            "dates": "2017 - 2023",
            "url": "https://www.usaa.com/?akredirect=true",
            "summary": "Managed a team of on/off-site resources in QA effort. I trained 12 teams in testing " +
                        "methodology, automation, documentation, and IT compliance. Supervised the introduction " + 
                        "of new tools to the organization. Collaborated with the team on accessibility, security, " + 
                        "and performance testing. Built a website to report regression testing status across all " + 
                        "test environments. Developed UI to trigger a limited number of regression tests for business.",
            "bullets": [
                "Prioritized production bugs with the program team. I documented test cases and bugs.",
                "Launched functional automated test to the CI/CD Pipeline, increasing speed to market.",
                "I championed automated Unit, API, and Functional testing.",
                "Designed automated regression for legacy applications.",
                "Created test case documentation for Auto and Consumer Lending teams.",
                "I devised an automated functional test framework with WebdriverIO and TestIM for Lending.",
                "Assisted Development team in creating Unit test with Jest",
                "Updated and Maintained Mobile automation framework built with Appium",
            ]
        },
        {
            "title": "Camp Systems",
            "role": "QA Engineer",
            "dates": "2014 - 2016",
            "url": "https://www.campsystems.com/",
            "summary": "Generated test case execution and defect reports. I took care of updating, creating, " +
                        "and pruning manual test cases for the system on both mobile and web platforms. Streamlined " +
                        "the process to facilitate testing of new user stories and improved regression testing. " +
                        "Leveraged Agile and Scrum project management practices, transitioning existing project " +
                        "requirements to user stories. Collaborated with the development team to complete user " +
                        "stories.",
            "bullets": [
                "I endorsed improving the documentation process and user guides.",
                "Built custom Automation Test framework in C# with Selenium WebDriver.",
                "Conceptualized documentation strategy for test cases using Zephyr.",
                "Wrote SQL queries to get data to validate test scenarios. Performed SIT, Regression, and Post Implementation Testing.",
                "Documented defects in Jira, linking them to test cases built in Zephyr.",
            ]
        },
    ]

    club_tiles = [
        {
            "title": "Coding United GitHub",
            "description": "As president, I manage the org repo, plan weekly challenges, and mentor contributors.",
            "link": "https://github.com/codingUnited",
            "icon": "github",  # special rendering case
        },
        {
            "title": "Lorem Ipseum ",
            "description": "Dolor sit amet, consectetur adipiscing",
        },
        {
            "title": "Lorem Ipsum",
            "description": "Dolor sit amet, consectetur adipiscing",
        },
        {
            "title": "Lorem Ipsum",
            "description": "Dolor sit amet, consectetur adipiscing",
        },
        {
            "title": "Lorem Ipsum",
            "description": "Dolor sit amet, consectetur adipiscing",
        },
    ]

    skills = ['JavaScript', 'Python', 'Django', 'Docker']
    
    return render(request, "core/home.html", {
        "jobs": jobs, 
        'skills':skills,
        'club_tiles':club_tiles,
        })

def fun(request):
    return render(request, "core/fun.html")
import unittest
from unittest.mock import Mock, patch
from app import *
from models import *
class UT_A_FilterRoleStaff(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        ####################################################
        # UNIT TEST - POST JSON PASSED TO API
        ####################################################

        self.json_blank = {}
        self.utA002json = {"search": "Engineer"}
        self.utA003json = {"search": "Geographer"}
        self.utA004json = {"department": ["HR"]}
        self.utA005json = {"department": ["Design Lab"]}
        self.utA006json = {"department": ["HR", "SOLUTIONING"]}
        self.utA007json = {"skills": ["System Integration"]}
        self.utA008json = {"skills": ["Computing"]}
        self.utA009json = {"skills": ["System Integration", "Network Administration and Maintenance"]}
        self.utA010json = {"skills": ["System Integration", "Budgeting"]}
        self.utA011json = {"search": "engineer", "department": ["SOLUTIONING"]}
        self.utA012json = {"search": "Account Manager", "department": ["IT"]}
        self.utA013json = {"search": "Developer", "skills": ["System Integration"]}
        self.utA014json = {"search": "Account Manager", "skills": ["System Integration"]}
        self.utA015json = {"department": ["SOLUTIONING"], "skills": ["Stakeholder Management"]}
        self.utA016json = {"department": ["DESIGN LAB"], "skills": ["Stakeholder Management"]}
        self.utA017json = {"search": "Engineer", "jobtype": ["PT"]}
        self.utA018json = {"search": "Admin", "jobtype": ["PT"]}
        self.utA019json = {"search": "Engineer", "department": ["SOLUTIONING"], "skills": ["Stakeholder Management"]}
        self.utA020json = {"search": "Engineer", "department": ["HR"], "skills": ["Stakeholder Management"]}

        ####################################################
        # UNIT TEST - LISTS / OBJECTS TO PATCH SQLALCHEMY
        ####################################################

        self.utA001RoleNameQuery = [
            Role(
                active_status=True,
                department="SALES",
                expiry_dt="Wed, 15 Nov 2023 23:59:59 GMT",
                hiring_manager_id=140944,
                job_description="The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analysing, and summarising sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organisation's products and services, as well as trends, developments and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused and persistent individual, who takes rejection as a personal challenge to succeed when given opportunity. He appreciates the value of long lasting relationships and prioritises efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily.",
                job_type="FT",
                original_creation_dt="Wed, 15 Feb 2023 08:30:00 GMT",
                role_id=1,
                role_listing_ver=0,
                role_name="Account Manager",
                upd_dt="Wed, 15 Feb 2023 08:30:00 GMT",
                upd_hiring_manager_id=140944
            ),
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 17 Nov 2023 23:59:59 GMT",
                hiring_manager_id=160318,
                job_description="Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                job_type="FT",
                original_creation_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                role_id=2,
                role_listing_ver=0,
                role_name="Admin Executive",
                upd_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                upd_hiring_manager_id=160318
            )
        ]

        self.utA002RoleNameQuery = [
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Thu, 28 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140001,
                job_description="The Engineering Director is responsible for spearheading the strategic planning, design and implementation of complex engineering solutions to meet customers requirements. He/She drives direction and strategy for the development and execution of engineering projects, and ensures alignment to the organisational strategy, vision and mission. He formulates strategies and frameworks to drive workplace health, safety, risk and environmental management in accordance with local and international regulations. He develops the organisations technology roadmap and drives continuous improvement strategies. In addition, he leverages his deep technical expertise and industry experience to develop technical capabilities and domain expertise for the organisation. He is a professional engineer, specialising in mechanical, electrical, control and instrumentation, civil, structural or geotechnical engineering disciplines.\r\n\r\nHe is the organisations technical expert who advises senior management and business partners on complex engineering matters. He maintains and builds strong links with the external engineering community and establishes best practises in the implementation of engineering standards and design. He is a strategic and creative thinker, demonstrates exceptional leadership and problem-solving skills, and establishes strategic partnerships.",
                job_type="FT",
                original_creation_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                role_id=7,
                role_listing_ver=0,
                role_name="Engineering Director",
                upd_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                upd_hiring_manager_id=140001
            ),
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=150866,
                job_description="The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. \r\n\r\nThe Junior Engineershould possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.",
                job_type="PT",
                original_creation_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                role_id=15,
                role_listing_ver=0,
                role_name="Junior Engineer",
                upd_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                upd_hiring_manager_id=150866
            ),
            Role(
                active_status=False,
                department="ENGINEERING",
                expiry_dt="Fri, 06 Oct 2023 23:59:59 GMT",
                hiring_manager_id=151443,
                job_description="The Senior Engineer applies advanced engineering principles and techniques to troubleshoot complex engineering problems encountered within the manufacturing facility and provides expert technical advice to guide the installation and maintenance of equipment and systems. He/She is expected to lead the technical cross-collaboration with the Process Development/Manufacturing Science and Technology (PD/MSAT) department in order to identify appropriate biopharmaceuticals manufacturing equipment and optimise their functionalities. The Senior Engineer leads manufacturing equipment and systems innovation projects by guiding feasibility assessments and tests on new technologies. He is expected to review and approve solutions and initiatives to optimise machine availability while managing energy and utility use. He sets parameters for equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. The Principal/Engineer must ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview.\r\n\r\nThe Engineering and Maintenance Principal/Engineer carries the responsibility of the in-house technical expert. He should possess a deep passion for analysing and resolving multifaceted engineering problems and be able to apply advanced critical and analytical thinking skills to deal with immediate situations. He should have a developmental and amiable approach in his interactions working as part of a team while guiding and mentoring others. He must also be able to communicate engineering concepts in a manner that will be understood by others within and beyond the team.",
                job_type="FT",
                original_creation_dt="Sun, 27 Aug 2023 14:50:00 GMT",
                role_id=20,
                role_listing_ver=0,
                role_name="Senior Engineer",
                upd_dt="Sun, 27 Aug 2023 14:50:00 GMT",
                upd_hiring_manager_id=151443
            ),
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA003RoleNameQuery = []

        self.utA004RoleNameQuery = [
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 17 Nov 2023 23:59:59 GMT",
                hiring_manager_id=160318,
                job_description="Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                job_type="FT",
                original_creation_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                role_id=2,
                role_listing_ver=0,
                role_name="Admin Executive",
                upd_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                upd_hiring_manager_id=160318
            ),
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=190059,
                job_description="TheHR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.\r\n\r\nThe HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.",
                job_type="FT",
                original_creation_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                role_id=11,
                role_listing_ver=0,
                role_name="HR Director",
                upd_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                upd_hiring_manager_id=190059
            )
        ]

        self.utA005RoleNameQuery = []

        self.utA006RoleNameQuery = [
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 17 Nov 2023 23:59:59 GMT",
                hiring_manager_id=160318,
                job_description="Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                job_type="FT",
                original_creation_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                role_id=2,
                role_listing_ver=0,
                role_name="Admin Executive",
                upd_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                upd_hiring_manager_id=160318
            ),
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=190059,
                job_description="TheHR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.\r\n\r\nThe HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.",
                job_type="FT",
                original_creation_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                role_id=11,
                role_listing_ver=0,
                role_name="HR Director",
                upd_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                upd_hiring_manager_id=190059
            ),
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA007SkillsQuery = [
            RoleListingSkills(
                role_id=6,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            )
        ]

        self.utA007RoleNameQuery1 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Thu, 07 Dec 2023 23:59:59 GMT",
                hiring_manager_id=171018,
                job_description="The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                job_type="FT",
                original_creation_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                role_id=6,
                role_listing_ver=0,
                role_name="Developer",
                upd_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                upd_hiring_manager_id=171018
            )
        ]
        self.utA007RoleNameQuery2 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA008SkillsQuery = []

        self.utA009SkillsQuery = [
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="Network Administration and Maintenance",
                skills_proficiency=3
            )
        ]

        self.utA009RoleNameQuery = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA010SkillsQuery = []

        self.utA011RoleNameQuery = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA012RoleNameQuery = []

        self.utA013SkillsQuery = [
            RoleListingSkills(
                role_id=6,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            )
        ]

        self.utA013RoleNameQuery1 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Thu, 07 Dec 2023 23:59:59 GMT",
                hiring_manager_id=171018,
                job_description="The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                job_type="FT",
                original_creation_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                role_id=6,
                role_listing_ver=0,
                role_name="Developer",
                upd_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                upd_hiring_manager_id=171018
            )
        ]

        self.utA013RoleNameQuery2 = []

        self.utA014SkillsQuery = [
            RoleListingSkills(
                role_id=6,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="System Integration",
                skills_proficiency=1
            )
        ]

        self.utA014RoleNameQuery1 = []
        self.utA014RoleNameQuery2 = []

        self.utA015SkillsQuery = [
            RoleListingSkills(
                role_id=6,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            )
        ]

        self.utA015RoleNameQuery1 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Thu, 07 Dec 2023 23:59:59 GMT",
                hiring_manager_id=171018,
                job_description="The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                job_type="FT",
                original_creation_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                role_id=6,
                role_listing_ver=0,
                role_name="Developer",
                upd_dt="Sat, 10 Jun 2023 16:55:00 GMT",
                upd_hiring_manager_id=171018
            )
        ]

        self.utA015RoleNameQuery2 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]

        self.utA016SkillsQuery = [
            RoleListingSkills(
                role_id=6,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            )
        ]

        self.utA016RoleNameQuery1 = []
        self.utA016RoleNameQuery2 = []

        self.utA017RoleNameQuery = [
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Thu, 28 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140001,
                job_description="The Engineering Director is responsible for spearheading the strategic planning, design and implementation of complex engineering solutions to meet customers requirements. He/She drives direction and strategy for the development and execution of engineering projects, and ensures alignment to the organisational strategy, vision and mission. He formulates strategies and frameworks to drive workplace health, safety, risk and environmental management in accordance with local and international regulations. He develops the organisations technology roadmap and drives continuous improvement strategies. In addition, he leverages his deep technical expertise and industry experience to develop technical capabilities and domain expertise for the organisation. He is a professional engineer, specialising in mechanical, electrical, control and instrumentation, civil, structural or geotechnical engineering disciplines.\r\n\r\nHe is the organisations technical expert who advises senior management and business partners on complex engineering matters. He maintains and builds strong links with the external engineering community and establishes best practises in the implementation of engineering standards and design. He is a strategic and creative thinker, demonstrates exceptional leadership and problem-solving skills, and establishes strategic partnerships.",
                job_type="FT",
                original_creation_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                role_id=7,
                role_listing_ver=0,
                role_name="Engineering Director",
                upd_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                upd_hiring_manager_id=140001
            ),
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=150866,
                job_description="The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. \r\n\r\nThe Junior Engineershould possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.",
                job_type="PT",
                original_creation_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                role_id=15,
                role_listing_ver=0,
                role_name="Junior Engineer",
                upd_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                upd_hiring_manager_id=150866
            ),
        ]

        self.utA018RoleNameQuery = [
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 17 Nov 2023 23:59:59 GMT",
                hiring_manager_id=160318,
                job_description="Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                job_type="FT",
                original_creation_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                role_id=2,
                role_listing_ver=0,
                role_name="Admin Executive",
                upd_dt="Wed, 02 Aug 2023 14:45:00 GMT",
                upd_hiring_manager_id=160318
            ),
            Role(
                active_status=True,
                department="HR",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=190059,
                job_description="TheHR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.\r\n\r\nThe HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.",
                job_type="FT",
                original_creation_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                role_id=11,
                role_listing_ver=0,
                role_name="HR Director",
                upd_dt="Wed, 28 Jun 2023 19:40:00 GMT",
                upd_hiring_manager_id=190059
            )
        ]

        self.utA019SkillsQuery = [
            RoleListingSkills(
                role_id=7,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            ),
            RoleListingSkills(
                role_id=15,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            ),
            RoleListingSkills(
                role_id=20,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            ),
            RoleListingSkills(
                role_id=22,
                role_listing_ver=0,
                skills="Stakeholder Management",
                skills_proficiency=2
            )
        ]


        self.utA0019RoleNameQuery1 = [
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Thu, 28 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140001,
                job_description="The Engineering Director is responsible for spearheading the strategic planning, design and implementation of complex engineering solutions to meet customers requirements. He/She drives direction and strategy for the development and execution of engineering projects, and ensures alignment to the organisational strategy, vision and mission. He formulates strategies and frameworks to drive workplace health, safety, risk and environmental management in accordance with local and international regulations. He develops the organisations technology roadmap and drives continuous improvement strategies. In addition, he leverages his deep technical expertise and industry experience to develop technical capabilities and domain expertise for the organisation. He is a professional engineer, specialising in mechanical, electrical, control and instrumentation, civil, structural or geotechnical engineering disciplines.\r\n\r\nHe is the organisations technical expert who advises senior management and business partners on complex engineering matters. He maintains and builds strong links with the external engineering community and establishes best practises in the implementation of engineering standards and design. He is a strategic and creative thinker, demonstrates exceptional leadership and problem-solving skills, and establishes strategic partnerships.",
                job_type="FT",
                original_creation_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                role_id=7,
                role_listing_ver=0,
                role_name="Engineering Director",
                upd_dt="Thu, 27 Jul 2023 09:10:00 GMT",
                upd_hiring_manager_id=140001
            )
        ]
        self.utA0019RoleNameQuery2 = [
            Role(
                active_status=True,
                department="ENGINEERING",
                expiry_dt="Fri, 15 Dec 2023 23:59:59 GMT",
                hiring_manager_id=150866,
                job_description="The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. \r\n\r\nThe Junior Engineershould possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.",
                job_type="PT",
                original_creation_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                role_id=15,
                role_listing_ver=0,
                role_name="Junior Engineer",
                upd_dt="Sun, 20 Aug 2023 23:20:00 GMT",
                upd_hiring_manager_id=150866
            )
        ]
        self.utA0019RoleNameQuery3 = [
            Role(
                active_status=False,
                department="ENGINEERING",
                expiry_dt="Fri, 06 Oct 2023 23:59:59 GMT",
                hiring_manager_id=151443,
                job_description="The Senior Engineer applies advanced engineering principles and techniques to troubleshoot complex engineering problems encountered within the manufacturing facility and provides expert technical advice to guide the installation and maintenance of equipment and systems. He/She is expected to lead the technical cross-collaboration with the Process Development/Manufacturing Science and Technology (PD/MSAT) department in order to identify appropriate biopharmaceuticals manufacturing equipment and optimise their functionalities. The Senior Engineer leads manufacturing equipment and systems innovation projects by guiding feasibility assessments and tests on new technologies. He is expected to review and approve solutions and initiatives to optimise machine availability while managing energy and utility use. He sets parameters for equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. The Principal/Engineer must ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview.\r\n\r\nThe Engineering and Maintenance Principal/Engineer carries the responsibility of the in-house technical expert. He should possess a deep passion for analysing and resolving multifaceted engineering problems and be able to apply advanced critical and analytical thinking skills to deal with immediate situations. He should have a developmental and amiable approach in his interactions working as part of a team while guiding and mentoring others. He must also be able to communicate engineering concepts in a manner that will be understood by others within and beyond the team.",
                job_type="FT",
                original_creation_dt="Sun, 27 Aug 2023 14:50:00 GMT",
                role_id=20,
                role_listing_ver=0,
                role_name="Senior Engineer",
                upd_dt="Sun, 27 Aug 2023 14:50:00 GMT",
                upd_hiring_manager_id=151443
            )
        ]
        self.utA0019RoleNameQuery4 = [
            Role(
                active_status=True,
                department="SOLUTIONING",
                expiry_dt="Wed, 13 Dec 2023 23:59:59 GMT",
                hiring_manager_id=140894,
                job_description="The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                job_type="PT",
                original_creation_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                role_id=22,
                role_listing_ver=0,
                role_name="Support Engineer",
                upd_dt="Wed, 15 Feb 2023 21:55:00 GMT",
                upd_hiring_manager_id=140894
            )
        ]


        ####################################################
        # UNIT TEST - STAFF OBJECTS (PASSED VIA REQUESTS)
        ####################################################

        self.utA001HiringMgr140944 = Staff(
            country="Singapore",
            dept="Sales",
            email="Yee.Lim.1@allinone.com.sg",
            staff_fname="Yee",
            staff_id=140944,
            staff_lname="Lim"
        )

        self.utA001UpdMgr140944 = Staff(
            country="Singapore",
            dept="Sales",
            email="Yee.Lim.1@allinone.com.sg",
            staff_fname="Yee",
            staff_id=140944,
            staff_lname="Lim"
        )

        self.utA001HiringMgr160318 = Staff(
            country="Singapore",
            dept="HR",
            email="Narong.Chua.2@allinone.com.sg",
            staff_fname="Narong",
            staff_id=160318,
            staff_lname="Chua"
        )

        self.utA001UpdMgr160318 = Staff(
            country="Singapore",
            dept="HR",
            email="Narong.Chua.2@allinone.com.sg",
            staff_fname="Narong",
            staff_id=160318,
            staff_lname="Chua"
        )

        self.utA002140001 = Staff(
            country="Singapore",
            dept="Sales",
            email="Derek.Tan.1@allinone.com.sg",
            staff_fname="Derek",
            staff_id=140001,
            staff_lname="Tan"
        )

        self.utA002150866 = Staff(
            country="Singapore",
            dept="Engineering",
            email="Henry.Chan@allinone.com.sg",
            staff_fname="Henry",
            staff_id=150866,
            staff_lname="Chan"
        )

        self.utA002151443 = Staff(
            country="Hong Kong",
            dept="Engineering",
            email="Anil.Kumar@allinone.com.hk",
            staff_fname="Anil",
            staff_id=151443,
            staff_lname="Kumar"
        )

        self.utA002140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA004160318 = Staff(
            country="Singapore",
            dept="HR",
            email="Narong.Chua.2@allinone.com.sg",
            staff_fname="Narong",
            staff_id=160318,
            staff_lname="Chua"
        )

        self.utA004190059 = Staff(
            country="Singapore",
            dept="Solutioning",
            email="Phuc.Le@allinone.com.sg",
            staff_fname="Phuc",
            staff_id=190059,
            staff_lname="Le"
        )

        self.utA006160318 = Staff(
            country="Singapore",
            dept="HR",
            email="Narong.Chua.2@allinone.com.sg",
            staff_fname="Narong",
            staff_id=160318,
            staff_lname="Chua"
        )

        self.utA006190059 = Staff(
            country="Singapore",
            dept="Solutioning",
            email="Phuc.Le@allinone.com.sg",
            staff_fname="Phuc",
            staff_id=190059,
            staff_lname="Le"
        )

        self.utA006140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA007171018 = Staff(
            country="Singapore",
            dept="Finance",
            email="Phuong.Truong.3@allinone.com.sg",
            staff_fname="Phuong",
            staff_id=171018,
            staff_lname="Truong"
        )

        self.utA007140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA009140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA011140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA013171018 = Staff(
            country="Singapore",
            dept="Finance",
            email="Phuong.Truong.3@allinone.com.sg",
            staff_fname="Phuong",
            staff_id=171018,
            staff_lname="Truong"
        )

        self.utA015171018 = Staff(
            country="Singapore",
            dept="Finance",
            email="Phuong.Truong.3@allinone.com.sg",
            staff_fname="Phuong",
            staff_id=171018,
            staff_lname="Truong"
        )

        self.utA015140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )

        self.utA017140001 = Staff(
            country="Singapore",
            dept="Sales",
            email="Derek.Tan.1@allinone.com.sg",
            staff_fname="Derek",
            staff_id=140001,
            staff_lname="Tan"
        )

        self.utA017150866 = Staff(
            country="Singapore",
            dept="Engineering",
            email="Henry.Chan@allinone.com.sg",
            staff_fname="Henry",
            staff_id=150866,
            staff_lname="Chan"
        )

        self.utA018160318 = Staff(
            country="Singapore",
            dept="HR",
            email="Narong.Chua.2@allinone.com.sg",
            staff_fname="Narong",
            staff_id=160318,
            staff_lname="Chua"
        )

        self.utA018190059 = Staff(
            country="Singapore",
            dept="Solutioning",
            email="Phuc.Le@allinone.com.sg",
            staff_fname="Phuc",
            staff_id=190059,
            staff_lname="Le"
        )

        self.utA019140001 = Staff(
            country="Singapore",
            dept="Sales",
            email="Derek.Tan.1@allinone.com.sg",
            staff_fname="Derek",
            staff_id=140001,
            staff_lname="Tan"
        )

        self.utA019150866 = Staff(
            country="Singapore",
            dept="Engineering",
            email="Henry.Chan@allinone.com.sg",
            staff_fname="Henry",
            staff_id=150866,
            staff_lname="Chan"
        )

        self.utA019151443 = Staff(
            country="Hong Kong",
            dept="Engineering",
            email="Anil.Kumar@allinone.com.hk",
            staff_fname="Anil",
            staff_id=151443,
            staff_lname="Kumar"
        )

        self.utA019140894 = Staff(
            country="Singapore",
            dept="Sales",
            email="Rahim.Khalid.1@allinone.com.sg",
            staff_fname="Rahim",
            staff_id=140894,
            staff_lname="Khalid"
        )


        #########################
        # UNIT TEST - EXPECTED RESPONSES
        ####################################################

        self.utA001Exp = [
            {
                "active_status": True,
                "department": "SALES",
                "expiry_dt": "Wed, 15 Nov 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Yee.Lim.1@allinone.com.sg",
                    "staff_fname": "Yee",
                    "staff_id": 140944,
                    "staff_lname": "Lim"
                },
                "hiring_manager_id": 140944,
                "job_description": "The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analysing, and summarising sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organisation's products and services, as well as trends, developments and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused and persistent individual, who takes rejection as a personal challenge to succeed when given opportunity. He appreciates the value of long lasting relationships and prioritises efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily.",
                "job_type": "FT",
                "original_creation_dt": "Wed, 15 Feb 2023 08:30:00 GMT",
                "role_id": 1,
                "role_listing_ver": 0,
                "role_name": "Account Manager",
                "upd_dt": "Wed, 15 Feb 2023 08:30:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Yee.Lim.1@allinone.com.sg",
                    "staff_fname": "Yee",
                    "staff_id": 140944,
                    "staff_lname": "Lim"
                },
                "upd_hiring_manager_id": 140944
            },
            {
                "active_status": True,
                "department": "HR",
                "expiry_dt": "Fri, 17 Nov 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "hiring_manager_id": 160318,
                "job_description": "Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                "job_type": "FT",
                "original_creation_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "role_id": 2,
                "role_listing_ver": 0,
                "role_name": "Admin Executive",
                "upd_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "upd_hiring_manager_id": 160318
            },
        ]

        self.utA002Exp = [
            {
                "active_status": True,
                "department": "ENGINEERING",
                "expiry_dt": "Thu, 28 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Derek.Tan.1@allinone.com.sg",
                    "staff_fname": "Derek",
                    "staff_id": 140001,
                    "staff_lname": "Tan"
                },
                "hiring_manager_id": 140001,
                "job_description": "The Engineering Director is responsible for spearheading the strategic planning, design and implementation of complex engineering solutions to meet customers requirements. He/She drives direction and strategy for the development and execution of engineering projects, and ensures alignment to the organisational strategy, vision and mission. He formulates strategies and frameworks to drive workplace health, safety, risk and environmental management in accordance with local and international regulations. He develops the organisations technology roadmap and drives continuous improvement strategies. In addition, he leverages his deep technical expertise and industry experience to develop technical capabilities and domain expertise for the organisation. He is a professional engineer, specialising in mechanical, electrical, control and instrumentation, civil, structural or geotechnical engineering disciplines.\r\n\r\nHe is the organisations technical expert who advises senior management and business partners on complex engineering matters. He maintains and builds strong links with the external engineering community and establishes best practises in the implementation of engineering standards and design. He is a strategic and creative thinker, demonstrates exceptional leadership and problem-solving skills, and establishes strategic partnerships.",
                "job_type": "FT",
                "original_creation_dt": "Thu, 27 Jul 2023 09:10:00 GMT",
                "role_id": 7,
                "role_listing_ver": 0,
                "role_name": "Engineering Director",
                "upd_dt": "Thu, 27 Jul 2023 09:10:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Derek.Tan.1@allinone.com.sg",
                    "staff_fname": "Derek",
                    "staff_id": 140001,
                    "staff_lname": "Tan"
                },
                "upd_hiring_manager_id": 140001
            },
            {
                "active_status": True,
                "department": "ENGINEERING",
                "expiry_dt": "Fri, 15 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Engineering",
                    "email": "Henry.Chan@allinone.com.sg",
                    "staff_fname": "Henry",
                    "staff_id": 150866,
                    "staff_lname": "Chan"
                },
                "hiring_manager_id": 150866,
                "job_description": "The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. \r\n\r\nThe Junior Engineershould possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.",
                "job_type": "PT",
                "original_creation_dt": "Sun, 20 Aug 2023 23:20:00 GMT",
                "role_id": 15,
                "role_listing_ver": 0,
                "role_name": "Junior Engineer",
                "upd_dt": "Sun, 20 Aug 2023 23:20:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Engineering",
                    "email": "Henry.Chan@allinone.com.sg",
                    "staff_fname": "Henry",
                    "staff_id": 150866,
                    "staff_lname": "Chan"
                },
                "upd_hiring_manager_id": 150866
            },
            {
                "active_status": False,
                "department": "ENGINEERING",
                "expiry_dt": "Fri, 06 Oct 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Hong Kong",
                    "dept": "Engineering",
                    "email": "Anil.Kumar@allinone.com.hk",
                    "staff_fname": "Anil",
                    "staff_id": 151443,
                    "staff_lname": "Kumar"
                },
                "hiring_manager_id": 151443,
                "job_description": "The Senior Engineer applies advanced engineering principles and techniques to troubleshoot complex engineering problems encountered within the manufacturing facility and provides expert technical advice to guide the installation and maintenance of equipment and systems. He/She is expected to lead the technical cross-collaboration with the Process Development/Manufacturing Science and Technology (PD/MSAT) department in order to identify appropriate biopharmaceuticals manufacturing equipment and optimise their functionalities. The Senior Engineer leads manufacturing equipment and systems innovation projects by guiding feasibility assessments and tests on new technologies. He is expected to review and approve solutions and initiatives to optimise machine availability while managing energy and utility use. He sets parameters for equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. The Principal/Engineer must ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview.\r\n\r\nThe Engineering and Maintenance Principal/Engineer carries the responsibility of the in-house technical expert. He should possess a deep passion for analysing and resolving multifaceted engineering problems and be able to apply advanced critical and analytical thinking skills to deal with immediate situations. He should have a developmental and amiable approach in his interactions working as part of a team while guiding and mentoring others. He must also be able to communicate engineering concepts in a manner that will be understood by others within and beyond the team.",
                "job_type": "FT",
                "original_creation_dt": "Sun, 27 Aug 2023 14:50:00 GMT",
                "role_id": 20,
                "role_listing_ver": 0,
                "role_name": "Senior Engineer",
                "upd_dt": "Sun, 27 Aug 2023 14:50:00 GMT",
                "upd_hiring_manager": {
                    "country": "Hong Kong",
                    "dept": "Engineering",
                    "email": "Anil.Kumar@allinone.com.hk",
                    "staff_fname": "Anil",
                    "staff_id": 151443,
                    "staff_lname": "Kumar"
                },
                "upd_hiring_manager_id": 151443
            },
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA003Exp = {"error": "No role found with search criteria"}

        self.utA004Exp = [
            {
                "active_status": True,
                "department": "HR",
                "expiry_dt": "Fri, 17 Nov 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "hiring_manager_id": 160318,
                "job_description": "Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                "job_type": "FT",
                "original_creation_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "role_id": 2,
                "role_listing_ver": 0,
                "role_name": "Admin Executive",
                "upd_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "upd_hiring_manager_id": 160318
            },
            {
                "active_status": True,
                "department": "HR",
                "expiry_dt": "Fri, 15 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Solutioning",
                    "email": "Phuc.Le@allinone.com.sg",
                    "staff_fname": "Phuc",
                    "staff_id": 190059,
                    "staff_lname": "Le"
                },
                "hiring_manager_id": 190059,
                "job_description": "TheHR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.\r\n\r\nThe HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.",
                "job_type": "FT",
                "original_creation_dt": "Wed, 28 Jun 2023 19:40:00 GMT",
                "role_id": 11,
                "role_listing_ver": 0,
                "role_name": "HR Director",
                "upd_dt": "Wed, 28 Jun 2023 19:40:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Solutioning",
                    "email": "Phuc.Le@allinone.com.sg",
                    "staff_fname": "Phuc",
                    "staff_id": 190059,
                    "staff_lname": "Le"
                },
                "upd_hiring_manager_id": 190059
            }
        ]

        self.utA005Exp = {"error": "No role found with search criteria"}

        self.utA006Exp = [
            {
                "active_status": True,
                "department": "HR",
                "expiry_dt": "Fri, 17 Nov 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "hiring_manager_id": 160318,
                "job_description": "Admin Executive will act as the point of contact for all employees, providing administrative support and managing their queries. Main duties include managing office stock, preparing regular reports (e.g. expenses and office budgets) and organizing company records. If you have previous experience as an Office Administrator or similar administrative role, wed like to meet you. ",
                "job_type": "FT",
                "original_creation_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "role_id": 2,
                "role_listing_ver": 0,
                "role_name": "Admin Executive",
                "upd_dt": "Wed, 02 Aug 2023 14:45:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "HR",
                    "email": "Narong.Chua.2@allinone.com.sg",
                    "staff_fname": "Narong",
                    "staff_id": 160318,
                    "staff_lname": "Chua"
                },
                "upd_hiring_manager_id": 160318
            },
            {
                "active_status": True,
                "department": "HR",
                "expiry_dt": "Fri, 15 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Solutioning",
                    "email": "Phuc.Le@allinone.com.sg",
                    "staff_fname": "Phuc",
                    "staff_id": 190059,
                    "staff_lname": "Le"
                },
                "hiring_manager_id": 190059,
                "job_description": "TheHR Director is responsible for establishing the overall talent management strategies and frameworks to identify, prepare and position the right talent to drive organisational success. He/She formulates career development frameworks and programmes to provide fulfilling career opportunities to employees in the organisation. He liaises with senior business stakeholders to formulate robust succession plans for business-critical roles in the organisation, ensuring future viability and alignment with business plans and direction. He is responsible for establishing retirement and exit policies and guidelines, and evaluating the business impact of redundancy, retirement and exit decisions. He also guides and advises senior business leaders in the management and communication of sensitive talent decisions. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent management plans.\r\n\r\nThe HR Director is a forward-thinking and influential leader who is able to integrate knowledge across diverse domains to make robust decisions and address multi-faceted issues effectively. He has the desire to motivate employees and develop talent capabilities both within the team and across the organisation, and demonstrates sensitivity and diplomacy when interacting with stakeholders at various levels.",
                "job_type": "FT",
                "original_creation_dt": "Wed, 28 Jun 2023 19:40:00 GMT",
                "role_id": 11,
                "role_listing_ver": 0,
                "role_name": "HR Director",
                "upd_dt": "Wed, 28 Jun 2023 19:40:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Solutioning",
                    "email": "Phuc.Le@allinone.com.sg",
                    "staff_fname": "Phuc",
                    "staff_id": 190059,
                    "staff_lname": "Le"
                },
                "upd_hiring_manager_id": 190059
            },
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA007Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Thu, 07 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "hiring_manager_id": 171018,
                "job_description": "The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                "job_type": "FT",
                "original_creation_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "role_id": 6,
                "role_listing_ver": 0,
                "role_name": "Developer",
                "skills_matched": [
                    "System Integration"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "upd_hiring_manager_id": 171018
            },
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "skills_matched": [
                    "System Integration"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]
        
        self.utA008Exp = {"error": "No role found with search criteria"}

        self.utA009Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "skills_matched": [
                    "System Integration",
                    "Network Administration and Maintenance"
                ],
                "skills_matched_count": 2,
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA010Exp = {"error": "No role found with search criteria"}

        self.utA011Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA012Exp = {"error": "No role found with search criteria"}

        self.utA013Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Thu, 07 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "hiring_manager_id": 171018,
                "job_description": "The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                "job_type": "FT",
                "original_creation_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "role_id": 6,
                "role_listing_ver": 0,
                "role_name": "Developer",
                "skills_matched": [
                    "System Integration"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "upd_hiring_manager_id": 171018
            }
        ]

        self.utA014Exp = {"error": "No role found with search criteria"}

        self.utA015Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Thu, 07 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "hiring_manager_id": 171018,
                "job_description": "The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.",
                "job_type": "FT",
                "original_creation_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "role_id": 6,
                "role_listing_ver": 0,
                "role_name": "Developer",
                "skills_matched": [
                    "Stakeholder Management"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Sat, 10 Jun 2023 16:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Finance",
                    "email": "Phuong.Truong.3@allinone.com.sg",
                    "staff_fname": "Phuong",
                    "staff_id": 171018,
                    "staff_lname": "Truong"
                },
                "upd_hiring_manager_id": 171018
            },
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "skills_matched": [
                    "Stakeholder Management"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA016Exp = {"error": "No role found with search criteria"}

        self.utA017Exp = [
            {
                "active_status": True,
                "department": "ENGINEERING",
                "expiry_dt": "Fri, 15 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Engineering",
                    "email": "Henry.Chan@allinone.com.sg",
                    "staff_fname": "Henry",
                    "staff_id": 150866,
                    "staff_lname": "Chan"
                },
                "hiring_manager_id": 150866,
                "job_description": "The Junior Engineerapplies engineering principles and techniques to optimise the equipment and systems within the manufacturing facility. He/She provides technical guidance and direction for the installation of equipment and systems. He develops plans for the maintenance of equipment and systems, and recommends engineering solutions to troubleshoot faults. The Junior Engineerinnovates equipment and systems, and contributes to manufacturing equipment and systems improvement projects by conducting feasibility assessments and tests on new technologies. He is also expected to manage energy resources and utilities by developing solutions to optimise machine availability and energy efficiency. The Junior Engineermust ensure compliance with Standard Operating Procedures (SOPs), Health, Safety and Environment (HSE) regulations and Current Good Manufacturing Practices (CGMPs) within his purview. He develops guidelines and conducts equipment qualification and validation in line with biopharmaceuticals manufacturing regulatory requirements. \r\n\r\nThe Junior Engineershould possess an enquiring and analytical mind and have a knack for investigating issues, analysing multifaceted engineering problems and developing solutions. He must also be a strong team player who can guide and mentor others, and communicate technical advices and solutions to colleagues beyond the team.",
                "job_type": "PT",
                "original_creation_dt": "Sun, 20 Aug 2023 23:20:00 GMT",
                "role_id": 15,
                "role_listing_ver": 0,
                "role_name": "Junior Engineer",
                "upd_dt": "Sun, 20 Aug 2023 23:20:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Engineering",
                    "email": "Henry.Chan@allinone.com.sg",
                    "staff_fname": "Henry",
                    "staff_id": 150866,
                    "staff_lname": "Chan"
                },
                "upd_hiring_manager_id": 150866
            }
        ]

        self.utA018Exp = {"error": "No role found with search criteria"}

        self.utA019Exp = [
            {
                "active_status": True,
                "department": "SOLUTIONING",
                "expiry_dt": "Wed, 13 Dec 2023 23:59:59 GMT",
                "hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "hiring_manager_id": 140894,
                "job_description": "The Support Engineer undertakes complex projects related to system provisioning, installations, configurations as well as monitoring and maintenance of systems. He/She applies highly developed specialist knowledge and skills in systems administration and works toward continuous optimisation of system performance. He implements system improvements and instructs other IT staff in the resolution of most complex issues. He is required to be on standby with on-call availability with varied shifts including nights, weekends and holidays to resolve systems related incidents. He works in a team setting and is proficient in Infrastructure systems and Network related tools and techniques required by the organisation. He is also familiar with the relevant platforms on which the database is deployed on. The Support Team is able to quickly and effectively solve issues as they arise. He is able to methodically identify the cause of the issue, evaluate it and develop a solution in collaboration with the team. He is able to communicate effectively and displays high service level standards.",
                "job_type": "PT",
                "original_creation_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "role_id": 22,
                "role_listing_ver": 0,
                "role_name": "Support Engineer",
                "skills_matched": [
                    "Stakeholder Management"
                ],
                "skills_matched_count": 1,
                "upd_dt": "Wed, 15 Feb 2023 21:55:00 GMT",
                "upd_hiring_manager": {
                    "country": "Singapore",
                    "dept": "Sales",
                    "email": "Rahim.Khalid.1@allinone.com.sg",
                    "staff_fname": "Rahim",
                    "staff_id": 140894,
                    "staff_lname": "Khalid"
                },
                "upd_hiring_manager_id": 140894
            }
        ]

        self.utA020Exp = {"error": "No role found with search criteria"}

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_001(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA001RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA001HiringMgr140944,
            self.utA001UpdMgr140944,
            self.utA001HiringMgr160318,
            self.utA001UpdMgr160318
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.json_blank)

        self.assertEqual(res.json, self.utA001Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_002(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA002RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA002140001, self.utA002140001,
            self.utA002150866, self.utA002150866,
            self.utA002151443, self.utA002151443,
            self.utA002140894, self.utA002140894
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA002json)

        self.assertEqual(res.json, self.utA002Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_003(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA003RoleNameQuery]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA003json)

        self.assertEqual(res.json, self.utA003Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_004(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA004RoleNameQuery]

        # Set the responses for the mock requests.get calls
        mock_requests_get.side_effect = [
            self.utA004160318, self.utA004160318,
            self.utA004190059, self.utA004190059
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA004json)

        self.assertEqual(res.json, self.utA004Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_005(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA005RoleNameQuery]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA005json)

        self.assertEqual(res.json, self.utA005Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_006(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA006RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA006160318, self.utA006160318,
            self.utA006190059, self.utA006190059,
            self.utA006140894, self.utA006140894,
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA006json)

        self.assertEqual(res.json, self.utA006Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_007(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA007SkillsQuery, self.utA007RoleNameQuery1, self.utA007RoleNameQuery2]

        mock_requests_get.side_effect = [
            self.utA007171018, self.utA007171018,
            self.utA007140894, self.utA007140894,
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA007json)

        self.assertEqual(res.json, self.utA007Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_008(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA008SkillsQuery]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA008json)

        self.assertEqual(res.json, self.utA008Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_009(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA009SkillsQuery, self.utA009RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA009140894, self.utA009140894,
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA009json)

        self.assertEqual(res.json, self.utA009Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_010(self, mock_requests_get, mock_query):
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA010SkillsQuery]
        
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA010json)

        self.assertEqual(res.json, self.utA010Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_011(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect  = [self.utA011RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA011140894, self.utA011140894,
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA011json)
        
        self.assertEqual(res.json, self.utA011Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_012(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA012RoleNameQuery]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA012json)
        
        self.assertEqual(res.json, self.utA012Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_013(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA013SkillsQuery, self.utA013RoleNameQuery1, self.utA013RoleNameQuery2]

        mock_requests_get.side_effect = [
            self.utA013171018, self.utA013171018,
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA013json)
        
        self.assertEqual(res.json, self.utA013Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_014(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA014SkillsQuery, self.utA014RoleNameQuery1, self.utA014RoleNameQuery2]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA014json)
        
        self.assertEqual(res.json, self.utA014Exp)
    
    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_015(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA015SkillsQuery, self.utA015RoleNameQuery1, self.utA015RoleNameQuery2]

        mock_requests_get.side_effect = [
            self.utA015171018, self.utA015171018,
            self.utA015140894, self.utA015140894,
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA015json)
        
        self.assertEqual(res.json, self.utA015Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_016(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA016SkillsQuery, self.utA016RoleNameQuery1, self.utA016RoleNameQuery2]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA016json)
        
        self.assertEqual(res.json, self.utA016Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_017(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA017RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA017140001, self.utA017140001,
            self.utA017150866, self.utA017150866,
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA017json)
        
        self.assertEqual(res.json, self.utA017Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_018(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA018RoleNameQuery]

        mock_requests_get.side_effect = [
            self.utA018160318, self.utA018160318,
            self.utA018190059, self.utA018190059,
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA018json)
        
        self.assertEqual(res.json, self.utA018Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_019(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA019SkillsQuery, self.utA0019RoleNameQuery1, self.utA0019RoleNameQuery2, self.utA0019RoleNameQuery3, self.utA0019RoleNameQuery4]

        mock_requests_get.side_effect = [
            self.utA019140001, self.utA019140001,
            self.utA019150866, self.utA019150866,
            self.utA019151443, self.utA019151443,
            self.utA019140894, self.utA019140894
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA019json)
        
        self.assertEqual(res.json, self.utA019Exp)

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_020(self, mock_requests_get, mock_query):
 
        mock_query.return_value = Mock()
        mock_query.return_value.join.return_value = Mock()
        mock_all = mock_query.return_value.join.return_value.filter.return_value.all
        mock_all.side_effect = [self.utA019SkillsQuery, self.utA0019RoleNameQuery1, self.utA0019RoleNameQuery2, self.utA0019RoleNameQuery3, self.utA0019RoleNameQuery4]

        mock_requests_get.side_effect = [
            self.utA019140001, self.utA019140001,
            self.utA019150866, self.utA019150866,
            self.utA019151443, self.utA019151443,
            self.utA019140894, self.utA019140894
        ]

        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA020json)
        
        self.assertEqual(res.json, self.utA020Exp)

class UT_B_UpdateRole(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

        ####################################################
        # UNIT TEST - POST JSON PASSED TO API
        ####################################################
        self.utB001json = {
            "active_status": True,
            "department": "Engineering",
            "expiry_dt": "Sat, 14 Oct 2023 23:59:59 GMT",
            "hiring_manager_id": 140001,
            "job_description": "Develop Machine learning Models",
            "job_type": "FT",
            "original_creation_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
            "role_name": "Data Engineer",
            "upd_hiring_manager_id": 140001,
            "role_listing_skills": [
            ["communication", 1],
            ["coding", 3]
            ],
            "orig_role_listing": {
                    "active_status": True,
                    "department": "Engineering",
                    "expiry_dt": "Sat, 14 Oct 2023 23:59:59 GMT",
                    "hiring_manager_id": 140001,
                    "job_description": "Develop software applications",
                    "job_type": "Full-time",
                    "original_creation_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
                    "role_id": 27,
                    "role_listing_ver": 0,
                    "role_name": "Software Engineer",
                    "upd_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
                    "upd_hiring_manager_id": 140001
            }
        }




        self.utB002json = {
            "active_status": True,
            "department": "Engineering",
            "expiry_dt": "Sat, 14 Oct 2023 23:59:59 GMT",
            "hiring_manager_id": 140001,
            "job_description": "Develop Machine learning Models",
            "job_type": "FT",
            "original_creation_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
            "role_name": "Data Engineer",
            "upd_hiring_manager_id": 140001,
            "role_listing_skills": [
            ["communication", 1],
            ["coding", 3]
            ],
        }

        self.utB003json = {
            "active_status": True,
            "department": "Engineering",
            "expiry_dt": "Sat, 14 Oct 2023 23:59:59 GMT",
            "hiring_manager_id": 140001,
            "job_description": "Develop Machine learning Models",
            "job_type": "FT",
            "original_creation_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
            "role_name": "Data Engineer",
            "upd_hiring_manager_id": 140001,
            "orig_role_listing": {
                    "active_status": True,
                    "department": "Engineering",
                    "expiry_dt": "Sat, 14 Oct 2023 23:59:59 GMT",
                    "hiring_manager_id": 140001,
                    "job_description": "Develop software applications",
                    "job_type": "Full-time",
                    "original_creation_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
                    "role_id": 27,
                    "role_listing_ver": 0,
                    "role_name": "Software Engineer",
                    "upd_dt": "Mon, 23 Oct 2023 18:45:39 GMT",
                    "upd_hiring_manager_id": 140001
            }
        }

        #########################
        # UNIT TEST - EXPECTED RESPONSES
        ####################################################

        self.utB001resActive = True
        self.utB001resDept = "Engineering"
        self.utB001resExpDt = "Sat, 14 Oct 2023 23:59:59 GMT"
        self.utB001resHiringMgrId = 140001
        self.utB001resJobDesc = "Develop Machine learning Models"
        self.utB001resJobType = "FT"
        self.utB001resOrigCreateDt = "Mon, 23 Oct 2023 18:45:39 GMT"
        self.utB001resRoleName = "Data Engineer"
        self.utB001resUpdHiringMgrId = 140001
        self.utB001resRoleListingSkills = [
                {
                    "role_id": 27,
                    "role_listing_ver": 1,
                    "skill_name": "communication",
                    "skills_proficiency": 1
                },
                {
                    "role_id": 27,
                    "role_listing_ver": 1,
                    "skill_name": "coding",
                    "skills_proficiency": 3
                }
            ]
        self.utB001resRoleListingVer = 1
        self.utB001resRoleID = 27

        self.utB002Exp = {"error": "orig_role_listing key not found in json object"}

        self.utB003Exp = {"error":"Passed JSON data invalid or missing values, error: \'role_listing_skills\'"}


    def test_UT_B_001(self):
 
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/updateRole", json=self.utB001json)

        self.assertEqual(res.json["active_status"], self.utB001resActive)
        self.assertEqual(res.json["department"], self.utB001resDept)
        self.assertEqual(res.json["expiry_dt"], self.utB001resExpDt)
        self.assertEqual(res.json["hiring_manager_id"], self.utB001resHiringMgrId)
        self.assertEqual(res.json["job_description"], self.utB001resJobDesc)
        self.assertEqual(res.json["job_type"], self.utB001resJobType)
        self.assertEqual(res.json["original_creation_dt"], self.utB001resOrigCreateDt)
        self.assertEqual(res.json["role_id"], self.utB001resRoleID)
        self.assertEqual(res.json["role_listing_skills"], self.utB001resRoleListingSkills)
        self.assertEqual(res.json["role_listing_ver"], self.utB001resRoleListingVer)
        self.assertEqual(res.json["role_name"], self.utB001resRoleName)
        self.assertEqual(res.json["upd_hiring_manager_id"], self.utB001resUpdHiringMgrId)

    def test_UT_B_002(self):
        
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/updateRole", json=self.utB002json)
                
        self.assertEqual(res.json, self.utB002Exp)

    def test_UT_B_003(self):
        
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/updateRole", json=self.utB003json)
                
        self.assertEqual(res.json, self.utB003Exp)


if __name__ == "__main__":
    unittest.main()

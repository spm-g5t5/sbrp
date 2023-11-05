import unittest
from unittest.mock import Mock, patch
from app import *
from models import *
import requests
import json


class CISetupTest(unittest.TestCase):
    def test_hello(self):

        res = hello()
        self.assertEqual(res, "Welcome to SBRP")


class UT_A_FilterRoleStaff(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.json_blank = {}

        self.utA002json = {"search": "Engineer"}

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

    @patch('app.db.session.query')
    @patch('requests.get')
    def test_UT_A_001(self, mock_requests_get, mock_query):
        mock_subquery = Mock()
        mock_subquery.c.role_id = Mock()
        mock_subquery.c.max_ver = Mock()

        # Mock the main query
        # Configure the mock subquery
        mock_query.return_value.join.return_value.filter.return_value.all.return_value = self.utA001RoleNameQuery

        # Set the responses for the mock requests.get calls
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
        mock_subquery = Mock()
        mock_subquery.c.role_id = Mock()
        mock_subquery.c.max_ver = Mock()

        # Mock the main query
        # Configure the mock subquery
        mock_query.return_value.join.return_value.filter.return_value.all.return_value = self.utA002RoleNameQuery

        # Set the responses for the mock requests.get calls
        mock_requests_get.side_effect = [
            self.utA002140001, self.utA002140001,
            self.utA002150866, self.utA002150866,
            self.utA002151443, self.utA002151443,
            self.utA002140894, self.utA002140894
        ]
        res = self.app.post(
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.utA002json)

        self.assertEqual(res.json, self.utA002Exp)


if __name__ == "__main__":
    unittest.main()

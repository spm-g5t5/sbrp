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
        self.jsonssss = {}

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

        # self.app.testing = True

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
            "http://127.0.0.1:5000/API/v1/searchRole", json=self.jsonssss)

        self.assertEqual(res.json, self.utA001Exp)


if __name__ == "__main__":
    unittest.main()

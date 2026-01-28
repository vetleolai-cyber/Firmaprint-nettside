#!/usr/bin/env python3

import requests
import sys
import json
from datetime import datetime
import uuid

class FirmaprintAPITester:
    def __init__(self, base_url="https://norsk-profiltoy.preview.emergentagent.com/api"):
        self.base_url = base_url
        self.token = None
        self.session_id = str(uuid.uuid4())
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        test_headers = {'Content-Type': 'application/json'}
        
        if headers:
            test_headers.update(headers)
        if self.token:
            test_headers['Authorization'] = f'Bearer {self.token}'

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=test_headers, timeout=30)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=test_headers, timeout=30)
            elif method == 'DELETE':
                response = requests.delete(url, headers=test_headers, timeout=30)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    return success, response.json() if response.content else {}
                except:
                    return success, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}...")
                self.failed_tests.append({
                    'name': name,
                    'expected': expected_status,
                    'actual': response.status_code,
                    'response': response.text[:200]
                })
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append({
                'name': name,
                'error': str(e)
            })
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root API", "GET", "", 200)

    def test_seed_database(self):
        """Seed database with products"""
        return self.run_test("Seed Database", "POST", "seed", 200)

    def test_get_categories(self):
        """Test get categories"""
        return self.run_test("Get Categories", "GET", "categories", 200)

    def test_get_products(self):
        """Test get all products"""
        return self.run_test("Get Products", "GET", "products", 200)

    def test_get_featured_products(self):
        """Test get featured products"""
        return self.run_test("Get Featured Products", "GET", "products?featured=true&limit=4", 200)

    def test_get_product_by_slug(self):
        """Test get specific product by slug"""
        return self.run_test("Get Product by Slug", "GET", "products/premium-t-skjorte", 200)

    def test_user_registration(self):
        """Test user registration"""
        test_user_data = {
            "email": f"test_{datetime.now().strftime('%H%M%S')}@test.no",
            "password": "TestPass123!",
            "name": "Test Bruker",
            "company_name": "Test AS",
            "is_business": True
        }
        
        success, response = self.run_test("User Registration", "POST", "auth/register", 200, test_user_data)
        if success and 'access_token' in response:
            self.token = response['access_token']
            print(f"   Token obtained: {self.token[:20]}...")
            return True, response
        return False, {}

    def test_user_login(self):
        """Test user login with existing user"""
        # First register a user
        test_email = f"login_test_{datetime.now().strftime('%H%M%S')}@test.no"
        register_data = {
            "email": test_email,
            "password": "TestPass123!",
            "name": "Login Test User"
        }
        
        # Register user
        reg_success, _ = self.run_test("Register for Login Test", "POST", "auth/register", 200, register_data)
        if not reg_success:
            return False, {}
        
        # Now test login
        login_data = {
            "email": test_email,
            "password": "TestPass123!"
        }
        
        success, response = self.run_test("User Login", "POST", "auth/login", 200, login_data)
        if success and 'access_token' in response:
            self.token = response['access_token']
            return True, response
        return False, {}

    def test_get_user_profile(self):
        """Test get current user profile"""
        if not self.token:
            print("⚠️  Skipping user profile test - no token available")
            return False, {}
        return self.run_test("Get User Profile", "GET", "auth/me", 200)

    def test_cart_operations(self):
        """Test cart operations"""
        # Get empty cart
        success, cart = self.run_test("Get Empty Cart", "GET", f"cart/{self.session_id}", 200)
        if not success:
            return False, {}

        # Add item to cart
        add_item_data = {
            "product_id": "test-product-id",  # This will fail but we test the endpoint
            "variant_color": "Sort",
            "size": "M",
            "quantity": 2
        }
        
        # This should return 404 since product doesn't exist, but tests the endpoint
        self.run_test("Add to Cart (Expected 404)", "POST", f"cart/{self.session_id}/add", 404, add_item_data)
        
        return True, {}

    def test_contact_form(self):
        """Test contact form submission"""
        contact_data = {
            "name": "Test Kontakt",
            "email": "test@test.no",
            "phone": "12345678",
            "subject": "Test melding",
            "message": "Dette er en test melding fra automatisert testing."
        }
        
        return self.run_test("Contact Form", "POST", "contact", 200, contact_data)

    def test_quote_request(self):
        """Test quote request submission"""
        quote_data = {
            "company_name": "Test Bedrift AS",
            "contact_name": "Test Kontakt",
            "email": "test@testbedrift.no",
            "phone": "87654321",
            "product_types": ["T-skjorter", "Hoodies"],
            "estimated_quantity": "50-100",
            "message": "Vi trenger profilklær til vårt team."
        }
        
        return self.run_test("Quote Request", "POST", "quotes", 200, quote_data)

    def test_logo_upload(self):
        """Test logo upload endpoint"""
        # We'll test with a simple text file to check the endpoint
        # In real scenario, this would be an image file
        print("\n🔍 Testing Logo Upload...")
        print("   Note: Testing endpoint availability, not actual file upload")
        
        # Test without file (should fail)
        try:
            url = f"{self.base_url}/upload/logo"
            response = requests.post(url, timeout=30)
            if response.status_code == 422:  # Unprocessable Entity - missing file
                print("✅ Logo upload endpoint is accessible (422 expected for missing file)")
                self.tests_passed += 1
            else:
                print(f"❌ Unexpected status code: {response.status_code}")
                self.failed_tests.append({
                    'name': 'Logo Upload Endpoint',
                    'expected': 422,
                    'actual': response.status_code
                })
        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append({
                'name': 'Logo Upload Endpoint',
                'error': str(e)
            })
        
        self.tests_run += 1
        return True, {}

    def test_pricing_calculation(self):
        """Test pricing calculation"""
        return self.run_test(
            "Pricing Calculation", 
            "POST", 
            "pricing/calculate?print_method=print&width_cm=10&height_cm=8&quantity=25&complexity=normal", 
            200
        )

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting Firmaprint API Tests")
        print("=" * 50)
        
        # Test basic endpoints
        self.test_root_endpoint()
        self.test_seed_database()
        self.test_get_categories()
        self.test_get_products()
        self.test_get_featured_products()
        self.test_get_product_by_slug()
        
        # Test authentication
        self.test_user_registration()
        self.test_user_login()
        self.test_get_user_profile()
        
        # Test cart operations
        self.test_cart_operations()
        
        # Test forms
        self.test_contact_form()
        self.test_quote_request()
        
        # Test file upload
        self.test_logo_upload()
        
        # Test pricing
        self.test_pricing_calculation()
        
        # Print results
        print("\n" + "=" * 50)
        print(f"📊 Test Results: {self.tests_passed}/{self.tests_run} passed")
        
        if self.failed_tests:
            print("\n❌ Failed Tests:")
            for test in self.failed_tests:
                print(f"   - {test['name']}: {test.get('error', f\"Expected {test.get('expected')}, got {test.get('actual')}\")}")
        
        success_rate = (self.tests_passed / self.tests_run) * 100 if self.tests_run > 0 else 0
        print(f"\n📈 Success Rate: {success_rate:.1f}%")
        
        return self.tests_passed == self.tests_run

def main():
    tester = FirmaprintAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
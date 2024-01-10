# from playwright.async_api import async_playwright, expect
# import jwt
# import datetime
# import os
# import pytest


# async def generate_token(secret_key):
#     return jwt.encode(
#         {"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
#         secret_key,
#         algorithm="HS256",
#     )


# SECRET_KEY = os.environ.get("SECRET_KEY") or "this is a secret"


# @pytest.mark.asyncio
# async def test_browser_launch():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         context = await browser.new_context()
#         page = await context.new_page()
#         await page.goto("https://example.com")
#         await browser.close()


# # @pytest.mark.asyncio
# # async def test_success_page():
# #     token = await generate_token(SECRET_KEY)
# #     async with async_playwright() as p:
# #         browser = await p.chromium.launch()
# #         context = await browser.new_context()

# #         await context.add_cookies(
# #             [{"name": "token", "value": token, "domain": "localhost", "path": "/"}]
# #         )

# #         page = await context.new_page()
# #         test_web_address = "localhost:5000"
# #         await page.goto(f"http://{test_web_address}/success")

# #         await expect(page.locator("h1")).to_have_text("Registration Successful!")

# #         await browser.close()

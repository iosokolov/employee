from aiohttp import web

import endpoints

app = web.Application()

app.add_routes([web.get('/employee-structure', endpoints.get_employee_structure)])


if __name__ == '__main__':
    web.run_app(app, port=8011)

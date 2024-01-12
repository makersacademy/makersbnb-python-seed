from lib.Dashboard import Requests

class DashboardRepository:
    def __init__(self,connection):
        self._connection = connection

    def list_req(self, user_id):
        rows = self._connection.execute('SELECT * FROM requests JOIN Spaces ON requests.space_id = Spaces.id WHERE req_id = %s;', [user_id])
        return_data = []
        for row in rows:
            data = Requests(row['req_id'],row['space_id'],row['date_req'],row['stat'], row['title'], row['price'])
            return_data.insert(0,data)
        return return_data
    
    def list_approvals(self, user_id):
        rows = self._connection.execute("SELECT * FROM requests JOIN spaces ON requests.space_id = spaces.id WHERE NOT req_id = %s AND spaces.user_id = %s AND stat = 'Pending';", [user_id, user_id])
        return_data = []
        for row in rows:
            data = Requests(row['req_id'],row['space_id'],row['date_req'],row['stat'], row['title'], row['price'])
            return_data.insert(0,data)
        return return_data

    def approve(self, req_id, space_id, date_req):
        self._connection.execute("UPDATE requests SET stat = 'Approved' WHERE space_id = %s AND req_id = %s AND date_req = %s;", [space_id, req_id, date_req])
        self._connection.execute("UPDATE requests SET stat = 'Declined' WHERE space_id = %s AND date_req = %s AND NOT req_id = %s;", [space_id, date_req, req_id])

    def decline(self, req_id, space_id, date_req):
        self._connection.execute("UPDATE requests SET stat = 'Declined' WHERE space_id = %s AND req_id = %s AND date_req = %s;", [space_id, req_id, date_req])


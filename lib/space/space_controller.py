from flask import Flask, request, render_template
from lib.space.space import Space
from lib.space.space_repository import SpaceRepository


class SpaceController:
    def __init__(self, space_repository, date_repository):
        self.space_repository = space_repository
        self.date_repository = date_repository

    def list_all(self):
        rows = self.space_repository.all()
        spaces = [
            Space(
                row["name"],
                row["description"],
                row["ownerid"],
                row["startdate"],
                row["enddate"],
            )
            for row in rows
        ]

        return spaces

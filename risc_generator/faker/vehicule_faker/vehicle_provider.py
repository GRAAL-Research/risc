"""
The code below was copied from the Faker Vehicle project, and has been modified for the purpose of this package.

COPYRIGHT

All contributions from the https://github.com/kennethwsmith/faker_vehicle authors.
Copyright (c) 2020 - January 16 2023
All rights reserved.

Each contributor holds copyright over their respective contributions. The project versioning (Git)
records all such contribution source information.

LICENSE

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Modification are:
 - removal of machine
 - removal of Category
"""

from random import choice

from faker.providers import BaseProvider

from .vehicle_dict import vehicles


class VehicleProvider(BaseProvider):
    """
    A Provider for vehicle related test data.

    >>> from faker import Faker
    >>> from faker_vehicle import VehicleProvider
    >>> fake = Faker()
    >>> fake.add_provider(VehicleProvider)
    """

    def vehicle_object(self):
        """
        Returns a random vehicle dict example:
        {"Year": 2008, "Make": "Jeep", "Model": "Wrangler", "Electric Vehicle": False}
        """
        veh = choice(vehicles)
        return veh

    def vehicle_year_make_model(self):
        """Returns Year Make Model example: 1997 Nissan 240SX"""
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def vehicle_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2017 GMC Sierra 1500 Double Cab (Pickup)
        """
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def vehicle_make_model(self):
        """Returns Make Model example: Audi Q7"""
        veh = self.vehicle_object()
        make = veh.get('Make')
        model = veh.get('Model')
        return make + ' ' + model

    def vehicle_make(self):
        """Returns Make example: Lincoln"""
        veh = self.vehicle_object()
        return veh.get('Make')

    def vehicle_year(self):
        """Returns Year example: 1999"""
        veh = self.vehicle_object()
        return str(veh.get('Year'))

    def vehicle_model(self):
        """Returns Model example: Frontier King Cab"""
        veh = self.vehicle_object()
        return veh.get('Model')

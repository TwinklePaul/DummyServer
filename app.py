from flask import Flask, request
from mock_suppliers import *
from mock_chargers import *
from mock_regions import *


app = Flask(__name__)


@app.route('/')
def find_supplier(filter):
    '''
        filter of following format:
        {
            id: String,
            name: String,
            region: String,
        }
    '''
    return {
        'supplier': supplier_active_01,
        'supplier_status': supplier_status_sa01,
        'supplier_in_region': supplier_in_region_SA01R01,
        'contact_person': contact_person_sa011,
    }


@app.route('/')
def find_suppliers(filter):
    '''
        filter of following format:
        {
            region: String,
            status: 'ACTIVE',
        }
    '''
    return [{
        'supplier': supplier_active_01,
        'supplier_status': supplier_status_sa01,
        'supplier_in_region': supplier_in_region_SA01R01,
        'contact_person': contact_person_sa011,
    },
        {
        'supplier': supplier_active_02,
        'supplier_status': supplier_status_sa02,
        'supplier_in_region': supplier_in_region_SA02R01,
        'contact_person': contact_person_sa021,
    }]


@app.route('/')
def find_all_suppliers(filter):
    '''
        filter of following format:
        {
            region: String,
        }
    '''
    return [{
        'supplier': supplier_active_01,
        'supplier_status': supplier_status_sa01,
        'supplier_in_region': supplier_in_region_SA01R01,
        'contact_person': contact_person_sa011,
    },
        {
        'supplier': supplier_active_02,
        'supplier_status': supplier_status_sa02,
        'supplier_in_region': supplier_in_region_SA02R01,
        'contact_person': contact_person_sa021,
    },
        {
        'supplier': supplier_active_03,
        'supplier_status': supplier_status_sa03,
        'supplier_in_region': supplier_in_region_SA03R01,
        'contact_person': contact_person_sa031,
    },
        {
        'supplier': supplier_inactive_01,
        'supplier_status': supplier_status_sia01,
        'supplier_in_region': supplier_in_region_SIA01R01,
        'contact_person': contact_person_sia011,
    }
    ]


@app.route('/')
def find_charger(filter):
    '''
        filter of following format:
        {
            id: String,
        }
    '''
    return {
        'charger': charger_01,
        'charger_status': charger_status_C01
    }


@app.route('/')
def find_chargers(filter):
    '''
        filter of following format:
        {
            region: String,
            status: 'ACTIVE',
        }
    '''
    return [{
        'charger': charger_01,
        'charger_status': charger_status_C01
    },
        {
        'charger': charger_02,
        'charger_status': charger_status_C02
    }
    ]


@app.route('/')
def find_all_chargers(filter):
    '''
        filter of following format:
        {
            region: String,
        }
    '''
    return [{
        'charger': charger_01,
        'charger_status': charger_status_C01
    },
        {
        'charger': charger_02,
        'charger_status': charger_status_C02
    },
        {
        'charger': charger_03,
        'charger_status': charger_status_C03
    },
        {
        'charger': charger_04,
        'charger_status': charger_status_C04
    }
    ]

#####################################################################################
################################## HOME PAGE ##################################
#####################################################################################


@app.route('/', methods=['POST', 'GET'])
def find_regionwise_suppliers(filter):
    '''
        if post:
        filter of following format:
        {
            start_date: '',
            end_date: '',
        }

        if get:
            return all
    '''
    if request.method == 'POST':
        return [{
            'suppliers': [{
                'supplier_id': supplier_active_01['supplier_id'],
                'supplier_name': supplier_active_01['supplier_name'],
            },
                {
                'supplier_id': supplier_active_02['supplier_id'],
                'supplier_name': supplier_active_02['supplier_name'],
            },
                {
                'supplier_id': supplier_active_03['supplier_id'],
                'supplier_name': supplier_active_03['supplier_name'],
            }],

            'regions': [{
                'region_id': region_01['region_id'],
                'region_name': region_01['region_name'],
            },
                {
                'region_id': region_02['region_id'],
                'region_name': region_02['region_name'],
            }
            ],

            'suppliers_in_regions': [
                supplier_in_region_SA01R01,
                supplier_in_region_SA01R02,
                supplier_in_region_SA02R01,
                supplier_in_region_SA03R02
            ]
        },
        ]

    return [{
            'suppliers': [{
                'supplier_id': supplier_active_01['supplier_id'],
                'supplier_name': supplier_active_01['supplier_name'],
            },
                {
                'supplier_id': supplier_active_02['supplier_id'],
                'supplier_name': supplier_active_02['supplier_name'],
            },
                {
                'supplier_id': supplier_active_03['supplier_id'],
                'supplier_name': supplier_active_03['supplier_name'],
            },

                {
                'supplier_id': supplier_inactive_01['supplier_id'],
                'supplier_name': supplier_inactive_01['supplier_name'],
            }
            ],

            'regions': [{
                'region_id': region_01['region_id'],
                'region_name': region_01['region_name'],
            },
                {
                'region_id': region_02['region_id'],
                'region_name': region_02['region_name'],
            }
            ],

            'suppliers_in_regions': [
                supplier_in_region_SA01R01,
                supplier_in_region_SA01R02,
                supplier_in_region_SA02R01,
                supplier_in_region_SA03R02,
                supplier_in_region_SIA01R01
            ]
            }]


@app.route('/', methods=['POST', 'GET'])
def find_regionwise_chargers_and_bookings(filter):
    '''
        if post:
        filter of following format:
        {
            start_date: '',
            end_date: '',
        }

        if get:
            return all
    '''
    if request.method == 'POST':
        return [{
            'bookings': [
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'}],

            'chargers': [
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'}],

            'clusters': [
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'}],

            'regions': [
                {'region_id', 'region_name'},
                {'region_id', 'region_name'},
            ],
        }
        ]

    return [{
            'bookings': [
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'}],

            'chargers': [
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'},
                {'charger_id', 'cluster_id', 'added_on'}],

            'clusters': [
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'},
                {'cluster_id', 'region_id'}],

            'regions': [
                {'region_id', 'region_name'},
                {'region_id', 'region_name'}
            ],
            }
            ]


@app.route('/', methods=['POST', 'GET'])
def find_frequented_data(filter):
    '''
        if post:
        filter of following format:
        {
            start_date: '',
            end_date: '',
        }

        if get:
            return all
    '''
    if request.method == 'POST':
        return [{
            'bookings': [
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'}],

            'chargers': [
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'}],

            'suppliers': [
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'}],

            'clusters': [
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'}],

            'regions': [
                {'region_id', 'region_name'},
                {'region_id', 'region_name'}]
        }]

    return [{
            'bookings': [
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'},
                {'booking_id', 'charger_id', 'booking_date', 'cost'}],

            'chargers': [
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
                {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'}],

            'suppliers': [
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'},
                {'supplier_id', 'supplier_name'}],

            'clusters': [
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'},
                {'cluster_id', 'cluster_name', 'region_id'}],

            'regions': [
                {'region_id', 'region_name'},
                {'region_id', 'region_name'}]
            }]


@app.route('/', methods=['POST', 'GET'])
def find_frequented_data(filter):
    return [{
        'chargers': [
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'},
            {'charger_id', 'pin_type', 'AC/DC', 'supplier_id', 'cluster_id'}],

        'charger_status': [
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id',
                'fault_occurence_time', 'fault_recovery_time', 'downtime'},
            {'charger_id', 'current_status', 'fault_id', 'fault_occurence_time', 'fault_recovery_time', 'downtime'}],

        'faults': [
            {'fault_id', 'fault_type', 'additional_msg'},
            {'fault_id', 'fault_type', 'additional_msg'},
            {'fault_id', 'fault_type', 'additional_msg'}],

        'suppliers': [
            {'supplier_id', 'supplier_name'},
            {'supplier_id', 'supplier_name'},
            {'supplier_id', 'supplier_name'},
            {'supplier_id', 'supplier_name'}
        ]
    }]


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

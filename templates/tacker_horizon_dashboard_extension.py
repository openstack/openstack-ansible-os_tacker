DASHBOARD = 'nfv'
DISABLED = {{ tacker_horizon_dashboard_disable }}
ADD_INSTALLED_APPS = [
    'tacker_horizon',
    'tacker_horizon.openstack_dashboard.dashboards.nfv',
]


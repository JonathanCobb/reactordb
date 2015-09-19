from octopus.lib import clcsv, dataobj
import re

def weblinks(cell):
    uc = dataobj.to_unicode()
    links = []
    lines = cell.split("\n")

    for line in lines:
        bits = line.split(" http")
        link = {}
        link["text"] = uc(bits[0])
        link["url"] = u"http" + uc(bits[1])
        links.append(link)

    return links

def owner(cell):
    owners = []
    share_rx = "^(.+) \((.+)\)$"
    lines = cell.split("\n\n")

    for line in lines:
        m = re.search(share_rx, line)
        own = {}
        if m is not None:
            own["name"] = m.group(1)
            own["share"] = m.group(2)
        else:
            own["name"] = line
        owners.append(own)

    return owners

class MasterSheet(clcsv.SheetWrapper):

    HEADERS = {
        # main identifying field
        u'Reactor Name' : "reactor_name",

        # fields unique to the master sheet
        u'WNA Name' : "wna_name",
        u'Latitude' : "latitude",
        u'Longitude' : "longitude",
        u"Region" : "region",
        u"Country Area" : "country_area",
        u"Site Name" : "site_name",
        u"Site Latitude" : "site_latitude",
        u"Site Longitude" : "site_longitude",
        u"Reactor Type" : "reactor_type",
        u"Project Start" : "project_start",
        u"Website" : "website",
        u"WNA Web Links" : "wna_links",
        u"WNN Web Links" : "wnn_links",
        u"Additional Info" : "additional_info",

        # fields shared with the scraped sheet
        u"Alternate Name" : "alternate_name",
        u"Location" : "country",
        u"Status" : "status",
        u"Owner" : "owner",
        u"Operator" : "operator",
        u"Model" : "model",
        u"Process" : "process",
        u"Reference Unit Power (Net Capacity)" : "reference_unit_power_capacity_net",
        u"Thermal Capacity" : "thermal_capacity",
        u"Design Net Capacity" : "design_net_capacity",
        u"Gross Capacity" : "gross_capacity",
        u"Construction Start Date" : "construction_start",
        u"Construction Suspend Date" : "construction_suspend",
        u"Construction Restart Date" : "construction_restart",
        u"First Criticality Date" : "first_criticality",
        u"First Grid Connection" : "first_grid_connection",
        u"Commercial Operation Date" : "commercial_operation",
        u"Longterm Shutdown Date" : "longterm_shutdown",
        u"Restart Date" : "restart",
        u"Permanent Shutdown Date" : "permanent_shutdown"
    }

    COERCE = {
        "latitude" : dataobj.to_float(),
        "longitude" : dataobj.to_float(),
        "site_latitude" : dataobj.to_float(),
        "site_longitude" : dataobj.to_float(),
        "project_start" : dataobj.date_str(out_format="%Y-%m-%d"),
        "wna_links" : weblinks,
        "wnn_links" : weblinks,
        "owner" : owner,
        "reference_unit_power_capacity_net" : dataobj.to_float(),
        "thermal_capacity" : dataobj.to_float(),
        "design_net_capacity" : dataobj.to_float(),
        "gross_capacity" : dataobj.to_float(),
        "construction_start" : dataobj.date_str(out_format="%Y-%m-%d"),
        "construction_suspend" : dataobj.date_str(out_format="%Y-%m-%d"),
        "construction_restart" : dataobj.date_str(out_format="%Y-%m-%d"),
        "first_criticality" : dataobj.date_str(out_format="%Y-%m-%d"),
        "first_grid_connection" : dataobj.date_str(out_format="%Y-%m-%d"),
        "commercial_operation" : dataobj.date_str(out_format="%Y-%m-%d"),
        "longterm_shutdown" : dataobj.date_str(out_format="%Y-%m-%d"),
        "restart" : dataobj.date_str(out_format="%Y-%m-%d"),
        "permanent_shutdown" : dataobj.date_str(out_format="%Y-%m-%d")
    }

    DEFAULT_COERCE = [dataobj.to_unicode()]

    IGNORE_VALUES = {
        "construction_start" : ["N/A"],
        "construction_suspend" : ["N/A"],
        "construction_restart" : ["N/A"],
        "first_criticality" : ["N/A"],
        "first_grid_connection" : ["N/A"],
        "commercial_operation" : ["N/A"],
        "longterm_shutdown" : ["N/A"],
        "restart" : ["N/A"],
        "permanent_shutdown" : ["N/A"]
    }

    def __init__(self, path):
        super(MasterSheet, self).__init__(path)


class PRISSheet(clcsv.SheetWrapper):

    HEADERS = {
        # main identifying field
        u'Reactor Name' : "reactor_name",
        u"Alternate Name" : "alternate_name",
        u"Location" : "country",
        u"Status" : "status",
        u"Owner" : "owner",
        u"Operator" : "operator",
        u"Model" : "model",
        u"Process" : "process",
        u"Reference Unit Power (Net Capacity)" : "reference_unit_power_capacity_net",
        u"Thermal Capacity" : "thermal_capacity",
        u"Design Net Capacity" : "design_net_capacity",
        u"Gross Capacity" : "gross_capacity",
        u"Construction Start Date" : "construction_start",
        u"Construction Suspend Date" : "construction_suspend",
        u"Construction Restart Date" : "construction_restart",
        u"First Criticality Date" : "first_criticality",
        u"First Grid Connection" : "first_grid_connection",
        u"Commercial Operation Date" : "commercial_operation",
        u"Longterm Shutdown Date" : "longterm_shutdown",
        u"Restart Date" : "restart",
        u"Permanent Shutdown Date" : "permanent_shutdown"
    }

    COERCE = {
        "reference_unit_power_capacity_net" : dataobj.to_float(),
        "thermal_capacity" : dataobj.to_float(),
        "design_net_capacity" : dataobj.to_float(),
        "gross_capacity" : dataobj.to_float(),
        "construction_start" : dataobj.date_str(out_format="%Y-%m-%d"),
        "construction_suspend" : dataobj.date_str(out_format="%Y-%m-%d"),
        "construction_restart" : dataobj.date_str(out_format="%Y-%m-%d"),
        "first_criticality" : dataobj.date_str(out_format="%Y-%m-%d"),
        "first_grid_connection" : dataobj.date_str(out_format="%Y-%m-%d"),
        "commercial_operation" : dataobj.date_str(out_format="%Y-%m-%d"),
        "longterm_shutdown" : dataobj.date_str(out_format="%Y-%m-%d"),
        "restart" : dataobj.date_str(out_format="%Y-%m-%d"),
        "permanent_shutdown" : dataobj.date_str(out_format="%Y-%m-%d")
    }

    DEFAULT_COERCE = [dataobj.to_unicode()]

    IGNORE_VALUES = {
        "construction_start" : ["N/A"],
        "construction_suspend" : ["N/A"],
        "construction_restart" : ["N/A"],
        "first_criticality" : ["N/A"],
        "first_grid_connection" : ["N/A"],
        "commercial_operation" : ["N/A"],
        "longterm_shutdown" : ["N/A"],
        "restart" : ["N/A"],
        "permanent_shutdown" : ["N/A"]
    }

    def __init__(self, path):
        super(PRISSheet, self).__init__(path)
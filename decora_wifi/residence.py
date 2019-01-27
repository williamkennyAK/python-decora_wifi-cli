# Leviton Cloud Services API model Residence.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Residence(BaseModel):
    def __init__(self, session, model_id=None):
        super(Residence, self).__init__(session, model_id)

    def add_person(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/addPerson".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/count"
        return session.call_api(api, attribs, 'get')

    def count_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_iot_switches(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_areas(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_breaker_panels(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_rooms(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_residential_schedules(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences"
        return session.call_api(api, attribs, 'post')

    def create_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_iot_switches(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_many(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences"
        return session.call_api(api, attribs, 'post')

    def create_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_areas(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_breaker_panels(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_rooms(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_residential_schedules(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_iot_switches(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_areas(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_breaker_panels(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_rooms(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_residential_schedules(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations/{1}".format(self._id, invitation_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_iot_switches(self, iot_switch_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches/{1}".format(self._id, iot_switch_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_omni_notifiers(self, omni_notifier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_activities(self, residential_activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_areas(self, residential_area_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas/{1}".format(self._id, residential_area_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_breaker_panels(self, residential_breaker_panel_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels/{1}".format(self._id, residential_breaker_panel_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_rooms(self, residential_room_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms/{1}".format(self._id, residential_room_id)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_residential_schedules(self, residential_schedule_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules/{1}".format(self._id, residential_schedule_id)
        return self._session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = Residence(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    def find_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations/{1}".format(self._id, invitation_id)
        data = self._session.call_api(api, attribs, 'get')

        from .invitation import Invitation
        model = Invitation(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_iot_switches(self, iot_switch_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches/{1}".format(self._id, iot_switch_id)
        data = self._session.call_api(api, attribs, 'get')

        from .iot_switch import IotSwitch
        model = IotSwitch(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_omni_notifiers(self, omni_notifier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier_id)
        data = self._session.call_api(api, attribs, 'get')

        from .omni_notifier import OmniNotifier
        model = OmniNotifier(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_activities(self, residential_activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_activity import ResidentialActivity
        model = ResidentialActivity(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_areas(self, residential_area_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas/{1}".format(self._id, residential_area_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_area import ResidentialArea
        model = ResidentialArea(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_breaker_panels(self, residential_breaker_panel_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels/{1}".format(self._id, residential_breaker_panel_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_breaker_panel import ResidentialBreakerPanel
        model = ResidentialBreakerPanel(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_rooms(self, residential_room_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms/{1}".format(self._id, residential_room_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_room import ResidentialRoom
        model = ResidentialRoom(self._session, data['id'])
        model.data = data
        return model

    def find_by_id_residential_schedules(self, residential_schedule_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules/{1}".format(self._id, residential_schedule_id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_schedule import ResidentialSchedule
        model = ResidentialSchedule(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/Residences/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_invitations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .invitation import Invitation
        result = []
        if items is not None:
            for data in items:
                model = Invitation(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_iot_switches(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .iot_switch import IotSwitch
        result = []
        if items is not None:
            for data in items:
                model = IotSwitch(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_omni_notifiers(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .omni_notifier import OmniNotifier
        result = []
        if items is not None:
            for data in items:
                model = OmniNotifier(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_account(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAccount".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .residential_account import ResidentialAccount
        model = ResidentialAccount(self._session, data['id'])
        model.data = data
        return model

    def get_residential_activities(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_activity import ResidentialActivity
        result = []
        if items is not None:
            for data in items:
                model = ResidentialActivity(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_areas(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_area import ResidentialArea
        result = []
        if items is not None:
            for data in items:
                model = ResidentialArea(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_breaker_panels(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_breaker_panel import ResidentialBreakerPanel
        result = []
        if items is not None:
            for data in items:
                model = ResidentialBreakerPanel(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_rooms(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_room import ResidentialRoom
        result = []
        if items is not None:
            for data in items:
                model = ResidentialRoom(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def get_residential_schedules(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules".format(self._id)
        items = self._session.call_api(api, attribs, 'get')

        from .residential_schedule import ResidentialSchedule
        result = []
        if items is not None:
            for data in items:
                model = ResidentialSchedule(self._session, data['id'])
                model.data = data
                result.append(model)
        return result

    def list_permissions(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/listPermissions".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def register_device(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/registerDevice".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def register_residential_breaker_panel(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/registerResidentialBreakerPanel".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def remove_person(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/removePerson".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    def update_attributes(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'put')

        self.data.update(attribs)
        return self

    def update_by_id_invitations(self, invitation_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/invitations/{1}".format(self._id, invitation_id)
        data = self._session.call_api(api, attribs, 'put')

        from .invitation import Invitation
        model = Invitation(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_iot_switches(self, iot_switch_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/iotSwitches/{1}".format(self._id, iot_switch_id)
        data = self._session.call_api(api, attribs, 'put')

        from .iot_switch import IotSwitch
        model = IotSwitch(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_omni_notifiers(self, omni_notifier_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/omniNotifiers/{1}".format(self._id, omni_notifier_id)
        data = self._session.call_api(api, attribs, 'put')

        from .omni_notifier import OmniNotifier
        model = OmniNotifier(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_activities(self, residential_activity_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialActivities/{1}".format(self._id, residential_activity_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_activity import ResidentialActivity
        model = ResidentialActivity(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_areas(self, residential_area_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialAreas/{1}".format(self._id, residential_area_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_area import ResidentialArea
        model = ResidentialArea(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_breaker_panels(self, residential_breaker_panel_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialBreakerPanels/{1}".format(self._id, residential_breaker_panel_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_breaker_panel import ResidentialBreakerPanel
        model = ResidentialBreakerPanel(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_rooms(self, residential_room_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialRooms/{1}".format(self._id, residential_room_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_room import ResidentialRoom
        model = ResidentialRoom(self._session, data['id'])
        model.data = data
        return model

    def update_by_id_residential_schedules(self, residential_schedule_id, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/{0}/residentialSchedules/{1}".format(self._id, residential_schedule_id)
        data = self._session.call_api(api, attribs, 'put')

        from .residential_schedule import ResidentialSchedule
        model = ResidentialSchedule(self._session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences"
        data = session.call_api(api, attribs, 'put')

        model = Residence(session, data['id'])
        model.data = data
        return model

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Residences/upsertWithWhere"
        return session.call_api(api, attribs, 'post')


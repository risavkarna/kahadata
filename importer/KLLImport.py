import UshahidiImport

class KLLImport(UshahidiImport.UshahidiImport):

    def grab_data(self, use_cache=False):
        return self._grab_data('http://quakemap.org/api?task=incidents', 'kll-data', use_cache)

    def find_record(self, row, db):
        return True 

    def parse_categories(self, categories):
        """
        Example response:
        u'categories': [{u'category': {u'id': 23, u'title': u'Food/Water/Shelter'}},
                         {u'category': {u'id': 3, u'title': u'Other'}}],

        Full category list
        {"categories":[
        {"category": {"id":"1","parent_id":"0","title":"Earthquake Damage","description":"Damage caused by earthquake","color":"9900CC","position":"0","icon":""} ,"translations":{"ne_NP":{"id":1,"category_title":"\u092d\u0942\u0915\u092e\u094d\u092a\u0940\u092f \u091b\u0947\u0924\u093f","category_description":""}}},
        {"category":{"id":"37","parent_id":"0","title":"VDC Trip Summaries","description":"Reports from trips to VDCs","color":"000000","position":"19","icon":""},"translations":[]},
        {"category":{"id":"13","parent_id":"0","title":"People Trapped","description":"People trapped inside fallen structures","color":"f0ff24","position":"20","icon":""},"translations":[]},
        {"category":{"id":"63","parent_id":"0","title":"Missing Person","description":"missing person","color":"626D70","position":"21","icon":""},"translations":[]},
        {"category":{"id":"14","parent_id":"0","title":"Blocked Roads","description":"Roads that are not accessible","color":"1054a6","position":"22","icon":""},"translations":[]},
        {"category":{"id":"15","parent_id":"0","title":"Shelter Area","description":"Places where people are taking shelter","color":"13ab05","position":"23","icon":""},"translations":[]},
        {"category":{"id":"26","parent_id":"15","title":"Medical Facility","description":"Has medical services","color":"34d12c","position":"24","icon":""},"translations":[]},
        {"category":{"id":"27","parent_id":"15","title":"Camp","description":"providing shelter","color":"7ae026","position":"25","icon":""},"translations":[]},
        {"category":{"id":"2","parent_id":"0","title":"Help Wanted","description":"Some kind of help needed","color":"3300FF","position":"26","icon":""},"translations":[]},
        {"category":{"id":"21","parent_id":"2","title":"Medical Evacuation","description":"Badly injured people","color":"0830fa","position":"27","icon":""},"translations":[]},
        {"category":{"id":"22","parent_id":"2","title":"Medical Assiatance","description":"Minor injuries","color":"3cad84","position":"28","icon":""},"translations":[]},
        {"category":{"id":"23","parent_id":"2","title":"Food\/Water\/Shelter\/Sanitation","description":"basic essentials urgently needed","color":"2c36eb","position":"29","icon":""},"translations":[]},
        {"category":{"id":"3","parent_id":"0","title":"Other","description":"Other reports","color":"663300","position":"31","icon":""},"translations":[]},
        {"category":{"id":"20","parent_id":"0","title":"Distribution Area","description":"Places where people are distributing food, water, tents etc.","color":"17e617","position":"33","icon":""},"translations":[]},
        {"category":{"id":"29","parent_id":"0","title":"Responding Organization","description":"Use this to mark the presence of Relief Efforts in an area","color":"eb4f07","position":"34","icon":""},"translations":[]},
        {"category":{"id":"30","parent_id":"29","title":"Medical Team","description":"Medical Teams who are working in the area","color":"e0711d","position":"35","icon":""},"translations":[]},
        {"category":{"id":"33","parent_id":"29","title":"Food, Water and Sanitation","description":"Groups providing food, water and sanitation material in the area","color":"f78b08","position":"36","icon":""},"translations":[]},
        {"category":{"id":"34","parent_id":"29","title":"Shelter","description":"Groups distributing tents, blankets, mats, etc in the area","color":"e39014","position":"37","icon":""},"translations":[]},
        {"category":{"id":"36","parent_id":"29","title":"Other","description":"Other relief effort. Please be very specific in the description.","color":"baa35f","position":"38","icon":""},"translations":[]},
        {"category":{"id":"35","parent_id":"29","title":"Rescue","description":"Groups involved in rescue of people trapped in buildings or blocked-off areas","color":"bf7424","position":"39","icon":""},"translations":[]}
        ]}
        """ 
        return categories;

    def parse_custom_fields(self, custom_fields):
        """
         u'customfields': {
            u'1': {u'field_default': u',Ward, VDC, Municipality, City/village, District, Region, Exact location, 100m, 500m, 1km, 5km, 50km, Other',
                   u'field_height': u'5',
                   u'field_id': u'1',
                   u'field_isdate': u'0',
                   u'field_ispublic_submit': u'0',
                   u'field_ispublic_visible': u'0',
                   u'field_maxlength': u'0',
                   u'field_name': u'Location Accuracy: - the report is from in this...',
                   u'field_required': u'0',
                   u'field_response': u'Ward',
                   u'field_type': u'7',
                   u'field_width': u'0',
                   u'form_id': u'1'},
           u'2': {u'field_default': None,
                  u'field_height': u'5',
                  u'field_id': u'2',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'0',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Phone Number',
                  u'field_required': u'0',
                  u'field_response': u'',
                  u'field_type': u'1',
                  u'field_width': u'0',
                  u'form_id': u'1'},
          u'3': {u'field_default': u', Dhading, Dolakha, Gorkha, Kathmandu, Kavrepalanchok, Lalitpur, Nuwakot, Okhaldhunga, Ramechhap, Rasuwa, Sindhuli, Sindhupalchok, Other',
                  u'field_height': u'5',
                  u'field_id': u'3',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'0',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Most Affected District',
                  u'field_required': u'0',
                  u'field_response': u'Kavrepalanchok',
                  u'field_type': u'7',
                  u'field_width': u'0',
                  u'form_id': u'1'},
          u'4': {u'field_default': u'Humanity Road, KLL',
                  u'field_height': u'5',
                  u'field_id': u'4',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'14',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Location accuracy checked or fixed by...',
                  u'field_required': u'0',
                  u'field_response': u'KLL',
                  u'field_type': u'6',
                  u'field_width': u'0',
                  u'form_id': u'1'},
          u'5': {u'field_default': u', partially meets the needs, fully meets the needs',
                  u'field_height': u'5',
                  u'field_id': u'5',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'14',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Dispatched organization capacity',
                  u'field_required': u'0',
                  u'field_response': u'',
                  u'field_type': u'7',
                  u'field_width': u'0',
                  u'form_id': u'1'},
          u'8': {u'field_default': None,
                  u'field_height': u'5',
                  u'field_id': u'8',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'14',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Number of times contact attempted',
                  u'field_required': u'0',
                  u'field_response': u'',
                  u'field_type': u'1',
                  u'field_width': u'0',
                  u'form_id': u'1'},
          u'9': {u'field_default': None,
                  u'field_height': u'5',
                  u'field_id': u'9',
                  u'field_isdate': u'0',
                  u'field_ispublic_submit': u'14',
                  u'field_ispublic_visible': u'0',
                  u'field_maxlength': u'0',
                  u'field_name': u'Number of times reached',
                  u'field_required': u'0',
                  u'field_response': u'',
                  u'field_type': u'1',
                  u'field_width': u'0',
                  u'form_id': u'1'}},
           u'10': {u'field_default': u'Dispatched',
                   u'field_height': u'5',
                   u'field_id': u'10',
                   u'field_isdate': u'0',
                   u'field_ispublic_submit': u'4',
                   u'field_ispublic_visible': u'0',
                   u'field_maxlength': u'0',
                   u'field_name': u'Dispatch Status - Quakemap.org team has contacted an organization and they have agreed to respond to this report',
                   u'field_required': u'0',
                   u'field_response': u'',
                   u'field_type': u'6',
                   u'field_width': u'0',
                   u'form_id': u'1'},
           u'12': {u'field_default': u'"box"',
                   u'field_height': u'5',
                   u'field_id': u'12',
                   u'field_isdate': u'0',
                   u'field_ispublic_submit': u'2',
                   u'field_ispublic_visible': u'0',
                   u'field_maxlength': u'0',
                   u'field_name': u'For Approval / Status Adjustment',
                   u'field_required': u'0',
                   u'field_response': u'',
                   u'field_type': u'8',
                   u'field_width': u'0',
                   u'form_id': u'1'},
           u'13': {u'field_default': u'BLANKDIV-13',
                   u'field_height': u'5',
                   u'field_id': u'13',
                   u'field_isdate': u'0',
                   u'field_ispublic_submit': u'2',
                   u'field_ispublic_visible': u'0',
                   u'field_maxlength': u'0',
                   u'field_name': u'BLANKDIV-13',
                   u'field_required': u'0',
                   u'field_response': u'',
                   u'field_type': u'9',
                   u'field_width': u'0',
                   u'form_id': u'1'},
           u'14': {u'field_default': u'Closed',
                   u'field_height': u'5',
                   u'field_id': u'14',
                   u'field_isdate': u'0',
                   u'field_ispublic_submit': u'14',
                   u'field_ispublic_visible': u'0',
                   u'field_maxlength': u'0',
                   u'field_name': u'Closed Status - nothing more needed from quakemap.org team',
                   u'field_required': u'0',
                   u'field_response': u'',
                   u'field_type': u'6',
                   u'field_width': u'0',
                   u'form_id': u'1'},
        """
        return custom_fields


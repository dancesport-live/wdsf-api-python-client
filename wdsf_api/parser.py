import datetime

from dacite import from_dict, Config
import xmltodict

from wdsf_api.types import Competition, Official, Participant, Person


class Parser:
    
    NAMESPACES = { 'http://services.worlddancesport.org/api': None }

    @staticmethod
    def parse_dict(
        xml_input,
        root: str = None,
        collections: dict = {},
        ):

        result_dict = xmltodict.parse(
            xml_input,
            process_namespaces=True,
            namespaces=Parser.NAMESPACES,
            force_list=collections.values(),
        )

        if root:
            result_dict = result_dict[root]

        for k, v in collections.items():
            result_dict[k] = result_dict[k][v]

        return result_dict
    
    @staticmethod
    def from_dict(data_class, data):
        return from_dict(data_class, data, Config(
            cast=[int, float],
            type_hooks={
                datetime.datetime: Parser.parse_datetime,
                datetime.date: Parser.parse_date,
            }
        ))
    
    @staticmethod
    def parse_date(date_str) -> datetime.date:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    @staticmethod
    def parse_datetime(date_str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

    @staticmethod
    def parse_generic(
        xml_input,
        data_class,
        root = None,
        collections = {},
        ):
        
        data_dict = Parser.parse_dict(
            xml_input,
            root=root,
            collections=collections
            )
        return Parser.from_dict(
            data_class=data_class,
            data=data_dict,
        )

    @staticmethod
    def parse_competition(xml):
        competition_dict = Parser.parse_dict(
            xml,
            root='competition',
            )
        return Parser.from_dict(
            data_class=Competition,
            data=competition_dict,
        )
    
    @staticmethod
    def parse_person(xml):
        person_dict = Parser.parse_dict(
            xml,
            root='person',
            collections={'licenses': 'license'},
            )
        return Parser.from_dict(
            data_class=Person,
            data=person_dict,
        )

    @staticmethod
    def parse_official(xml_input):
        return Parser.parse_generic(
            xml_input,
            data_class=Official,
            root='official'
        )
    
    @staticmethod
    def parse_participant(xml_input):
        return Parser.parse_generic(
            xml_input,
            data_class=Participant,
            root='participant'
        )
from operator import index
from .models import Hotel, Offer
from datetime import datetime

class Data:

    def __init__(self, searchURL):
        self.__searchURL = searchURL
        self.__dataDict = {}
        self.__UrlToData()
        print(self.__dataDict)



    def __UrlToData(self):
        searchURL = self.__searchURL
        print(searchURL)
        sections = searchURL.split("&")
        #eigene Methode ?
        for element in sections:
            e = element.split("=")
            match e[0]:
                case 'abflughafen':
                    self.__dataDict['outbounddepartureairport'] = e[1]
                case 'anzahlErwachsene':
                    self.__dataDict['countAdults'] = e[1]
                case 'anzahlKinder':
                    self.__dataDict['countChildren'] = e[1]
                case 'begin':
                    begin = datetime.strptime(e[1], "%Y-%m-%d").date()
                    print(type(begin))
                    self.__dataDict['depatureDate__date'] = begin
                case 'ende':
                    ende = datetime.strptime(e[1], "%Y-%m-%d")
                    self.__dataDict['returnDate__date'] = ende.date()
                case 'pension':
                    if e[1] != 'all':
                        self.__dataDict['mealtype'] = e[1]
                case 'oceanblick':
                    oceanblick = e[1]
                    if oceanblick == 'on':
                        oceanblick = True
                    else:
                        oceanblick = False
                    self.__dataDict['oceanview'] = oceanblick
                case 'raumtyp':
                    if e[1] != 'all':
                        self.__dataDict['roomtype'] = e[1]
                case _:
                    pass


    def getDataDict(self):
        return self.__dataDict
    
    # optimierter Datensatz damit ein Formfehler bei der Weitergabe der Suchparametern nicht passiert noch nötig ?
    def get_optimized_DataDict(self):
        op_dataDict = self.__dataDict.copy()
        if op_dataDict.get('begin') != None:
            op_dataDict.update('begin', datetime.strftime(op_dataDict.get('begin'), "%Y-%m-%d"))
        if op_dataDict.get('ende') != None:
            op_dataDict.update('ende', datetime.strftime(op_dataDict.get('ende'), "%Y-%m-%d"))
        return op_dataDict

    def searchOffers(self):
        print(self.__dataDict)
        objs = Offer.objects.all()
        objs = objs.filter(**self.__dataDict)
        return objs

    def searchHotels(self, objs):
        # hotelIDs = objs.values('Hotel_ID')
        # hotels = {}
        # for hotel in hotelIDs:
        #     obj = Hotel.objects.filter(Hotel_ID = hotel.get('Hotel_ID'))
        #     if len(obj) == 1:
        #         hotels[hotel.get('Hotel_ID')] = obj

        hotelIDs = objs.values('Hotel_ID')
        for hotel in hotelIDs:
            hotels = Hotel.objects.filter(Hotel_ID = hotel.get('Hotel_ID'))
            if len(hotel) == 1:
                
                print(hotels)
       # return hotels
        
    def getDuration(self):
        if self.__dataDict.get('returnDate') != None and self.__dataDict.get('depatureDate') != None:
            return self.__dataDict.get('returnDate') - self.__dataDict.get('depatureDate')

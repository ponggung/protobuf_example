import APHDC_pb2
from google.protobuf.json_format import MessageToJson
import json


def toPB(result):
    data_add = APHDC_pb2.ApHdc()
    # game status
    data_add.source = result["source"]
    data_add.game_class = result["game_class"]
    data_add.game_type = result["game_type"]
    data_add.status = result["status"]
    data_add.event_time = result["event_time"]
    data_add.source_updatetime = result["source_updatetime"]
    data_add.live = result["live"]

    # information
    information = result["information"]
    data_add.information.league = information["league"]
    data_add.information.game_title = information["game_title"]
    data_add.information.home.rot_id = information["home"]["rot_id"]
    data_add.information.home.team_name = information["home"]["team_name"]
    data_add.information.home.pitcher = information["home"]["pitcher"]
    data_add.information.away.rot_id = information["away"]["rot_id"]
    data_add.information.away.team_name = information["away"]["team_name"]
    data_add.information.away.pitcher = information["away"]["pitcher"]
    data_add.score.home = result["score"]["home"]
    data_add.score.away = result["score"]["away"]

    # handicap
    handicap = result["handicap"]
    for h_type,odds in handicap.items():
        if h_type == "zf_tw":
            data_add.twZF.homeZF.line = handicap["zf_tw"]["home"]["line"]
            data_add.twZF.homeZF.odds = handicap["zf_tw"]["home"]["odds"]
            data_add.twZF.awayZF.line = handicap["zf_tw"]["away"]["line"]
            data_add.twZF.awayZF.odds = handicap["zf_tw"]["away"]["odds"]
        elif h_type == "ds_tw":
            data_add.twDS.line = handicap["ds_tw"]["line"]
            data_add.twDS.over = handicap["ds_tw"]["over"]
            data_add.twDS.under = handicap["ds_tw"]["under"]
        elif h_type == "de":
            data_add.de.home = handicap["de"]["home"]
            data_add.de.away = handicap["de"]["away"]
            data_add.draw = handicap["draw"]
        elif h_type == "esre":
            data_add.esre.let = handicap["esre"]["let"]
            data_add.esre.home = handicap["esre"]["home"]
            data_add.esre.away = handicap["esre"]["away"]

    # data_add.draw = result[""]
    return data_add

def list_toPB(handi_result):
    pb_list = []
    for result in handi_result:
        pb_data = toPB(result)
        pb_list.append(pb_data)
    # print(pb_list)

    data = APHDC_pb2.ApHdcArr()
    data.aphdc.extend(pb_list)
    data = data.SerializeToString()
    return data

def toJson(pb_data):
    data = APHDC_pb2.ApHdcArr()
    data.ParseFromString(pb_data)
    jsonObj = MessageToJson(data)
    jsonObj = json.loads(jsonObj)["aphdc"]
    # print(type(data))
    return jsonObj


if __name__=="__main__":

    # Input
    with open("handi_result.json", "r") as file:
        handi_result = json.load(file)

    # json list 轉成 Protobuf file
    pb_data = list_toPB(handi_result)
    print(pb_data)

    print("--------------------")
    # 轉回 json

    jsonObj = toJson(pb_data)
    print(jsonObj)

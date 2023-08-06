#from rasa.nlu.model import Interpreter #Comented by Pravin K on 26-APR-21  [to avoide rasa installation issue] 
import json
import glob
import os
import loggerutility as logger

class Rasa_id_interpreter:
    
    # def __init__(self):
    #     logger.log("init Rasa_id_interpreter ","0")

    @staticmethod
    def get_model_path(enterprise, modelScope, modelType, modelName):
        modelName  = "item_classification"
        base_filePath = "/proteus-sense/trained_model/"
        filePath=""
        if modelType == "" or modelType == None:
            modelType  = "product_identification"
        
        if enterprise != "" or enterprise != None:
            modelScope = "enterprise"
            filePath = base_filePath + modelType +  "/" +modelScope + "/" + enterprise + "/"+ modelName
            if not os.path.exists(filePath):
                logger.log(f"{modelName} not found against {modelScope.upper()}","0")
                modelScope = "global"
                filePath = base_filePath + modelType +  "/" +modelScope + "/"+ modelName 
                if not os.path.exists(filePath):
                    logger.log(f"{modelName} not found against {modelScope.upper()}","0")    
        else:
            modelScope = "global"
            filePath = filePath + modelType +  "/" +modelScope + "/"+ modelName 
            if not os.path.exists(filePath):
                logger.log(f"{modelName} not found against {modelScope.upper()}","0")    
            
        logger.log(f"\nenterprise::{enterprise}, \nmodelScope::{modelScope}, \nmodelType::{modelType}, \nmodelName::{modelName}, \nfilePath::{filePath}","0")    
        list_of_files1 = glob.glob(filePath+"/models/*.tar.gz")    # Added by SwapnilB on [ 02-Feb-23 ] 
        logger.log(f"list_of_files1 [{list_of_files1}]","0")
        latest_file = max(list_of_files1, key=os.path.getctime)
        rasa_model_path = latest_file+"/nlu"
        return rasa_model_path

    @staticmethod
    def rasa_output(text,attr_count,enterprise,modelScope, modelType, modelName):   #Added by SwapnilB
    # def rasa_output(self,text,attr_count,modelName):  
        logger.log(f"In rasa_output text:{text}","0")
        from rasa.nlu.model import Interpreter  #Added by Pravin K on 26-APR-21 [to avoide rasa installation issue]
        res=[]
        rasa_model_path = Rasa_id_interpreter.get_model_path(enterprise,modelScope, modelType, modelName)
        # rasa_model_path = self.get_model_path(modelName)    #Added by SwapnilB
        interpreter = Interpreter.load(rasa_model_path)
        logger.log(f"In rasa_output interpreter:{interpreter}","0")
        for t in range(len(text)):
            result = interpreter.parse(text[t])
            entities = result['entities']
            entity_dict = {}
            for j in range(attr_count):
                attr_name = 'attr' + str(j + 1)
                for i in range(len(entities)):
                    if entities[i]['entity'] == attr_name and entities[i]['extractor'] == 'DIETClassifier' and entities[i]['confidence_entity'] >= 0.90:
                        entity_dict[attr_name] = entities[i]['value']
            res.append(entity_dict)
        logger.log(f"Rasa_id_interpreter class rasa_output() res::: {res}","0")
        return res

    @staticmethod
    def extract_entities(products,attr_count,enterprise, modelScope, modelType, modelName):  #Added by SwapnilB 
    # def extract_entities(self,products,attr_count,modelName):  
        # logger.log(f"In extract_entities[{products}]attr_count[{attr_count}],enterprise[{modelName}]","0")
        result = []
        entities_extracted = Rasa_id_interpreter.rasa_output(products,attr_count,enterprise,modelScope, modelType, modelName)   # Added by SwapnilB
        # entities_extracted = self.rasa_output(self,products,attr_count,modelName)  
        logger.log(f"entities_extracted line 72::: \n {entities_extracted}","0")
        for i in range(len(entities_extracted)):
            attr_list = []
            for j in range(attr_count):
                attr_key = 'attr' + str(j+1)
                attr_list.append(entities_extracted[i].get(attr_key,0))
            text=''
            result_dict={}
            for k in range(len(attr_list)):
                if attr_list[k]!=0:
                    key='attr'+ str(k+1)
                    result_dict[key] = attr_list[k]
            result_dict['descr'] = products[i]
            result_dict['id'] = i+1
            result.append(result_dict)
        logger.log(f"Rasa_id_interpreter class extract_entities() result::: {result}","0")
        return result

    # extract_entities( ["Augmentin 375mg Intravenous"],attr_count=3)
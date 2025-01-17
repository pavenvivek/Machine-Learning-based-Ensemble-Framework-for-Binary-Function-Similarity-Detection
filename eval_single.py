import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
print (tf.__version__)
import numpy as np
import argparse
import json
from datetime import datetime
from siamese_nonuplet import graphnn
#from utils import *
from utils_cflg import *
from settings import *



parser = argparse.ArgumentParser()
parser.add_argument('--device', type=str, default='0',
        help='visible gpu device')
parser.add_argument('--fea_dim1', type=int, default=32,
        help='feature dimension')
parser.add_argument('--fea_dim2', type=int, default=7,
        help='feature dimension')
parser.add_argument('--fea_dim3', type=int, default=2560,
        help='feature dimension')
parser.add_argument('--embed_dim', type=int, default=64, #64,
        help='embedding dimension')
parser.add_argument('--embed_depth', type=int, default=2, #2,
        help='embedding network depth')
parser.add_argument('--output_dim', type=int, default=64, #64,
        help='output layer dimension')
parser.add_argument('--iter_level', type=int, default=5, #5,
        help='iteration times')
parser.add_argument('--lr', type=float, default=1e-4,
        help='learning rate')
parser.add_argument('--epoch', type=int, default=100,
        help='epoch number')
parser.add_argument('--batch_size', type=int, default=1,
        help='batch size')
parser.add_argument('--load_path', type=str,
        default='./saved_model/graphnn-model_best')
parser.add_argument('--log_path', type=str, default=None,
        help='path for training log')


if __name__ == '__main__':
    args = parser.parse_args()
    args.dtype = tf.float32
    print(f"Parameters: {args}")

    os.environ["CUDA_VISIBLE_DEVICES"] = args.device
    
    Dtype = args.dtype

    NODE_FEATURE_DIM1 = args.fea_dim1
    NODE_FEATURE_DIM2 = args.fea_dim2
    NODE_FEATURE_DIM3 = args.fea_dim3

    EMBED_DIM = args.embed_dim
    EMBED_DEPTH = args.embed_depth
    OUTPUT_DIM = args.output_dim
    ITERATION_LEVEL = args.iter_level
    LEARNING_RATE = args.lr
    MAX_EPOCH = args.epoch
    BATCH_SIZE = args.batch_size
    LOAD_PATH = args.load_path
    LOG_PATH = args.log_path

    SHOW_FREQ = 1
    TEST_FREQ = 1
    SAVE_FREQ = 25

    FUNC_NAME_DICT = {}

    # Process the input graphs
    F_NAME = ["./data/test_data.json"]  

    print ("Functions: {}".format(F_NAME))

    FUNC_NAME_DICT = get_f_dict(F_NAME)
    Gs, classes = read_graph(F_NAME, FUNC_NAME_DICT)
    print ("{} graphs, {} functions".format(len(Gs), len(classes)))
    

    avg_acu = 0
    total_auc = 0

    avg_acc2 = 0
    total_auc2 = 0

    total_auc2_1 = 0
    total_auc2_2 = 0
    total_auc2_3 = 0
    total_auc2_4 = 0

    total_auc2_1_flip = 0
    total_auc2_2_flip = 0
    total_auc_pm = 0
    total_auc_pm2 = 0
    total_auc_cmb = 0
    total_auc_cmb_2 = 0
    total_auc_cmb_3 = 0
    total_auc_cmb_4 = 0

    for i in range(0, 50):

      perm = [i for i in range(0, len(classes))]

      Gs_test, classes_test =\
            partition_data(Gs,classes,[1],perm)

      ids = []
      if os.path.isfile('./data/test_ids1.json'):
        with open('./data/test.json') as inf:
            test_ids = json.load(inf)
        with open('./data/test_ids.json') as inf:
            ids = json.load(inf)
        test_epoch = generate_epoch_pair_3(
                Gs_test, classes_test, BATCH_SIZE, load_id=test_ids, mode = "Testing")
        print ("loading existing data !")
      else:
        test_epoch, test_ids, ids = generate_epoch_pair_3(
                Gs_test, classes_test, BATCH_SIZE, output_id=True, mode = "Testing")



      # Model
      gnn = graphnn(
            N_x1 = NODE_FEATURE_DIM1,
            N_x2 = NODE_FEATURE_DIM2,
            N_x3 = NODE_FEATURE_DIM3,
            Dtype = Dtype, 
            N_embed = EMBED_DIM,
            depth_embed = EMBED_DEPTH,
            N_o = OUTPUT_DIM,
            ITER_LEVEL = ITERATION_LEVEL,
            lr = LEARNING_RATE
        )
      gnn.init(LOAD_PATH, LOG_PATH)

      test_auc, fpr, tpr, thres, auc2, auc2_1, auc2_2 = get_auc_epoch(
            gnn, Gs_test, classes_test, BATCH_SIZE, load_data=test_epoch, ids=ids, mode="Testing")
      gnn.say( "AUC on testing set itr {}: {}".format(i, test_auc) )



      total_auc = total_auc + test_auc
      total_auc2 = total_auc2 + auc2

      total_auc2_1 = total_auc2_1 + auc2_1
      total_auc2_2 = total_auc2_2 + auc2_2


    print ("\n\n-------------------------------------")
    print ("Average accuracy (AUC) after {} runs: {}".format(i+1, (total_auc/(i+1)) * 100))
    print ("Cirrina Average accuracy after {} runs: {}".format(i+1, total_auc2/(i+1)))
    print ("Average accuracy 2 case 1 after {} runs: {}".format(i+1, total_auc2_1/(i+1)))
    print ("Average accuracy 2 case 2 after {} runs: {}".format(i+1, total_auc2_2/(i+1)))


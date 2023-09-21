#!/bin/bash

# Define paths
STANFORD_NER_DIR=~/stanford-ner-2020-11-17
GOLD_STANDARD_WIKI=wikipedia-gold.txt
GOLD_STANDARD_FAN=fanwiki-gold.txt
GOLD_STANDARD_WIKI2=wikipedia-gold2.txt
GOLD_STANDARD_FAN2=fanwiki-gold2.txt
EVAL_WIKI=wikipedia-eval.txt
EVAL_FAN=fanwiki-eval.txt
EVAL_WIKI2=wikipedia-eval2.txt
EVAL_FAN2=fanwiki-eval2.txt

# Run the evaluation
java -mx600m -cp "$STANFORD_NER_DIR/stanford-ner.jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$STANFORD_NER_DIR/classifiers/english.all.3class.distsim.crf.ser.gz" -testFile "$GOLD_STANDARD_WIKI" > "$EVAL_WIKI"
java -mx600m -cp "$STANFORD_NER_DIR/stanford-ner.jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$STANFORD_NER_DIR/classifiers/english.all.3class.distsim.crf.ser.gz" -testFile "$GOLD_STANDARD_FAN" > "$EVAL_FAN"
java -mx600m -cp "$STANFORD_NER_DIR/stanford-ner.jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$STANFORD_NER_DIR/classifiers/english.all.3class.distsim.crf.ser.gz" -testFile "$GOLD_STANDARD_WIKI2" > "$EVAL_WIKI2"
java -mx600m -cp "$STANFORD_NER_DIR/stanford-ner.jar" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier "$STANFORD_NER_DIR/classifiers/english.all.3class.distsim.crf.ser.gz" -testFile "$GOLD_STANDARD_FAN2" > "$EVAL_FAN2"

echo "Evaluation completed. Results saved in $EVAL_WIKI and $EVAL_FAN."
echo "Evaluation completed. Results saved in $EVAL_WIKI2 and $EVAL_FAN2."

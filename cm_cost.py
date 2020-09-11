X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(list(y_test),y_pred))
tn, fp, fn, tp = confusion_matrix(y_test,y_pred).ravel()

total = len(y_test)
precision = tn/(tn+fn)
recall = tn/(tn+fp)
accuracy = (tp+tn)/total
print('Recall: ',recall)
print('Precision: ',precision)
print('Accuracy: ',accuracy)

tn_cost = 71
fp_cost = 0.2*(2*71)+0.8*(71-141-0.1*141)-0.05*141
fn_cost = -70
tp_cost = 71
rev = tn_cost*tn + fp_cost*fp + fn_cost*fn + tp_cost*tp
ori_rev = y_test.sum()*(-70)+(len(y_test)-y_test.sum())*71
impro_gain = rev - ori_rev

##################For the whole sample##################
Y_pred = model.predict(X)

print(confusion_matrix(y,Y_pred))
tn, fp, fn, tp = confusion_matrix(y,Y_pred).ravel()

total = len(y)
precision = tn/(tn+fn)
recall = tn/(tn+fp)
accuracy = (tp+tn)/total
print('Recall: ',recall)
print('Precision: ',precision)
print('Accuracy: ',accuracy)

ori_rev = df['IsCanceled'].sum()*(-70)+(len(df['IsCanceled'])-df['IsCanceled'].sum())*71
rev = tn_cost*tn + fp_cost*fp + fn_cost*fn + tp_cost*tp
print("Total additional revenue gain: ", rev -ori_rev)
print("Additional revenue gain per order: ", (rev -ori_rev)/len(df))
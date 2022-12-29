#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;
class SegmentTree {
public:
    int level = 0;
    int length = 0;
    vector<int> inputList;
    int inputListLength = 0;
    int inputStartIndex = 0;
    int inputEndIndex = 0;
    int treeIndex = 1;
    string calculationMethod;
    vector<int> resultList;
    int rangeResult = 0;

    SegmentTree (vector<int>* inputList, string calculationMethod) {
        this->calculationMethod = calculationMethod;
        this->inputListLength = (*inputList).size();
        this->inputEndIndex = this->inputListLength - 1;

        for (int i = 0; i < this->inputListLength; i++) {
            this->inputList.push_back((*inputList)[i]);
        }

        this->level = (int) ceil(log(this->inputListLength) / log(2)) + 1;
        this->length = (int) pow(2, this->level);
        this->resultList = vector<int>(this->length, 0);

        this->make(0, this->inputListLength-1, 1);
    }

    int gcd(int leftResult, int rightResult) {
        if(rightResult == 0) {
            return leftResult;
        }

        return this->gcd(rightResult, leftResult % rightResult);
    }

    int method(int leftResult, int rightResult) {
        if (this->calculationMethod == "sum") {
            return leftResult + rightResult;
        }
        else if (this->calculationMethod == "max") {
            return max(leftResult, rightResult);
        }
        else if (this->calculationMethod == "gcd") {
            return this->gcd(leftResult, rightResult);
        }
    }

    int updateProcess(int inputStartIndex, int inputEndIndex, int treeIndex, int updateIndex, int updateValue) {
        if ((updateIndex < inputStartIndex) || (updateIndex > inputEndIndex)) {
            return this->resultList[treeIndex];
        }

        if (inputStartIndex == inputEndIndex) {
            this->resultList[treeIndex] = updateValue;
            return this->resultList[treeIndex];
        }

        int inputMidIndex = (inputStartIndex + inputEndIndex) / 2;
        int leftResult = this->updateProcess(inputStartIndex, inputMidIndex, treeIndex * 2, updateIndex, updateValue);
        int rightResult = this->updateProcess(inputMidIndex + 1, inputEndIndex, treeIndex * 2 + 1, updateIndex, updateValue);

        this->resultList[treeIndex] = this->method(leftResult, rightResult);

        return this->resultList[treeIndex];
    }

    void update(int updateIndex, int updateValue) {
        this->treeIndex = 1;
        this->inputList[updateIndex] = updateValue;

        this->updateProcess(this->inputStartIndex, this->inputEndIndex, this->treeIndex, updateIndex, updateValue);
    }

    int getRangeProcess(int inputStartIndex, int inputEndIndex, int treeIndex, int rangeStartIndex, int rangeEndIndex) {
        if ((inputEndIndex < rangeStartIndex) || (inputStartIndex > rangeEndIndex)) {
            return 0;
        }

        if ((inputStartIndex >= rangeStartIndex) && (inputEndIndex <= rangeEndIndex)) {
            return this->resultList[treeIndex];
        }

        int inputMidIndex = (inputStartIndex + inputEndIndex) / 2;

        int leftResult = this->getRangeProcess(inputStartIndex, inputMidIndex, treeIndex * 2, rangeStartIndex, rangeEndIndex);
        int rightResult = this->getRangeProcess(inputMidIndex + 1, inputEndIndex, treeIndex * 2 + 1, rangeStartIndex, rangeEndIndex);

        return this->method(leftResult, rightResult);
    }

    int getRange(int rangeStartIndex, int rangeEndIndex) {
        this->rangeResult = this->getRangeProcess(this->inputStartIndex, this->inputEndIndex, this->treeIndex, rangeStartIndex, rangeEndIndex);
        return this->rangeResult;
    }

    int make(int inputStartIndex, int inputEndIndex, int treeIndex) {
        if (inputStartIndex == inputEndIndex) {
            this->resultList[treeIndex] = this->inputList[inputStartIndex];
            return this->resultList[treeIndex];
        }

        int inputMidIndex = (inputStartIndex + inputEndIndex) / 2;
        int leftResult = this->make(inputStartIndex, inputMidIndex, treeIndex * 2);
        int rightResult = this->make(inputMidIndex + 1, inputEndIndex, treeIndex * 2 + 1);

        this->resultList[treeIndex] = this->method(leftResult, rightResult);

        return this->resultList[treeIndex];
    }

};

int main(void) {

    int rangeSum = 0;
    vector<int> numberList = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    SegmentTree segmentTree(&numberList, "sum");;


    for(auto value: segmentTree.resultList) {
        cout << value << ends;
    }
    cout << "\n";

    rangeSum = segmentTree.getRange(3, 5);
    cout << rangeSum << endl;

    segmentTree.update(4, 7);
    for(auto value: segmentTree.resultList) {
        cout << value << ends;
    }
    cout << "\n";
    rangeSum = segmentTree.getRange(3, 5);
    cout << rangeSum << endl;


    return 0;
}

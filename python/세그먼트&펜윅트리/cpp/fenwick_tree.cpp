#include <iostream>
#include <vector>

using namespace std;

class FenwickTree {
public:
    int inputListLength = 0;
    vector<int> inputList;
    vector<int> resultList;

    FenwickTree (vector<int>* inputList) {
        this->inputListLength = (*inputList).size();
        this->resultList = vector<int>(this->inputListLength, 0);

        for (int i = 0; i < this->inputListLength; i++) {
            this->inputList.push_back((*inputList)[i]);
        }

        int inputIndex = 1;
        for(int i = 0; i < this->inputListLength; i++) {
            this->update(inputIndex, this->inputList[i]);
            inputIndex = inputIndex + 1;
        }
    }

    void update(int inputIndex, int inputValue) {
        while(inputIndex < this->resultList.size()) {
            this->resultList[inputIndex] += inputValue;
            inputIndex = inputIndex + (inputIndex & -inputIndex);
        }
    }

    int getIndexRange(int index) {
        int result = 0;

        while (index > 0) {
            result += this->resultList[index];
            index =  index - (index &  -index);
        }

        return result;
    }

    int getRange(int rangeStartIndex, int rangeEndIndex) {
        int leftResult = this->getIndexRange(rangeStartIndex-1);
        int rightResult = this->getIndexRange(rangeEndIndex);

        return rightResult - leftResult;
    }
};

int main(void) {
    int rangeSum = 0;
    vector<int> numberList = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    FenwickTree fenwickTree(&numberList);

    for(auto value: fenwickTree.resultList) {
        cout << value << ends;
    }
    cout << "\n";

    rangeSum = fenwickTree.getRange(3, 5);
    cout << rangeSum << endl;


    fenwickTree.update(4, 3);
    for(auto value: fenwickTree.resultList) {
        cout << value << ends;
    }
    cout << "\n";

    rangeSum = fenwickTree.getRange(3, 5);
    cout << rangeSum << endl;


    return 0;
}
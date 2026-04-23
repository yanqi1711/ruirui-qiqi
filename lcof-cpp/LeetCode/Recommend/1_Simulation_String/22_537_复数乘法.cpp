class Solution {
public:
    struct RealImage
    {
        int real;
        int image;
        RealImage(string num) {
            size_t pos = num.find('+');
            if (pos != string::npos) {
                // 处理形如 "a+bi"
                real = stoi(num.substr(0, pos));
                image = stoi(num.substr(pos + 1, num.size() - pos - 2));
            } else {
                // 处理形如 "ai" 或 "a"
                size_t i_pos = num.find('i');
                if (i_pos != string::npos) {
                    // 处理形如 "ai"
                    real = 0;
                    image = stoi(num.substr(0, i_pos));
                } else {
                    // 处理形如 "a"
                    real = stoi(num);
                    image = 0;
                }
            }
        }
        RealImage& operator*(const RealImage& num2)
        {
            int prevReal = this->real;
            real = real * num2.real + (-1)* image * num2.image;
            image = prevReal*num2.image + image*num2.real;
            return *this;
        }

        string data() const {
            return to_string(real) + "+" + to_string(image) + "i";
        }
        
    };
    string complexNumberMultiply(string num1, string num2) {
        RealImage r1(num1);
        return (r1*RealImage(num2)).data();
    }
};
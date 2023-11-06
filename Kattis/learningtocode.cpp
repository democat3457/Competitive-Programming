#include <map>
#include <regex>
#include <iostream>
#include <sstream>
#include <string>

auto variables = std::map<std::string, std::string*>();

void replaceOnce(std::string &str, const std::string &from, const std::string &to)
{
    if (from.empty())
        return;
    size_t pos = str.find(from);
    if (pos != std::string::npos)
        str.replace(pos, from.length(), to);
}

void replaceAll(std::string &str, const std::string &from, const std::string &to)
{
    if (from.empty())
        return;
    size_t start_pos = 0;
    while ((start_pos = str.find(from, start_pos)) != std::string::npos)
    {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
    }
}

std::string regex_replace(
    const std::string &input,
    const std::regex &regex,
    std::function<std::string(std::smatch const &match)> format)
{
    std::ostringstream output;
    std::sregex_iterator begin(input.begin(), input.end(), regex), end;
    std::string suffix = "";
    for (; begin != end; begin++)
    {
        output << begin->prefix() << format(*begin);
        suffix = begin->suffix();
    }
    output << suffix;
    return output.str();
}

std::string* parse_template(std::string s)
{
    std::regex backtickRemove("^`(.*)`$");
    std::regex varParse("\\$\\{(.+?)\\}");
    s = std::regex_replace(s, backtickRemove, "$1");
    replaceAll(s, "${`", "");
    replaceAll(s, "`}", "");
    replaceAll(s, "${\"", "");
    replaceAll(s, "\"}", "");

    // std::cout << "--- Template to parse: " << s << std::endl;

    s = regex_replace(s, varParse, [](std::smatch const &match){
        // std::cout << "--- match " << match[0] << " 1 " << match[1] << std::endl;
        return *variables[match[1]];
    });
    // std::cout << "--- result " << s << std::endl;
    return new std::string(s);
}

std::string* parse_value(std::string value)
{
    if (value.at(0) == '`') return parse_template(value);
    if (value.at(0) == '"') {
        std::regex quoteRemove("^\"(.*)\"$");
        // if (std::regex_search(value, quoteRemove)) std::cout << "--- Found quotes in " << value;
        std::string result = std::regex_replace(value, quoteRemove, "$1");
        // std::cout << " resulting in " << result << std::endl;
        return new std::string(result);
    }
    return variables[value];
}

int main()
{
    while (true)
    {
        std::string s;
        std::getline(std::cin, s);
        if (s == "end.")
            break;
        if (s.at(0) == 'v')
        {
            replaceOnce(s, "var ", "");
            replaceOnce(s, ";", "");
            size_t pos = s.find(" = ");
            std::string name = s.substr(0, pos);
            std::string value = s.substr(pos + 3);
            std::string *parsed = parse_value(value);
            variables[name] = parsed;
            // printf("--- Set %s to '%s'\n", name.c_str(), parsed->c_str());
        }
        else if (s.at(0) == 'p')
        {
            replaceOnce(s, "print ", "");
            replaceOnce(s, ";", "");
            std::cout << *parse_value(s) << std::endl;
        }
    }
}

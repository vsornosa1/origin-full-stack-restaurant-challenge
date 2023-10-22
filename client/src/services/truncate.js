export function truncateMealName (name, wordNumber) {
    if(name) return name.split(" ").slice(0, wordNumber).join(" ");
};

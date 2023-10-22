export function truncateMealName (name, wordNumber) {
    if(name) return name.split(" ").slice(0, wordNumber).join(" ");
};

export function parseTimeToString(timestamp) {
  if (!timestamp) return "";
  const regex = /(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})/;
  let matches = timestamp.match(regex);
  if (matches) {
    return matches[1] + " " + matches[2];
  }
};
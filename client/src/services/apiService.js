export async function getToken(credentials) {
  const response = await fetch("https://localhost:8443/api/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.message || "Login failed");
  }

  return response.json();
}


export async function makeApiCallWithToken(url, options = {}) {
  options.headers = options.headers || {};
  options.headers["Authorization"] = "Bearer " + localStorage.getItem("token");
  const response = await fetch(url, options);

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.message || "API call failed");
  }

  return response.json();
}



export async function registerUser(credentials) {
  const response = await fetch("https://localhost:8443/api/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || "Registration failed");
  }

  return response.json();
}
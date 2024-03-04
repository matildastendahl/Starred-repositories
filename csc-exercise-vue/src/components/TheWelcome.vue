<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const ID = "78b56c56898a8692e345"
const REDIRECT = "http://127.0.0.1:8000/callback"

const authenticationUrl = `https://github.com/login/oauth/authorize?client_id=${ID}&redirect_uri=${REDIRECT}&scope=repo`

const accessToken = ref('');

const loginToGitHub = () => {
  console.log("Login to GitHub function called");
  const url = new URL(window.location.href);
  console.log(url)
  console.log("URL search params:", url.searchParams);
  const code = url.searchParams.get('code');
  console.log("Code parameter found in URL:", code);
  if (code) {
    exchangeCodeForAccessToken(code);
  } else {
    window.location.href = authenticationUrl;
  }
}

const exchangeCodeForAccessToken = async (code) => {
  console.log("Exchange code for access token function called with code:", code);
  
  const response = await fetch(`https://github.com/login/oauth/access_token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    body: JSON.stringify({
      client_id: "78b56c56898a8692e345",
      client_secret: "dd53a4d74f81012fe8259b56806ad01af07bdac7",
      code: code
    })
  });

  const data = await response.json();
  console.log("Access token response:", data);
  accessToken.value = data.access_token;
  console.log("Access token:", accessToken.value);
  fetchStarredRepositories();
}

const fetchStarredRepositories = async () => {
  console.log("Fetch starred repositories function called");
  const response = await fetch(`https://api.github.com/user/starred`, {
    headers: {
      'Authorization': `Bearer ${accessToken.value}`
    }
  });

  const starredRepositories = await response.json();
  console.log(starredRepositories);
}

</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Starred repositories</template>

    Login with
    <a href="#" @click="loginToGitHub">GitHub</a>
  </WelcomeItem>

</template>
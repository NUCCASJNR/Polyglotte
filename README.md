# PolyGlotte

Polyglotte is a blogging platform that allows users to create and share blog posts, follow other users, and interact with their content.
It breaks one main blogging barrier which is multillingual blogging, Users can read blog in their desired language

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#Usage)

## Introduction

Polyglotte is a Blogging Platform is a web application that provides users with a platform to express their thoughts and share their knowledge through blog posts. Users can create an account, write and publish blog posts, follow other users, and engage with the content by liking and commenting on posts.

This platform aims to foster a community of bloggers, where users can discover interesting content, connect with like-minded individuals, and gain exposure for their own writing.

## Features

- User Registration: Users can create an account by providing their name, email address, and password.
- Blog Post Creation: Users can write and publish their own blog posts, including a title and content.
- User Profile: Each user has a profile page displaying their profile picture, bio, and a list of their published blog posts.
- Follow Users: Users can follow other users to receive updates on their new blog posts.
- Like and Comment: Users can like and comment on blog posts to show their appreciation and engage in discussions.
- Explore and Discover: Users can explore the platform to discover new blog posts and follow interesting authors.

## Requirements

To run the Blogging Platform, you need the following:

- Python 3.10
- Flask web framework
- SQLAlchemy
- MySQL

## Installation

1. Clone the repository:

```bash
git clone https://github.com/NUCCASJNR/Polyglotte.git
```
2. Change into the project directory

```bash
cd Polyglotte
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Setup the database
```bash
cat setup_mysql_dev.sql | sudo mysql
```

## Usage

1. Register a new account by providing your name, email, and password.
2. Log in to your account using your credentials.
3. Create a new blog post by clicking on the "New Post" button and providing a title and content.
4. Explore the platform to discover other users and their blog posts.
5. Follow other users to receive updates on their new posts.
6. Like and comment on blog posts to engage with the community.
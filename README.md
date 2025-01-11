# Kubernetes-Photo-Gallery-Application

This project implements a **Kubernetes-Photo-Gallery-Application** using **Kubernetes** to deploy a scalable photo management system. It integrates services like **Flask**, **MinIO**, and **MySQL** within a Kubernetes cluster. The application allows users to upload photos, manage albums, and perform search operations while providing hands-on experience with Kubernetes features like Pods, Deployments, Services, and PersistentVolumes.

## Important Notice
**For security reasons, sensitive files such as credentials, keys, and configuration files will NOT be included in this repository.**

---

## Overview

The system includes:
- **Flask Application** for the backend and user interface.
- **MinIO Object Storage** for storing uploaded photos.
- **MySQL Database** for storing metadata.
- **Kubernetes** for container orchestration.

---

## Features

1. **Photo Management**:
   - **Add Photos**: Upload photos to MinIO storage.
   - **Delete Photos**: Remove selected photos.
   - **Update Photos**: Modify titles, descriptions, and tags.

2. **Album Management**:
   - **Create Albums**: Organize photos into collections.
   - **Delete Albums**: Remove albums and associated photos.

3. **Search**:
   - Filter photos by metadata such as tags, titles, or descriptions.

4. **Database Integration**:
   - Store and retrieve metadata in a MySQL database.

5. **Kubernetes Orchestration**:
   - Use Kubernetes features like Pods, Deployments, Services, PersistentVolumes, and PersistentVolumeClaims.

---

## Setup Instructions

### Prerequisites

- Installed tools: `Minikube`, `kubectl`, `Python 3.x`, `Docker`

### Steps

1. **Set Up MySQL**:
   - Create PersistentVolume and PersistentVolumeClaim:
     ```bash
     kubectl apply -f configuration/1-mysql-vol.yaml
     ```
   - Deploy MySQL:
     ```bash
     kubectl apply -f configuration/2-mysql.yml
     ```

2. **Set Up MinIO**:
   - Create PersistentVolume and PersistentVolumeClaim:
     ```bash
     kubectl apply -f configuration/3-minio-vol.yaml
     ```
   - Deploy MinIO:
     ```bash
     kubectl apply -f configuration/4-minio.yaml
     ```

3. **Configure Flask Application**:
   - Update `DB_HOSTNAME` in `utils/photo-table.py` and create the database table:
     ```bash
     python3 utils/photo-table.py
     ```
   - Deploy the Flask application:
     ```bash
     kubectl apply -f configuration/5-app.yaml
     ```

4. **Access Application**:
   - Use Minikube to get the application URL:
     ```bash
     minikube service <service-name>
     ```

5. **Clean Up Resources**:
   - Delete resources:
     ```bash
     kubectl delete -f configuration/
     ```
   - Stop Minikube:
     ```bash
     minikube delete
     ```

---

## Testing

### Functionalities
- **Photo Upload**: Upload photos and verify persistence.
- **Album Creation**: Create and manage albums.
- **Search**: Perform searches by metadata.
- **Photo Details**: Retrieve and modify metadata.

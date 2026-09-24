JSONResponse(status_code=400, content={"error": "Dados inválidos"})

app.include_router(profiles.router, prefix="/api/profiles", tags=["Profiles"])
app.include_router(technologies.router, prefix="/api/technologies", tags=["Technologies"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])

@app.get("/")
def root():
    return {"message": "DevShowcase API v2 rodando! Acesse /docs"}

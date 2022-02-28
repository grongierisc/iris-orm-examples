package org.acme.hibernate.orm;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.transaction.Transactional;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.WebApplicationException;
import javax.ws.rs.core.Response;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;
import javax.json.Json;

import org.jboss.resteasy.annotations.jaxrs.PathParam;

@Path("Persons")
@ApplicationScoped
@Produces("application/json")
@Consumes("application/json")
public class PersonResource {

    @GET
    public List<Person> get() {
        return Person.listAll();
    }
    @GET
    @Path("{id}")
    public Person getSingle(@PathParam Long id) {
        Person entity = Person.findById(id);
        if (entity == null) {
            throw new WebApplicationException("Person with id of " + id + " does not exist.", 404);
        }
        return entity;
    }
    @POST
    @Transactional
    public Response create(Person Person) {
        if (Person.id != null) {
            throw new WebApplicationException("Id was invalidly set on request.", 422);
        }
        Person.persist();
        return Response.ok(Person).status(201).build();
    }
    @PUT
    @Path("{id}")
    @Transactional
    public Person update(@PathParam Long id, Person person) {
        if (person.name == null) {
            throw new WebApplicationException("Person Name was not set on request.", 422);
        }
        Person entity = Person.findById(id);
        if (entity == null) {
            throw new WebApplicationException("Person with id of " + id + " does not exist.", 404);
        }
        entity.name = person.name;
        entity.surname = person.surname;

        return entity;
    }
    @DELETE
    @Path("{id}")
    @Transactional
    public Response delete(@PathParam Long id) {
        Person entity = Person.findById(id);
        if (entity == null) {
            throw new WebApplicationException("Person with id of " + id + " does not exist.", 404);
        }
        entity.delete();
        return Response.status(204).build();
    }
    @Provider
    public static class ErrorMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception exception) {
            int code = 500;
            if (exception instanceof WebApplicationException) {
                code = ((WebApplicationException) exception).getResponse().getStatus();
            }
            return Response.status(code)
                    .entity(Json.createObjectBuilder().add("error", exception.getMessage()).add("code", code).build())
                    .build();
        }
    }
}

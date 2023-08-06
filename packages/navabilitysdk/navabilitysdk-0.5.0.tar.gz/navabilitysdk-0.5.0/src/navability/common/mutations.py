# This will become common across all SDKs so we can't assume it's going to flake cleanly.
# flake8: noqa

GQL_ADDVARIABLE = """
mutation sdk_addVariable ($variable: FactorGraphInput!) {
    addVariable(variable: $variable)
}
"""


GQL_ADD_VARIABLE_PACKED = """
mutation sdk_add_variable_packed(
    $variablePackedInput: AddVariablePackedInput!, 
    $options: AddVariablePackedOptionsInput
  ) {
  addVariablePacked(variable: $variablePackedInput, options:$options) {
    context {
      eventId
    }  
    status {
      state
      progress
    }
  }
}
"""


GQL_INIT_VARIABLE = """
mutation sdk_init_variable(
    $variable: InitVariableInput!, 
    $options: EmptyOptionsInput
  ) {
  initVariable(variable: $variable, options:$options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""


GQL_ADDFACTOR = """
mutation sdk_addFactor ($factor: FactorGraphInput!) {
  addFactor(factor: $factor)
}
"""


GQL_DELETEFACTOR = """
  mutation sdk_delete_factor(
    $factor: DeleteFactorInput!, 
    $options: DeleteFactorOptionsInput
  ) {
  deleteFactor(factor: $factor, options: $options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""


GQL_SOLVESESSION = """
mutation sdk_solveSession ($client: ClientInput!, $options: SolveOptionsInput) {
  solveSession(client: $client, options: $options)
}
"""


MUTATION_EXPORT_SESSION = """
mutation sdk_export_session(
    $session: ExportSessionInput!, 
    $options: ExportSessionOptions
  ){
  exportSession(session:$session, options:$options) {
    context {
      eventId
    }
    status {
      state
      progress
    }
  }
}
"""



## =============================================================
## BlobEntry => Blob
## =============================================================


GQL_CREATEDOWNLOAD = """
mutation sdk_url_createdownload ($userId: String!, $blobId: ID!) {
  url: createDownload(
    userId: $userId
    fileId: $blobId
  )
}
"""


GQL_CREATEUPLOAD = """
mutation sdk_url_createupload($blobLabel: String!, $blobSize: BigInt!, $parts: Int!) {
  createUpload(
    file: {
      filename: $blobLabel,
      filesize: $blobSize
    },
    parts: $parts
  ) {
    uploadId
    parts {
      partNumber
      url
    }
    file {
      id
    }
  }
}
"""


GQL_COMPLETEUPLOAD_SINGLE = """
mutation completeUpload($blobId: ID!, $uploadId: ID!, $eTag: String) {
  completeUpload (
    fileId: $blobId,
    completedUpload: {
      uploadId: $uploadId,
      parts: [
        {
          partNumber: 1,
          eTag: $eTag
        }
      ]
    }
  )
}
"""

# TODO deprecate and remove, use GQL_ADDBLOBENTRY instead
GQL_ADDDATAENTRY = """
mutation sdk_adddataentry($userId: ResourceId!, $robotId: ResourceId!, $sessionId: ResourceId!, $variableLabel: String!, $blobId: UUID!, $dataLabel: String!, $mimeType: String) {
  addDataEntry (
    dataEntry: {
      client: {
        userId: $userId,
        robotId: $robotId,
        sessionId: $sessionId
      },
      blobStoreEntry: {
        id: $blobId,
        label: $dataLabel
        mimetype: $mimeType
      },
      nodeLabel: $variableLabel
    }
  )
}
"""

GQL_ADDBLOBENTRY = """
mutation sdk_addblobentry(
  $userId: String!
  $robotId: String!
  $sessionId: String!
  $variableLabel: String!
  $blobId: UUID!
  $blobLabel: String!
  $blobSize: Int!
  $mimeType: String
) {
  addBlobEntry(
    blob: {
      id: $blobId
      label: $blobLabel
      size: $blobSize
      mimeType: $mimeType
      blobstore: NAVABILITY
    }
    options: {
      links: [
        {
          key: {
            user: { userLabel: $userId }
            variable: {
              userId: $userId
              robotId: $robotId
              sessionId: $sessionId
              variableLabel: $variableLabel
            }
          }
        }
      ]
    }
  ) {
    context {
      eventId
    } 
    status {
      state
      progress
    }
  }
}
"""
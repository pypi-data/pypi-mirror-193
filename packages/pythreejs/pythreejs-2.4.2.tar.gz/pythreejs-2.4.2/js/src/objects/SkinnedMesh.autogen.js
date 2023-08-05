//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var MeshModel = require('./Mesh.js').MeshModel;

var SkeletonModel = require('./Skeleton.autogen.js').SkeletonModel;

class SkinnedMeshModel extends MeshModel {

    defaults() {
        return _.extend(MeshModel.prototype.defaults.call(this), {

            bindMode: "attached",
            bindMatrix: [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
            skeleton: null,
            type: "SkinnedMesh",

        });
    }

    constructThreeObject() {

        var result = new THREE.SkinnedMesh(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry'),
            this.convertThreeTypeArrayModelToThree(this.get('material'), 'material')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        MeshModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('skeleton');

        this.props_created_by_three['morphTargetInfluences'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['bindMode'] = null;
        this.property_converters['bindMatrix'] = 'convertMatrix';
        this.property_converters['skeleton'] = 'convertThreeType';
        this.property_converters['type'] = null;

        this.property_assigners['bindMatrix'] = 'assignMatrix';

    }
}

SkinnedMeshModel.model_name = 'SkinnedMeshModel';
SkinnedMeshModel.serializers = {
    ...MeshModel.serializers,
    skeleton: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    SkinnedMeshModel: SkinnedMeshModel,
};

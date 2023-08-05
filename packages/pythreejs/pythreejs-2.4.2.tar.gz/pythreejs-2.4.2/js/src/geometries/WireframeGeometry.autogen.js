//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;

var BaseBufferGeometryModel = require('../core/BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;

class WireframeGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            geometry: null,
            type: "WireframeGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.WireframeGeometry(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('geometry');

        this.props_created_by_three['type'] = true;

        this.property_converters['geometry'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

WireframeGeometryModel.model_name = 'WireframeGeometryModel';
WireframeGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
    geometry: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    WireframeGeometryModel: WireframeGeometryModel,
};
